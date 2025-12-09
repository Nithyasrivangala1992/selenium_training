# num = int(input("Enter the number : "))
#
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# ################################################################
#
# for num in range(1, 20):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")


# ################################################################
#
# def even_odd(start, end):
#     for num in range(start, end):
#         if num%2==0:
#             print("even")
#         else:
#             print("odd")
#
# even_odd(10, 20)
# even_odd(101, 201)


################################################################


# def even_odd(start, end):
#     even_list = []
#     odd_list = []
#     for num in range(start, end):
#         if num%2==0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)
#
#     return odd_list
#     return even_list
#
#
# even_odd(10, 20)
# even_odd(101, 201)



def even_odd(start, end):
    even_list = []
    odd_list = []
    for num in range(start, end):
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    yield odd_list
    yield even_list


even_odd(10, 20)
even_odd(101, 201)






































