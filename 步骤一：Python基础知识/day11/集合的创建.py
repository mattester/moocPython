# 集合的创建
# 1：使用{}符号创建集合
college1 = {'哲学','经济学','教育学',"法学"}
print(college1) #{'法学', '教育学', '经济学', '哲学'}
#为何与集合类的顺序不同，因为每一次运行产生的hash值是不一样的
# 对于集合来说它是不关心数据的，它只关心如何利用散列值快速的提取数据

#set（）内置函数从其他结构转换
college2 = set(['金融学","哲学','经济学','历史学',"文学"])
print(college2)

#利用set创建字符串集合
college3 = set('中华人民共和国')
print(college3)

#空集合创建
college4 = {}
print(type(college4))

college5 = set()
#不传入任何数据
