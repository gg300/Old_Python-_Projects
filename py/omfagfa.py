#lol = {}
#while True:
#    name = input("Student's name ")
#    if name=="":
#        break
#    score = int(input("Rate the student with a score beetween [0,10]: "))
#    if score < 0 or score > 10:
#        break
#    if name in lol:
#        lol[name]+=(score,)
#    else:
#        lol[name]=(score,)
#for name in sorted(lol.keys()):
#    sum=0
#    counter = 0 
#    for score in lol[name]:
#        sum+=score
#        counter+=1
#    print(name+" average score = ",sum/counter)

tup = (1,2,4,2,6,2,6,77,8,7,54,3,2,1,1,4,5,6,3)
print(tup.count(1))
print(tup.count(2))