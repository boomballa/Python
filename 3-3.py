# coding:utf8

class Programer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight


    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return  self.__weight

    def self_introduction(self):
        print ("My Name is %s \nI am %s years old\n") % (self.name, self.age)

if __name__ == '__main__':
    programer = Programer('Albert', 25 ,80)
    print (dir(programer))
    print (Programer.get_hobby())
    print (programer.get_weight)
    programer.self_introduction()