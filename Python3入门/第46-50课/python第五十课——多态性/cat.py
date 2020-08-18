#！/usr/bin/env python
# Author:Hank

from animal import Animal

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def eat(self):
        print(self.name + "正在进食...")