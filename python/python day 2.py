# #Peterson number
# #number =145
# no=int(input("enter the value:"))
# rev=0 
# while no>0:
#   rem=no%10
#   rev=rev*10+rem
#   no=no//10
# print("reverse no is",rev)

#1.count no of digits 
#no=123456 ans =6
# no=int(input("enter the value:"))
# count=0 
# while no>0:
#       no=no//10
#       count=count+1
# print("no of digit",count)

# #2.sum of digit
# no=int(input("enter the value:"))
# sum=0 
# while no>0:
#       rem=no%10
#       no=no//10
#       sum=sum+rem
# print("sum of digit",sum)

#3.check no is palindrome
# no=int(input("enter the no:"))
# rev=0 
# t=no
# while no>0:
#     rem=no%10
#     rev=rev*10+rem
# if no==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

#4.check no is armstrong
# no=int(input("enter the value:"))
# sum=0 
# temp=no
# count=0
# while no>0:
#         no=no//10
#         count=count+1
# no=temp
# while no>0: 
#         rem=no%10
#         no=no//10
#         sum=sum+rem**count
# if temp==sum:
#             print("armstrong")
# else:
#             print("not armstrong")

#5.
# for i in range (1,10000):
#     no=i
#     sum=0 
#     temp=no
#     count=0
#     while no>0:
#             no=no//10
#             count=count+1
#     no=temp
#     while no>0: 
#             rem=no%10
#             no=no//10
#             sum=sum+rem**count
#     if t==sum:
#             print(i)