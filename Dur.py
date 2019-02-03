def maxd(arr,key,maximum):
    for i in arr:
        #print(i)
        count=0
        dup=i
        #print(dup)
        while i>0:
            dig=(dup%10)
            #print(dig)
            if(dig==key):
                count+=1
            i=i/10
        #print(count)
        if count>maximum:
            maximum=count
            num=dup
    return num
    
arr=[37,823,122,2322,6017]
a=maxd(arr,2,0)
print(a);
