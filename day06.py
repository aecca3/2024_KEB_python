import random

# numbers = list()
# for i in range(5):
#     numbers. append(random.randint(1, 100))
numbers = [random.randint(1, 100) for i in range(10)] #range 5는 5번 반복, 즉 5개를 뺴라
print(numbers)
try :
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) "))
    print(numbers[pick])
    print(5/0)
except IndexError as err:
    print(f"Out of range : Wrong index number\n{err}")
except ValueError as err:
    print(f"Input Only Number~\n{err}")
except ZeroDivisionError as err :
    print(f"The denomiator cannot be 0.\n{err}")
# except Exception as err:
#     print(f"Error occurs : {err}") #보험으로 제일 마지막으로 들어가고 디테일한 예외처리들이 선행되서 나온다
