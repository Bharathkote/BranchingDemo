a=int(input("Enter a number:"))
ns=str(a)

# To check whether the number is palindrome or not
if ns == ns[::-1]:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

print("The number is",a)
print("The reverse of the number is :",ns[::-1])
print("the sum of num and the reverse is:",a+int(ns[::-1]))
