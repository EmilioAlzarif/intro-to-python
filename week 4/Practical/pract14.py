list1 = ['a', 'abc', 'xyz', 's', 'aba', '1221']

length_count = [x for x in list1 if len(x)>=2]
same_chars = [ x for x in length_count if x[0]==x[-1]]
print(length_count)
print(same_chars)
print(len(same_chars))