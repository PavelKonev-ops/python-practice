n=int(input('число напиши'))
big=0
smol=0
while n>0:
    v=n%10
    if v>=5:
        big=big+1
    else:
        smol=smol+1
    n=n//10
print('big=' , big ,  'and smoll=' , smol)
    

