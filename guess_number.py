# حدس عدد توسط computer
import random
min = 0
max = 100
hads = random.randint(min, max)
print("hads computer: ", hads)
while True:
    javab = input("your number bigger than gusse?? 0>>>no , 1>>>yes , 2>>>equal , 3>>>exit : ")
    if javab == '3':
        print("shoma az bazy khareg shodid!")
        break
    elif javab == '2':
        print("good")
        break
        
    elif javab == '1':
       min = hads + 1
    elif javab == '0':
        max = hads - 1
    else:
        print("please select 0, 1, 2 : ")
        continue
    if min > max:
        print("eror")
        break
    hads = random.randint(min, max)
    print("hads: ", hads)
        
print("finished")