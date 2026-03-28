# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
#     alice=0
#     bob=0
#     for i in range (len(a)):
#       if a[i]>b[i]:
#         alice=alice+1
#       elif a[i]<b[i]:
#          bob=bob+1
#       elif a[i]==b[i]:
#          pass
#     return alice,bob

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

# n=int(input())
# ........ 1
# a=int(input())
# b=int(input())
# ........ 1
# ........ 2
# a,b=map(int,input().split())
# ........ 1 2
# a,b,c=map(int,input().split())
# ......... 1,2,3
# arr=list(map(int,input().split()))
# ......... 1 2 3 4 5 6
# arr=eval(input())
# ......... [11,22,33,44,55]
# ......... {1,3,5,7,9}
# ......... 5+3-1*15/2

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

# def aVeryBigSum(ar):
#     # Write your code here
#      sum =0
#      for i in range(len(ar)):
#         sum=sum+ar[i]
#      return sum

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = aVeryBigSum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# def diagonalDifference(arr):
#     # Write your code here
#     sum1=0
#     sum2=0
    
#     for i in range(len(arr)):
#         sum1=sum1+arr[i][i]
#         sum2=sum2+arr[i][n-i-1]
#     res=sum1-sum2
#     return abs(res)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#  # Write your code here
#    # Write your code here
#     n=len(arr)
#     pos=0
#     neg=0
#     zero=0
#     for i in range(len(arr)):
#         if arr[i]>0:
#             pos=pos+1
#         elif arr[i]<0:
#             neg=neg+1
#         else:
#             zero=zero+1
#     pos =pos/n
#     neg =neg/n
#     zero =zero/n
   
#     print("{:.6f}".format(pos))
#     print("{:.6f}".format(neg))
#     print("{:.6f}".format(zero))
#     return pos,neg,zero























