# - If we put input as 3, that means the no. of alphabets in the output will be 3 which are A, B, C.
# - If we put input as 4, that means the no. of alphabets in the output will be 4 which are A, B, C, D


def diamond(n):
    alphabets = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    for i in range(n):
        print(' ' * (n-i) + alphabets[:2*i+1])

    for i in range(n-2, -1, -1):
        print(' ' * (n-i) + alphabets[:2*i+1])

diamond(3)
diamond(5)


