from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import os
import sys
import json
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '..')))
os.environ["FLAGS_allocator_strategy"] = 'auto_growth'
import paddle
from ppocr.data import create_operators, transform
from ppocr.modeling.architectures import build_model
from ppocr.postprocess import build_post_process
from ppocr.utils.save_load import init_model
from ppocr.utils.utility import get_image_file_list
import tools.program as program


def main():
    global_config = {'debug': False, 'use_gpu': False, 'epoch_num': 150, 'log_smooth_window': 20, 'print_batch_step': 10, 'save_model_dir': './output/rec/r34_vd_none_bilstm_ctc/', 'save_epoch_step': 20, 'eval_batch_step': [0, 2000],
                     'cal_metric_during_train': True, 'pretrained_model': 'output/rec/r34_vd_none_bilstm_ctc/best_accuracy', 'checkpoints': None, 'save_inference_dir': None, 'use_visualdl': False, 'infer_img': 'data/test/',
                     'character_dict_path': 'ppocr/utils/dianbiao.txt', 'character_type': 'en', 'max_text_length': 25, 'infer_mode': False, 'use_space_char': False, 'save_res_path': './output/rec/predicts_r34_vd_none_bilstm_ctc.txt',
                     'distributed': False, 'load_static_weights': False}
    # build post process
    post_process_class = build_post_process( {'name': 'CTCLabelDecode'}, global_config)

    # build model
    if hasattr(post_process_class, 'character'):
        char_num = len(getattr(post_process_class, 'character'))
        if config['Architecture']["algorithm"] in ["Distillation",]:  # distillation model

            for key in config['Architecture']["Models"]:
                config['Architecture']["Models"][key]["Head"][
                    'out_channels'] = char_num
        else:  # base rec model
            config['Architecture']["Head"]['out_channels'] = char_num

    model = build_model(config['Architecture'])

    init_model(config, model)

    # create data ops
    transforms = []
    for op in config['Eval']['dataset']['transforms']:
        op_name = list(op)[0]
        if 'Label' in op_name:
            continue
        elif op_name in ['RecResizeImg']:
            op[op_name]['infer_mode'] = True
        elif op_name == 'KeepKeys':
            if config['Architecture']['algorithm'] == "SRN":
                op[op_name]['keep_keys'] = [
                    'image', 'encoder_word_pos', 'gsrm_word_pos',
                    'gsrm_slf_attn_bias1', 'gsrm_slf_attn_bias2'
                ]
            else:
                op[op_name]['keep_keys'] = ['image']
        transforms.append(op)
    global_config['infer_mode'] = True
    ops = create_operators(transforms, global_config)

    save_res_path = config['Global'].get('save_res_path',
                                         "./output/rec/predicts_rec.txt")
    if not os.path.exists(os.path.dirname(save_res_path)):
        os.makedirs(os.path.dirname(save_res_path))

    model.eval()

    with open(save_res_path, "w") as fout:

        # =================================================
        # =======================原图像图像文件夹路径==========
        # =================================================
        for file in get_image_file_list("data/test/"):
            # print("file:",file)
            with open(file, 'rb') as f:
                img = f.read()
                data = {'image': img}
            batch = transform(data, ops)
            if config['Architecture']['algorithm'] == "SRN":
                encoder_word_pos_list = np.expand_dims(batch[1], axis=0)
                gsrm_word_pos_list = np.expand_dims(batch[2], axis=0)
                gsrm_slf_attn_bias1_list = np.expand_dims(batch[3], axis=0)
                gsrm_slf_attn_bias2_list = np.expand_dims(batch[4], axis=0)

                others = [
                    paddle.to_tensor(encoder_word_pos_list),
                    paddle.to_tensor(gsrm_word_pos_list),
                    paddle.to_tensor(gsrm_slf_attn_bias1_list),
                    paddle.to_tensor(gsrm_slf_attn_bias2_list)
                ]

            images = np.expand_dims(batch[0], axis=0)
            images = paddle.to_tensor(images)

            if config['Architecture']['algorithm'] == "SRN":
                preds = model(images, others)
            else:
                preds = model(images)

            post_result = post_process_class(preds)
            print("post_result:",post_result)
            info = None
            if isinstance(post_result, dict):
                rec_info = dict()
                for key in post_result:
                    if len(post_result[key][0]) >= 2:
                        rec_info[key] = {
                            "label": post_result[key][0][0],
                            # "score": post_result[key][0][1],
                        }
                info = json.dumps(rec_info)
            else:
                if len(post_result[0]) >= 2:
                    info = post_result[0][0] # + "\t" + str(post_result[0][1])

            if info is not None:
                # print("info:",info)
                #print("file:",file)
            # ============================识别结果=============================
                fout.write(file + "\t\n" + info)
    print("完成：")

if __name__ == '__main__':
    # config, device, logger, vdl_writer = program.preprocess()
    config = {'Global': {'debug': False, 'use_gpu': False, 'epoch_num': 150, 'log_smooth_window': 20, 'print_batch_step': 10, 'save_model_dir': './output/rec/r34_vd_none_bilstm_ctc/', 'save_epoch_step': 20,
    'eval_batch_step': [0, 2000],'cal_metric_during_train': True, 'pretrained_model': 'output/rec/r34_vd_none_bilstm_ctc/best_accuracy', 'checkpoints': None, 'save_inference_dir': None, 'use_visualdl': False,
    'infer_img': 'data/test/', 'character_dict_path': 'ppocr/utils/dianbiao.txt', 'character_type': 'en', 'max_text_length': 25, 'infer_mode': False, 'use_space_char': False,
    'save_res_path': './output/rec/predicts_r34_vd_none_bilstm_ctc.txt', 'distributed': False, 'load_static_weights': False},'Optimizer': {'name': 'Adam', 'beta1': 0.9, 'beta2': 0.999, 'lr': {'learning_rate': 0.0005},
    'regularizer': {'name': 'L2', 'factor': 0}}, 'Architecture': {'model_type': 'rec', 'algorithm': 'CRNN', 'Transform': None, 'Backbone':{'name': 'ResNet', 'layers': 34}, 'Neck': {'name': 'SequenceEncoder', 'encoder_type': 'rnn', 'hidden_size': 256},
    'Head': {'name': 'CTCHead', 'fc_decay': 0}}, 'Loss': {'name': 'CTCLoss'}, 'PostProcess': {'name': 'CTCLabelDecode'},'Metric': {'name': 'RecMetric', 'main_indicator': 'acc'}, 'Train': {'dataset': {'name': 'SimpleDataSet',
    'data_dir': 'E:/shijueshibie/ORC/PaddleOCR-release-2.2/train_data/2015/', 'label_file_list': ['E:/shijueshibie/ORC/PaddleOCR-release-2.2/train_data/2015/train_lable1.txt'], 'transforms': [{'DecodeImage': {'img_mode': 'BGR', 'channel_first': False}},
    {'CTCLabelEncode': None}, {'RecResizeImg': {'image_shape': [3, 32, 100]}}, {'KeepKeys': {'keep_keys': ['image', 'label', 'length']}}]}, 'loader': {'shuffle': True, 'batch_size_per_card': 32, 'drop_last': True, 'num_workers': 8}},
    'Eval': {'dataset': {'name': 'SimpleDataSet', 'data_dir': 'E:/shijueshibie/ORC/PaddleOCR-release-2.2/train_data/2015/', 'label_file_list': ['E:/shijueshibie/ORC/PaddleOCR-release-2.2/train_data/2015/test_lable1.txt'],
    'transforms': [{'DecodeImage': {'img_mode': 'BGR', 'channel_first': False}}, {'CTCLabelEncode': None}, {'RecResizeImg': {'image_shape': [3, 32, 100]}}, {'KeepKeys': {'keep_keys': ['image', 'label', 'length']}}]},
    'loader': {'shuffle': False, 'drop_last': False, 'batch_size_per_card': 32, 'num_workers': 8}}}

    main()
