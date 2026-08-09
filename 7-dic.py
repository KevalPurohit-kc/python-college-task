dic = {
   
    'name':"raj",
     'age':20
        }

print("dictionary items:",dic.items())
print("dictionary keys:",dic.keys())
print("dictionary values:",dic.values())
dic['age']=50
dic['name']='jenish'
last_item=dic.pop('age')



#only dictionary inside date clear empty dic show 
last_item=dic.clear()
print(dic)
#delete dictionary 
del dic
dic2 = {'name':'keval'}
print(type(dic2))
