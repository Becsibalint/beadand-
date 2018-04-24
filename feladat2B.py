#keretezett szöveg

list=['Hello','World','in','a','frame']

def lineframe(list):
    max=0
    for i in list:
        if len(i)>max:
            max=len(i)
    for k in range(max+4):
        print('*',end='')
    print()

    for j in range(len(list)):
        print('* '+list[j]+' *')

    for k in range(max+4):
        print('*',end='')



lineframe(list)