# converted the given list to separeted list by comma
#then used index() func to learn given item's index in that list

box=input()
box2=box.split(",")
item=input()
i=box2.index(item)
i+=1
print(i*5)
