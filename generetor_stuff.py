def square_numbers(nums):
    for i in nums:
        yield (i*i)
        print("lol") # it executes on 2nd call

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)
print(next(my_nums))
print(next(my_nums))

# for num in my_nums:
#     print(num)


# my_nums = (x*x for x in [1,2,3,4,5])
#
# print list(my_nums) # [1, 4, 9, 16, 25]
