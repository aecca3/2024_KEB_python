# #캐릭터 3개라고 치자/
# # 1)리자몽 :체력 10/공격: 펀치->남의꺼 -2/방어:쭈구리기->남의거안통함
# # 2)꼬북이 : 체력 15/ 공격: 발차기->남의꺼 -1/ 방어: 숨기->남의거안통함
# # 3)피카츄 : 체력 20/ 공격: 전기충격->남의꺼 -3/ 방어: 방패->남의거안통함
#
# #attack/attack attack/defence defence/attack defence/defence
#
# import random
# character_list = ["Charizard", "Kobuk", "Pikachyu"]
# random_character = random.choice(character_list)
#
# class Charizard:
#     def __init__(self):
#         self.life = 10
#     def kick(self):
#         self.enemylife -= 2
#         if #enemy defence, enemy life = current enemy life
#         elif #enemy attack, my life -= random enemys' attack value
#         else #누군가의 life가 0이 될때까지 계속 반복
#     def crouch(self):
#         self.mylife = self.life
#
# class Kobuk:
#     def __init__(self):
#         self.life = 15
#     def punch(self):
#         self.enemylife -= 1
#         if #enemy defence, enemy life = current enemy life
#         elif #enemy attack, my life -= random enemys' attack value
#         else #누군가의 life가 0이 될때까지 계속 반복 0이나 -가 되면 게임종료
#     def hide(self):
#         self.mylife = self.life
#
# mode_choice = True
# while True:
#     print("Choose one")
#     menu = input("1)Attack 2)Defence")
#     if menu == '1' : #상대방은 공격을 랜덤하게 함
#
#
#
# import random

# def Pikachyu_value():
#     life = int(20)
#     electric shock =
#     shield =



while True:
    print("You wanna play the Pokemon Game?")
    menu = input("1)PLAY 2)QUIT")

    if menu == '1':
        print("Your charcter will be randomly designated.\nLoading...")
        import random
        character_list = ["Charizard", "Kobuk", "Pikachyu"]
        random_character = random.choice(character_list)
        import time
        time.sleep(2)
        print(f"Your charcter is {random_character}")
        import time
        time.sleep(2)
    # def enemy_choice():
        print(f"Enemy's character will be randomly designated.\nLoading...")
        import random
        character_list = ["Charizard", "Kobuk", "Pikachyu"]
        random_character = random.choice(character_list)
        import time
        time.sleep(2)
        print(f"Enemy's character is {random_character}")
    # inner_while_condition = True
    # while inner_while_condition:
        import time
        time.sleep(2)
    print("Continue or Run away?")
    menu = input("1)Continue 2)Run away")
    if menu == '1':
        pass
    if menu == '2':
            print("You are moving to another area.\nLoading...")
            import time
            time.sleep(2)
            print("You are in new area.\nEnemy's character will be randomly designated.\nLoading... ")

    #
    # if menu == '2':
    #     print("GOOD-BYE")
    #     break


