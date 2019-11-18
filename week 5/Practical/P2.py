def evensfunc(nums):
    evens= 0
    for x in nums:
        if x%2==0:
            evens += 1
    return evens
nums= list(range(50))
print(evensfunc(nums))



