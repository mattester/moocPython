#对于类的知识我还是不够了解，只知道一切皆对象，对象就是现实中存在的真是的东西。
#定义一个猫类
class Tiger:
    """
    判断类的实例用到的类
    """
    pass


class Cat(object):
    """猫科动物类"""
    tag = "我是家猫"
    #希望年龄保密
    def __init__(self,name,age,sex=None):
        self.name = name
        self.__age = age #两个下划线开头的表示私有的变量
        self.sex = sex
    #改变猫龄
    def set_age(self,age):
        self.__age = age

    #显示猫的信息
    def show_info(self):
        rest = ('我叫：{0},今年{1}岁'.format(self.name,self.__age))
        print('我的性别：{0}'.format(self.sex))
        print(rest)
        return rest

    def eat(self):
        """吃"""
        print("猫喜欢吃鱼")

    def catch(self):
        """猫抓老鼠"""
        print("猫抓老鼠")

    def jiao(self):
        """猫叫"""
        print("猫喵喵喵的叫")


if __name__ == '__main__':
    #实例，我家的猫叫小黑
    cat_black = Cat("小黑","2","公的")
    cat_black.eat()
    cat_black.show_info()
    print('------------------')
    print(cat_black.name)
    # print(cat_black.age)
    # print(cat_black.__age)
    print('------------------')
    #更改猫的名称
    cat_black.name = "嘿嘿"
    cat_black.show_info()

    #实例化我家小白
    print('xxxxxxxxxxxxxxxxxxx')
    cat_white = Cat("小白",3,"母的")
    cat_white.show_info()
    print(cat_white.tag)
    print(cat_black.tag)



    #类的实例判断
    print(isinstance(cat_black,Cat))
    print(isinstance(cat_white,Cat))
    print(isinstance(cat_black,Tiger))
    print(isinstance(cat_white,Tiger))
