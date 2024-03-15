"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name:
Lab Time:
"""
def inc_5():
    first_int = int(input())
    second_int = int(input())

    if second_int < first_int:
        print("Second integer can't be less than the first.")
    else:
        while first_int <= second_int:
            print(first_int, end=' ')
            first_int += 5

    print()  # Print newline at the end

if __name__ == '__main__':
    inc_5()
