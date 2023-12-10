def fibo(n):
    ls=[1,1]
    a=0
    for i in range(int(n)):
        a=ls[i]+ls[i+1]
        ls.append(a)
    return ls

def zhishu(n):
    p=True
    for i in range(2,n):
        if n%i==0:
            p=False
            break
    return p

a=int(input('请输入范围：'))
for i in range(2,int(fibo(a)[a-1])):
    if i in fibo(a) and zhishu(i)==True:
        print(i)
