# cook your dish here
for t in range(int(input())):
    x,y=map(int,input().split())
    if(y<=x):
        print(y)
    else:
        print((x)+((y-x)*2))