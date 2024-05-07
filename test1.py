
def openreadtxt(file_name):
    data = []
    file = open(file_name,'r',encoding='utf-8')  # 打开文件
    file_data = file.readlines() # 读取所有行
    for row in file_data:
        tmp_list = row.split(' ') # 按‘，’切分每行的数据
        tmp_list[-1] = tmp_list[-1].replace('\n','')  # 去掉换行符
        data.append(tmp_list)  # 将每行数据插入data中
    return data


if __name__=="__main__":
    data = openreadtxt('result.txt')
    print(data)
    '''
    # 输出图片名
    for a in data:
        for i in a[0:1]:
          print(i)
    # 输出预测结果
    for a in data:
        for i in a[1:3]:
          print(i)
    '''
    # 遍历输出
    for i in data:
        name = i[0]
        pre = i[1]

        print("name:",name)
        print("pre:",pre)

