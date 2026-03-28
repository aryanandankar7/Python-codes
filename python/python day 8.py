# class Student:
#     def showA(self, a, b):  # instance function
#         print("I am in showA")

#     def showB(a):  # static function
#         print("I am in showB")


# if __name__ == '__main__':
#     obj = Student()
#     obj.showA(11, 22)
#     Student.showB(22)

#Two sum
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if target==nums[i]+nums[j]:
#                    return[i,j]


#Fizz Buzz
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         ans=[]
#         for i in range (1,n+1):
#             if i%3==0 and i%5==0:
#                 ans.append("FizzBuzz")
#             elif i%3==0:
#                 ans.append("Fizz")
#             elif i%5==0:
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(i))
#         return ans

# running-sum-of-1d-array
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         ans=[]
#         sum=0
#         for i in range(1,len(nums)):
#             nums[i] = nums[i] + nums[i-1]
#         return nums
    











