a= int(input("Enter the number:"))
ns=str(a)


# To find the sum of the digits -  branch sumofdig
total=0
count=0
for i in ns:
    total+=int(i)
    count+=1

print("The sum of the digits:",total)


print("The average of digits is:",total/count)

print("The sum & Avg",total,total/count)