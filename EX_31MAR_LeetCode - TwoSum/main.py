#Define a function that takes a list of numbers and a target sum
def two_sum(nums, target):
    #Outer loop -> iterate over each index x in the list
    for x in range(len(nums)):
        #Inner loop -> iterate over each index y that comes after x (x + 1 to avoid reusing the same element)
        for y in range(x + 1, len(nums)):
            #Check if the two elements at index x and y add up to the target
            if nums[x] + nums[y] == target:
                #If the sum is correct, return the 2 indices in a list
                return [x, y]

#Give values to nums and target
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))

nums = [3, 3]
target = 6
print(two_sum(nums, target))