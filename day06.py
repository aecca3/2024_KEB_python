def get_odds(n) -> int:
    """
    1부터 n까지의 홀수를 발생시키는 제너레이터
    :param n: int
    :return: int
    """
    for i in range(1, n+1, 2):
        yield i
cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt = cnt + 1
    if cnt == 3:
        print(f'Third number is {odd} ')
        break

# #9.2
# #range(10)의 홀수를 반환하는 get_odds generator 함수를 정의해보자.
# #for문으로 반환된 세 번째 홀수를 찾아서 출력한다.
# def get_odds():
#     for x in range(1, 10, 2):
#         yield x
#
# count = 0
# for x in get_odds():
#     count += 1
#     if count == 3:
#         third_odd = x
#         break
# print(f'세 번째 홀수는 {third_odd} 입니다.')
#
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
