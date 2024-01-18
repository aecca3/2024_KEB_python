#closure 호출하는 함수에 있는 내부함수의 주소를 받는다/ 바깥쪽 함수의 매개변수 값도 가지고 있는 상태
def out_func(nout):
    def inner_func():
        return nout * nout
    return inner_func

x = out_func(9)
print(type(x))
print(x)
print(x())

#innerfunction
# def out_func(nout):
#     def inner_func(nin):
#         return nin * nin
#     return inner_func(nout)
#
# print(out_func(5))