# # # # # # Palindrome Number
# # # # # # class Solution:
# # # # # #     def isPalindrome(self, x: int) -> bool:
# # # # # #         n = abs(x)
# # # # # #         rev = 0
        
# # # # # #         while n != 0:
# # # # # #             rem = n % 10
# # # # # #             n = n // 10
# # # # # #             rev = rev * 10 + rem
        
# # # # # #         if x < 0:
# # # # # #             return False
        
# # # # # #         if rev == x:
# # # # # #             return True
# # # # # #         else:
# # # # # #             return False


# # # # # Richest Customer Wealth

# # # # # class Solution:
# # # # #     def maximumWealth(self, accounts: List[List[int]]) -> int:
# # # # #         wealth = []
# # # # #         sum = 0
        
# # # # #         for i in accounts:
# # # # #             sum = 0
# # # # #             for j in range(len(i)):
# # # # #                 sum = sum + i[j]
# # # # #             wealth.append(sum)
        
# # # # #         return max(wealth)

# # # # Find Product
# # # # n=int(input())
# # # # arr=list(map(int,input().split()))
# # # # mod=10**9+7
# # # # product=1
# # # # for num in arr:
# # # #     product=(product * num)%mod
# # # # print(product)

# # # # Staircase
# # # # def staircase(n):
# # # #     for i in range(1,n+1):
# # # #         print(" "*(n-i)+"#"*i)

# # # Mini-Max Sum
# # # def miniMaxSum(arr):
# # #     total = sum(arr)
# # #     min_val = min(arr)
# # #     max_val = max(arr)
    
# # #     print(total - max_val,total - min_val)

# # Birthday Cake Candles
# # def birthdayCakeCandles(candles):
# #     max_val = max(candles)
# #     count = 0

# #     for c in candles:
# #         if c == max_val:
# #             count += 1

# #     return count


# Time Conversion
# def timeConversion(s):
#     period = s[-2:]
#     hour = int(s[:2])
    
#     if period == "AM":
#         if hour == 12: 
#             hour = 0
#     else:
#         if hour != 12:
#             hour += 12
#     return f"{hour:02d}{s[2:8]}"
