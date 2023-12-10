def huiwen(n):
    p=False
    if str(n)==str(n)[::-1]:
        p=True
    return p


def zhishu(n):
    p=True
    for i in range(2,n):
        if n%i==0:
            p=False
            break
    return p


a=input("请输入最大值：")
for j in range(2,int(a)):
    if huiwen(j)==True and zhishu(j)==True:
        print(j)