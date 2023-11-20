#DanendraF #11/20/2023

#break
buah = ["Apple","orange","Avocado", "Grape"]
for x in buah:
    print(x)
    if x == "Grape":
        break
    
#break2
buah = ["Apple","orange","Avocado", "Grape"]
for x in buah:
    if x == "Avocado":
        break
    print(x)
    
#continue
buah = ["Apple","orange","Avocado", "Grape"]
for x in buah:
    if x == "pisang":
        continue
    print(x)

#continue2
for val in "danendra" :
    if val == "n" :
        continue
    print(val)
print("Stop")
