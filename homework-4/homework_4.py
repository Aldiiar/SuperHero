class A:
    def __init__(self, name):
        self.name = name
class B:
    def __init__(self, age):
        self.age = age
class C(A):
    def nickname(self):
        print(f'Меня зовут - {self.name}')

class D(B):
    def y_b(self):
        print(f'Я родился в {2022 - self.age} году')

class E(C, D):
    def __init__(self, name, age):
        C.__init__(self, name)
        D.__init__(self, age)

e = E('Алдияр', 18)
e.nickname()
e.y_b()