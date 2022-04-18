import random
a=0
l1=[]
l2=[]
l3=[]
for i in range(1,6):
    odd_rndm = random.randrange(1,70,2)
    even_rndm = random.randrange(2,70,2)
    l1.append(odd_rndm)
    l2.append(even_rndm)

l3 = l1+l2
print(l1)
l1.pop(2)
l1.insert(2,l2)
print(l1)
print(sorted(l3))
