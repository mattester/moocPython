source = "7782,CLARK,MANAGER,SALES,5000$7934,MILLER,SALESMAN,SALES,3000$7369,SMITH,ANALYST,RESEARCH,2000"
#定义一个所有员工的字典allyg{编号：员工属性}
#定义单个员工的字典oneyg{工号:no,姓名:name,岗位:job,部门:department,工资:salary}
allyg = {}
#分割字符串
yg_list = source.split("$")
print(yg_list)
#把总员工列表里面的单个员工给取出来
#1：找到这个列表的索引值，通过索引值给列表取值然后用split进行分割
for i in range(0,len(yg_list)):
    print(i)
    e = yg_list[i].split(',')
    print(e)

#将分割好的列表，添加key变成单个员工字典
oneyg = {'no':e[0],'name':e[1],'job':e[2],'departemt':e[3],'salary':e[4]}
print(oneyg)
#单个员工字典放入到总员工字典中,新增一个key，首先就要有这个字典
allyg[oneyg['no']] = oneyg
print(allyg)

while True:
# 以上就全完成了，接下来就是查询
#输入编号，判断字典中有没有这个编号就行了，这个编号就是key
    shulu = input("请输入员工编号")
    if shulu == "":
        break
    if shulu in allyg:
        emp = allyg.get(shulu)
        print(allyg.get(shulu))
        #对字典进行格式化
        print("工号:{no},名字:{name},岗位:{job},部门:{departemt},工资:{salary}".format_map(emp))
    else:
        print("编号不在里面")



