def test(f):
    """
    데코레이터 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    """
    #def test_in
    def test_in(): #test in 은 closure다
        print('start')
        #result = f(*args, **kwargs)
        f()
        print('end')
        #return result
    return test_in
@test
def greeting():
    print("안녕하세요~")

greeting()
# #9.3
# #어떤 함수가 호출되면 'start'를, 끝나면 'end'를 출력하는 test decorator를 정의해보자.
# def test_decorator(func) :
#     def new_func(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return new_func()
#
# @test_decorator
# def my_function():
#     print('함수 실행 중')
#
# my_function
#
# #9.4
