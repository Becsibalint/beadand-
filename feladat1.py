#first 100 fibonacci number
#0,1,1,2,3,5,8,13,21...
a0=0
a1=1
a2=1

list=[1,1]

for i in range(2,101):
    list.append(list[i-2]+list[i-1])


print(list)


#be kell irniegy fv-be