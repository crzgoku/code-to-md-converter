#-q
# 7. Write a python program to find the maximum of three numbers. Please note that the code
# to find the maximum of three numbers is to be written in a function.
#-q
def find_max_of_three(a, b, c):
    big = a if a>b else b
    big = big if  big>c else c
    print("Maximum of three is ", big)

find_max_of_three(4,23,5)