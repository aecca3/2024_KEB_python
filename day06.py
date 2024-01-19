def desc(f): #desc:decorator->다른 함수가 필요하다 따라서 def sth나오는 것/호출은 something()이렇게 한다
    def wrapper(): #wrapper: closure/ 독립된 공간 desc 매개변수를 기억하고있다 호출한다고 나오는 것이 아님 f값을 기억한다
        print("study")
        f()
    #print("a")
    return wrapper

@desc #이렇게 @붙이면 그냥 decoration 함수 나온다....
def something():
    print("do something")

s = desc(something) #desc()이 안에 f 넣으면 s = desc(something)이렇게 선언?해줘야한다..
s()


#is prime number decorator 붙여보기