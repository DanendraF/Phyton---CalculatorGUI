#DanendraF #11/20/2023

# WHILE
n = 7
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1
    
print("hasilnya adalah", sum)

#i <= n  maka i akan mengulang sampai n
#7+6+5+4+3+2+1+0

#WHILE ELSE
counter = 0

while counter < 3:
    print("INSIDE LOOP")
    counter = counter + 1
else:
    print("EXCLUDE LOOP")
    
#BREAK
i = 0
while i < 7:
    i += 1
    if i == 4:
        break
    print (i)
    
#CONTINUE
i = 0
while i < 7:
    i += 1
    if i == 4:
        continue
    print (i)