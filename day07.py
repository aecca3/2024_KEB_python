class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"

class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓추진기로 하늘을 날아갑니다"

class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f"날개로 헐훨 날아갑니다~"


class Pikachu:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.fly_behavior = NoFly() #composition


nofly = NoFly()
p1 = Pikachu("피카츄", 35)
print(p1.fly_behavior.fly())
#wings = FlyWithWings()

#c1.fly.fly()
# print(p1)
# print(p1.fly_behavior.fly())
# p1.set_fly_behavior(JetPack())
# print(p1.fly_behavior.fly())
#print(g1+200)

#색깔 비워진 마름모 aggregation(각 파트들의 lifestyle이 다르다)/
#색깔 채워진 마름모는 compostion

# #magic method
# def __str(self):
#     return self.__name + "입니다"
# def __add__(self):
#     return self.__name + " + " + target.__name