#importing modules
import random
#python practicing

#This is a string type variable
x = "This is a variable"
#this variable is a frozenset
y = frozenset({"apple", "banana", "cherry"})

#prinitng my variables
print(x,y)

#this is bytes
y = b'Hello'
#byterarray
x = bytearray(5)
#memoryview
x = memoryview(bytes(5))

dit = {"name":"John", "age":45}

#finding the type of y
print(type(y))

print(random.randrange(1,))

a = "my name is banana"

#strip only removes whitespaces from beginning or end

print("heh", len(a), a.strip(), "tapasya",a.lower(), a.upper())

#replacing a part of a string

b = a.replace("b","p")
print(b)

c = a.split(" ")

print(c)

#using format

#this is a list
a = ["me", "2"]

#this is a tuple

a = ("me", "2")

#this is a set

a = {"me", "2"}

a.add("item")
a.update(["no","yes"])

print(a)

a = {"name":"taps","age":20}

#dict constructor:

a = "my name"


class Solution:
    def runningSum(self, nums):
        sum = []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            sum.append(count)

        return sum

a = Solution()

a.runningSum([1,2,3,4])