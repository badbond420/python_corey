# def addnum(num):
#     def inner(another_num):
#         return num + another_num
#     return inner
#
# add3 = addnum(3)
# add4 = addnum(4)
# print(add3(3),add4(3))

class addnum:
    def __init__(self,num):
        self.num = num

    def __call__(self,num):
        return num + self.num

add3 = addnum(3)
add4 = addnum(4)
print(add3(3),add4(3))