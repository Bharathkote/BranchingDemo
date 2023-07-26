a= int(input("Enter the number:"))
ns=str(a)


# To find the sum of the digits -  branch sumofdig
total=0
for i in ns:
    total+=int(i)

print("The sum of the digits:",total)
