import math,random
# print(math.pi)
# average=3.55555
# average=round(average)
# print(average)
# a=55
# if(a>10):
#     print(10)
# elif(9>a>5):
#     print(5)
# else:
#     print(0)
# print('word','\nww',end='')
# print('word','\nww')
# x=42
# value=f'value of x is {x}'
# print(value)
# mathScores=[60,70,10,20,81,63,4]
# print(mathScores[0])
# firstItem=f'first item in mathScore is {mathScores[0]}'
# print(firstItem)
#
# for i in range(0,10):
#     # 0~9
#     print(i)
# for i in range(10):
#     print(i)
# for i in range(len(mathScores)):
#     print(i,mathScores[i])
# for i in mathScores:
#     print(i)
# kk=(12,55,6,44,8,5)
# for i in kk:
#     print(i)
# fa={"a":"A",'b':'B','c':'C'}
# for me in fa.items():
#     print(me)
# for key,value in fa.items():
#     print(f'my {key} is {value}')
# aa=[60,70,10,20,81,63,4]
# for i in aa:
#     print(i**0.5*10)
# [print(i)for i in range(10)]
# [print(math.sqrt(i)) for i in aa]
#
# i=random.randint(1,50)
# for i in range(10):
#     for k in range(10):
#         print(f'{i}*{k}={i*k}\t',end='   ')
#     print()
#     o=0;
# while(o<100):
#     print("w")
#     o+=1;
# else:
#     print("G")
# c=1;
# p=95;
# eval()可以把字串拿來算
# while(c<=95):
#     if(c%2==1):
#         print(c)
#     c+=1;
# y=input("給我打:")
# print(y)
r=int(input("R:"))
c=int(input("C:"))
b=[]
t=0
for q in range(0,r):
    a=[]
    for w in range(0,c):
        i=random.randint(1,100)
        t+=i;
        a.append(i)
    b.append(a)
[print (i) for i in b]
r=int(input("R:"))
c=int(input("C:"))
d=[]
t=0
for q in range(0,r):
    a=[]
    for w in range(0,c):
        i=random.randint(1,100)
        t+=i;
        a.append(i)
    d.append(a)
[print (i) for i in d]
print()
e=[]
for q in range(0,r):
    a=[]
    for w in range(0,c):
        i=b[q][w]+d[q][w]
        a.append(i)
    e.append(a)
[print(i) for i in e]
# print(t)
# sr=int(input("sr:"))
# print(sum(b[sr-1]))
# sc=int(input("sc:"))
# l=0
# for m in range(0,r):
#     l+=b[m][sc-1]
# print(l)