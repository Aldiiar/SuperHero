'''1hero'''
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def namehero(self):
        print(f"Hero's name is {self.name}")

    def hp(self):
        self.health_points *=2

    def __str__(self):
        return (f'His nickname {self.nickname}'
                f'\nHis power is  - {self.superpower}'
                f'\nHealth - {self.health_points}'
                f'\nHis catchphrase - {self.catchphrase}')

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Ichigo', 'Shinigami', 'Zanpacuto', 3, 'BANKAIIII!')
hero.namehero()
hero.hp()
print(hero)
print(f'{len(hero)}\n')



'''2hero'''
class Hero2(SuperHero):
    speedster = 'lightning'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly, damage):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage
        
    def hp(self):
        self.health_points **= 2

    def fly1(self):
        self.fly = True

    def phrase(self):
        return (f'fly in the {self.fly}_phrase')


hero2 = Hero2('Barry Allen', 'Flash', 'super speed', 20,
              'Меня зовут Барри Аллен, и я самый быстрый человек на Земле', False, False)

hero2.namehero()
hero2.hp()
hero2.fly1()
print(f'{hero2}\n'
      f'Fly: {hero2.fly}\n'
      f'Damage: {hero2.damage}\n'
      f'{hero2.phrase()}\n')



'''3hero'''
class Hero3(Hero2):
    levitation = 'levitation'

hero3 = Hero3('Clark', 'Superman', 'laser sight', 100000,
              'Мой грех? Спасение мира', False, False)

hero3.namehero()
hero3.hp()
hero3.fly1()
print(f'{hero3}\n'
      f'Fly: {hero3.fly}\n'
      f'Damage: {hero3.damage}\n'
      f'{hero3.phrase()}\n')



'''4monster'''
class Villain(Hero2):
    people = 'monster'

    def gen_x(self):...

    def crit(self):
        self.damage **= 2


villain = Villain('Ulquiorra Cifer', 'Arrankar', 'Gran ray sero', 4,
              'Я понял: её рука, тянущаяся ко мне — и есть душа', False, False)


villain.namehero()
villain.hp()
villain.fly1()
villain.crit()
print(f'{villain}\n'
      f'Fly: {villain.fly}\n'
      f'Damage: {villain.damage}\n'
      f'{villain.phrase()}\n')





