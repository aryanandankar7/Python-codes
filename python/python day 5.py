# #accept 5 numbers and find max no.
# n1=int(input("enter the value:"))
# n2=int(input("enter the value:"))
# n3=int(input("enter the value:"))
# n4=int(input("enter the value:"))
# max=n1
# if n2>max:
#     max=n2
# if n3>max:
#     max=n3
# if n4>max:
#     max=n4
# print("max number is",max)

#find minimum and maximum element 
# arr=[6,7,22,5,9]
# max=arr[0]
# min=arr[0]
# for i in arr:
#     if i<min:
#      min=i
#     if i>max:
#      max=i
# print("maximum is:",max)
# print("minimum is:",min)

#check leap year
# year=int(input("Enter the year:"))
# if year%100!=0:
#     if year%4==0:
#         print("Non century leap year")
#     else:
#         print("Not leap year")
# else:
#     if year%400==0:
#         print("Century leap year")
#     else:
#         print("Not leap year")

#tech number
# no=2201
# n1=no%100
# n2=no//100
# n3=n1+n2
# n4=n3*n3
# if n4==no:
#     print("tech no")
# else:
#     print("non tech")

# # rearrange postive -ve nmuber in pattern +-+-+-+-+-+-
# arr = [1, -2, -3, -4, 5, 6]

# pos = []
# neg = []

# for i in arr:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# result = []
# for i in range(min(len(pos), len(neg))):
#     result.append(pos[i])
#     result.append(neg[i])

# print(result)
# #sum of array


# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'simpleArraySum' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY ar as parameter.
# #

# def simpleArraySum(ar):
#     # Write your code here
#     sum=0
#     for i in range (len(ar)):
#         sum=sum+ar[i]
#     return(sum)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# #compare 4 number using if else

# n1=int(input("enter the nmuber"))
# n2=int(input("enter the nmuber"))
# n3=int(input("enter the nmuber"))
# n4=int(input("enter the nmuber"))
# max=n1

# if max<n2:
#     max=n2
# if max<n3:
#     max=n3
# if max<n4:
#     max=n4
# print(max)
        
        
    

