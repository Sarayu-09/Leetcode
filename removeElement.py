def removeElement(arr,value):
    c=0
    for i in arr:
        if i==value:
            arr.remove(i)
            c+=1
    for i in range(c):
        arr.append('-')
    return arr
arr=[3,2,2,7,3]
val=3
print(removeElement(arr,val))
            
