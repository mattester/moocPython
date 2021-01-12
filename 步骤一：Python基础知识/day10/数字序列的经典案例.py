#利用range遍历其序列
c = 'abcdefg'
list = []
for i in range(0,len(c)):
    letter = c[i]
    print(letter)
    #保存到列表中
    list.append(letter)
    print(list)

#斐波那契数列 （后一个数等于前两个数之和） q
#1,1,2,3,5,8,13,21...(前两位固定是1）
#1到50的斐波拉契数列
#定义一个数列
result = []
for i in range(0,50):
    if i == 0 or i ==1:
        result.append(1)
    else:
        result.append(result[i - 2] + result[i -1])
print(result)

#判断质数，质数的定义：在大于1的自然数中，除了1和他本身以外能够被整除，不在有其他因素的数字，就是质数
# z = 776351721
z = int(input("请输入数字"))
is_prime = True
for i in range(2,z):
    if z % i == 0:

       is_prime = False #这里是一个等于号，不是比价运算符
       break
if is_prime == True:
    print('{0}是质数'.format(z))
else:
    print('{0}不是质数'.format(z))






