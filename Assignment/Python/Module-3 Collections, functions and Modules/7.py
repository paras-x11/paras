# 7. Write a Python program to remove duplicates from a list.

nums = [3, 5, 7, 3, 9, 1, 5, 6, 2, 9, 8]
i=0

while i < len(nums):
    if nums[i] in nums[:i]:
        del nums[i]
    else:
        i += 1
print(nums)


new_nums = set(nums)
print(new_nums)
print(type(new_nums))


new_nums = list(set(nums))
print(new_nums)
print(type(new_nums))



