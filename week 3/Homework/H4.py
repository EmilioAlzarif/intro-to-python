Market = {"dairy": ["yogurt", "cheese"],"fruits": ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana', 'banana']}

Market["candies"]= ['mars', 'kinder', 'twix']
print(Market)

editing = set(Market["fruits"])
Market["fruits"] = list(editing)
Market["fruits"].sort()
print(Market)