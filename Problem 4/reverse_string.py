"""
Complete the following python code to reverse the string entered by the user.

Name: 
Lab Time:
"""
def reverse_string():
    while True:
        text = input()
        if text.lower() in ["done", "d"]:
            break
        else:
            print(text[::-1])

if __name__ == "__main__":
    reverse_string()
