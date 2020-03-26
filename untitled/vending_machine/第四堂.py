import vending_machine.vending_service as machine
flag = True

"""

"""
a=0;

while flag:
    print('\n=========================================')
    select=eval(input('1.儲值\n2.購買\n3.查詢餘額\n4.離開\請選擇:'))

    if select ==1: #儲值
        machine.deposit()
        pass
    elif select ==2: #購買
        machine.buy()
        pass
    elif select ==3: #查詢餘額
        print(f'目前餘額{balance}元')
        pass
    elif select ==4: #離開
        # print('====請輸入1.2.3.4====')
        print('bye')
        flag = False;
        break
    else: #重新輸入
        print('====請輸入1~4之間====')
        continue
# wa1=5
# wa2=6
# def add (w1,w2):
#     result=w1+w2
#     result1=w1/w2
#     return result,result1
# print(add(5,6)) #會變TUPLE
# x1,x2=add(3,7)
# print(x1)
# print(x2)#就可以解開
# print()
# print(add(wa1,wa2))
# print(add(w2=wa1,w1=wa2))