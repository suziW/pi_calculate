from __future__ import division
import time
print("\n欢迎来到圆周率计算器！\n")
number = int(input('请输入想要计算到小数点后的位数:'))
print("\n正在计算...\n")
time1 = time.time()

b = 10**number  # 多计算10位，防止尾数取舍的影响
x1 = b * 4 // 5  # 取整求含4/5的首项
x2 = b // -239  # 取整求含1/239的首项
he = x1 + x2  # 求第一大项
number *= 2  #设置下面循环的终点，即共计算n项
for i in range(3, number, 2):  #循环初值=3，末值n,步长=2
    x1 //= -25  #取整求每个含1/5的项及符号
    x2 //= -57121  #取整求每个含1/239的项及符号
    x = (x1 + x2) // i  #求两项之和，除以对应因子，取整
    he += x  #求总和
pai = he * 4  #求出π, 没有小数点的
paistring = str(pai)
result = paistring[0] + str('.') + paistring[1:len(paistring)]
print("计算结果：\n\n%s" % result)
time2 = time.time()
print('\n总共耗时：' + str(time2 - time1) + 's')

with open('./{}.txt'.format(number // 2), 'w') as f:
    f.write(result)
