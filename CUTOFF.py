# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    #print(arr)
    print(arr[x-1]-1)
        