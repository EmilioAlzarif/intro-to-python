def passcheck(password):
    num=0
    nums="0123456789"
    if len(password)<10:
        return False
    for i in password:
        for j in nums:
            if i==j:
                num += 1
            else:
                num= num
    if num>=2:
        return True
    else:
        return False
password = "dasjdask32"
print(passcheck(password))


    

