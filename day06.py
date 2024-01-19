class Pokemon :
    def __init__(self, name):
        self.name = name
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을 공격!")
class Pikachu(Pokemon): #Pikachu is a Pokemon 상속이 되는 것 부모를 보면 된다/
    # #추상화된 언어(abstract class instance는 볼 수 없지만 분류나 상속의 목적으로... 이 예시에선 포켓몬)
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을 {self.type} 공격!")
    def electric_info(self) :
        print("전기 계열의 공격을 합니다")
class Squirtle(Pokemon) :
    pass

class Agumon(Pokemon) :
    pass

p1 = Pikachu("피카츄", "전기")
p2 = Squirtle("꼬부기")
p3 = Pokemon("아무개")
p1.electric_info()
#p3.electric_info()
p1.attack(p2)
p2.attack(p1)
print(p1.name, p2.name)
print(p1.name)
print(issubclass(Pikachu, Pokemon))
print(issubclass(Agumon, Pokemon))