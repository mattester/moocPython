#集合的数学运算
#交集，获取两个集合中重复的部分，新建一个集合
college1 = {'哲学','经济学','教育学',"法学"}
college2 = set(['金融学","哲学','经济学','历史学',"文学"])
c3 = college1.intersection(college2)
print(c3) #{'经济学'}

#更新原有的集合,update会见执行的结果重新写入到college1中，对
#原有的集合产生变化
college1.intersection_update(college2)
print(college1) #{'经济学'}

college1 = {'哲学','经济学','教育学',"法学"}

#并集，将两个集合所有元素合并，去重
c4 = college1.union(college2)
print(c4) #{'经济学', '教育学', '金融学","哲学', '历史学', '法学', '文学', '哲学'}

#差集，指两个集合中间差异的部分
#difference代表得到a在b集合中不存在的部分
c5 = college1.difference(college2)
print(c5) #{'哲学', '教育学', '法学'}

#symmetric_difference代表双向差集
c6 = college1.symmetric_difference(college2)
print(c6) #{'金融学","哲学', '法学', '历史学', '哲学', '文学', '教育学'}
#将a在b集合中不存在的部分+b在集合中不存在的部分一起放在一个新集合里面

college1.symmetric_difference_update(college2)
print(college1) #{'金融学","哲学', '教育学', '历史学', '法学', '文学', '哲学'}









