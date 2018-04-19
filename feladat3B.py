#primszámok 10001

def primszamok():
    list=[]
    f=0


    while len(list)<10002:

        db=0
        for i in range(1,f+1):
            if f%i==0:
                db+=1
        if db==2:
            list.append(i)
        f+=1

    return list





print(primszamok()[10001])