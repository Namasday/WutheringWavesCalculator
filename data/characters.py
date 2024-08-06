import os, json

datapath = 'json/'  # 人物json文件路径

# 人物名列表
listChara = os.listdir(datapath)
listChara = [file[:-5] for file in listChara]


def open_json(charaName):
    """
    打开json文件
    :param charaName: 人物名字
    :return: 返回json数据
    """
    with open(datapath + charaName + ".json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


class MetaClass(type):
    """
    自定义元类，用以批量创建人物类
    """
    def __new__(cls, name, bases, dct):
        """
        定义类的实例属性和方法
        """
        # 动态定义属性
        data = open_json(name)
        dct['data'] = data  # 为所有通过此元类创建的类添加一个属性

        # 动态定义实例方法
        def calculate(self):
            print(f"This is a custom method for {name}. Data: {self.data}")

        # 将自定义方法添加到类的字典中
        dct['calculate'] = calculate

        return super().__new__(cls, name, bases, dct)


def create_classes_with_metaclass(names):
    """
    批量创建类
    ：param names: 类名列表
    ：return: 返回类字典
    """
    classes = {}
    for name in names:
        cls = MetaClass(name, (object,), {})
        classes[name] = cls
    return classes


def create_instances(dictClass):
    """
    创建所有人物实例
    :param dictClass: 所有人物类字典
    :return: 返回所有人物实例字典
    """
    dictCharacters = {}
    for name, cls in dictClass.items():
        dictCharacters[name] = cls()

    return dictCharacters


dictCharaClasses = create_classes_with_metaclass(listChara)  # 创建所有人物类字典
dictCharas = create_instances(dictCharaClasses)  # 创建所有人物实例字典
