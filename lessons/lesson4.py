#class Animal:
    #def make_sound(self):
        #return "звук"
#class Flyable:
    #def move(self):
        #return "летит"
#class Swimable:
    #def move(self):
        #return "плавает"
#class A:
    #def test_method(self):
       # return "Class A"
#class B(A):
    #def test_method(self):
       # return "Class B"
#class C(A):
    #def test_method(self):
        #return "Class C"
#class D(B, C):
   # pass
#obj = B()
#print(B.__mro__)

#class Math:
    #атрибут класа
    sum = 123
    #
    #@staticmethod
    #def add(a,b):
        #return a + b

    #@classmethod
    #def get_sum(cls):
       # return cls.sum

#print(Math.add(555, 555))

#class Circle:
    #def __init__(self, radius):
       # sel.__radius = radius

    #@property
   # def get_radius(self):
        #return self.__radius
    #@property
    #def area(self):
        #return 3.14 * self.__radius


def my_decorator(func):
    def wraper():
        print('')
        func()
        print('')
        return wraper()
@my_decorator

def check_user(func):
    def wraper():
        print('Пользователь не админ')
        func()
        print('Пользователь админ')
@check_user(user)
