with open('./1000000.txt', 'r') as f:
    pi = f.read()

start = int(input('请输入想要获取多少位小数点开始的数: ')) + 1
length = int(input('请输入想要获取多少位数据长度: '))

print('结果是:{}'.format(pi[start:start + length]))
