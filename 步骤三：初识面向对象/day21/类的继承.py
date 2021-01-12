#定义基础类为猫科动物类
"""
              基础类BzseCat
         |              |                |
老虎类 Tiger     熊猫类Panda       家猫类Petcat

                                |                  |
                            短毛猫Duancat       田园猫Huacat

"""
class cat2():
    pass

class BaseCat(object):
    """"猫科动物类"""
    tag = "猫科动物类" #标签，类的类型

    def __init__(self,name):
        self.name = name

    def eat(self):
        print("猫吃东西")

class Tiger(BaseCat):
    """老虎类"""
    def eat(self):
        super(Tiger,self).eat()
        print("我喜欢吃肉")


class Panda(BaseCat):
    """熊猫类"""
    def eat(self):
        super(Panda,self).eat()
        print("我吃竹子")


class Petcat(BaseCat):
    """家猫类"""
    def eat(self):
        super(Petcat,self).eat()
        print("我吃猫粮")


class Duancat(Petcat):
    def eat(self):
        super(Duancat,self).eat()
        print("我吃短毛")


class Huacat(Petcat):
    def eat(self):
        super(Huacat,self).eat()
        print("我吃小鱼干")


if __name__ == '__main__':
    cat = Huacat("小黄")
    cat.eat()

#验证子类信息
print(issubclass(Panda,BaseCat))
print(issubclass(Panda,cat2))