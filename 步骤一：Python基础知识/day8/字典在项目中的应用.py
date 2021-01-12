#先谈谈思路
'''
我们有一串字符串，里面就有姓名，年龄，工资，岗位这些，我们要去处理这些字符串
这些字符串就是这种形式，“盒饭，25,9000，测试$李华，33,5666，运维”。
拿到这些字符串，我们就去把盒饭和李华的属性进行分割，使用split（“$”）进行分割
这样就变成了数组：属性记事本【“盒饭，23,9000，测试”，“李华，33,5666，运维”】而是将
以上每个员工的属性都变成了一个元素，这样这个记事本就有两个元素了

接下来我们需要定义一个员工记事本，给他们的值加上key形成key：value
 employee = {"no" : e[0],'name':e[1],'job':e[2],'department':e[3],'salary':e[4]}
 整个大记事本的字典格式是：{员工编号：员工的的各种属性}
 all_employee = {emloyee['no']} = emloyee
 以上就是整个框架搭建好了

 接下来取值就是判断key在不在中了，在就格式化输出字典'''

source = "7782,CLARK,MANAGER,SALES,5000$7934,MILLER,SALESMAN,SALES,3000$7369,SMITH,ANALYST,RESEARCH,2000"
# 保存所有解析后的员工信息,key是员工编号,value则是包含完整员工信息的字典
all_emp = {}
#将员工数据字符串分割成对应的列表
employee_list = source.split("$")
print(employee_list)
#根据索引值去取单个员工的数据
# for i in range(0,len(employee_list)):   #先看看这个员工数据有多少个元素
#     e = employee_list[i].split(',')
# print(e)
# print(i)
for i in range(0,len(employee_list)):
    #print(i)
    e = employee_list[i].split(",")
    print(e)
print(e) #在遍历外面只会输出最后一个

 # 创建员工字典
    employee = {"no" : e[0],'name':e[1],'job':e[2],'department':e[3],'salary':e[4]}
    print(employee)
    all_emp[employee['no']] = employee  #新增了一个编号为员工编号的key
print(all_emp)



