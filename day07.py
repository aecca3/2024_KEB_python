class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"

class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓추진기로 날아갑니다"

class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f"날개로 헐훨 날아갑니다~"

class SwimmingBehavior:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp, fly_behavior):
        self.__name = name
        self.hp = hp
        self.fly_behavior = fly #aggregation(has-a)

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
    #name = property(get_name, set_name)
    def __str__(self):
        return self. __name + "입니다"

    def __add__(self, target):
        return self.__name + " + " + target.__name
        return f"두 포켓몬스터 체력의 합은 {self.hp + target.hp}입니다."
class Pikachu(Pokemon):
    pass

class Charizard(Pokemon):
    pass
nofly = NoFly()
g1 = Pikachu("피카츄", 35, nofly) #LSP
wings = FlyWithWings()
c1 = Charizard("리자몽", 120, wings) #LSP
c1.fly.fly()
print(g1)
print(c1)
print(g1+c1)
print(c1.fly_behavior.fly())
print(g1.fly_behavior.fly())
#print(g1+200)

#색깔 비워진 마름모 aggregation(각 파트들의 lifestyle이 다르다)/
#색깔 채워진 마름모는 compostion

# #magic method
# def __str(self):
#     return self.__name + "입니다"
# def __add__(self):
#     return self.__name + " + " + target.__name