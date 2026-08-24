text = 'HelloWorld'

print(text[3:6]) 

#list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)
print(nums[2]) 

#mixed data type list
mixed_list = [1, 'Hello', 3.14, True]

#mixing 2 lists
mix = [nums, mixed_list]
print(mix)

print("length of mix:", len(mix))

print(mix[0][4])  # Accessing the 5th element of the first list (nums)
print(mix[1][3])  # Accessing the 4th element of the second list (mixed_list)


#comining the values
mixed = nums + mixed_list
print(mixed)  # Combining the two lists into one

nums.append(56)
print(nums)

nums.remove(3)
print(nums)