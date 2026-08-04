li = ["BMW","Audi","Rolls-Royce","TATA",39,50]
el = [540,450,751,456]
print("====MAX and MIN value print====")
print(max(el))
print(min(el))
print("====length====")
print(len(li))
print("====2 list marge====")
print(li + el)
print("===2 time list print=====")
print(li*2)
print("====find number T/F====")
print(540 in el)
print("====only one item print====")

#only one item print
print(li[2])
print("====starting to ending istem print====")
#starting to ending istem print

print(li[2:6])
print("====Comprehension====")
#Comprehension
li2 = []
for i in li:
    li2.append(i)
print(li2)
