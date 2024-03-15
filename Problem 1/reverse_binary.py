"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Nhi Tran
Lab Time:

"""

def reverse_binary():
    user_num = int(input())
    binary_representation = ""

    while user_num > 0:
        binary_representation += str(user_num % 2)
        user_num //= 2

    print(binary_representation)

if __name__ == "__main__":
    reverse_binary()
