"""Singleton Design Pattern.

Applicability:

1. Single DB object across modules
2. Single Logger object
3. Access control at global variables

"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance


class SingletonA(Singleton):
    def __init__(self, a):
        self.a = a


obj_1 = SingletonA(10)
print(obj_1.a)

obj_2 = SingletonA(20)
print(obj_2.a)

obj_3 = SingletonA(30)
print(obj_3.a)

print(obj_1.a, obj_2.a, obj_3.a)

print(id(obj_1))
print(id(obj_2))
print(id(obj_3))
