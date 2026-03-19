pal = input("Enter your palindrome: ")
pal = pal.lower()
pal2 = pal[::-1]
if pal == pal2:
    print("Palindrome")
else:
    print("Not Palindrome")
