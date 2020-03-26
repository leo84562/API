from vendingmachine.data import Drink
balance =0
drinks=[Drink('可樂',20),
Drink('雪碧',20),
Drink('茶裏王',25),
Drink('原翠',25),
Drink('純粹喝',30),
Drink('水',20)]
def deposit():

global balance
value = eval(input('儲值金額:'))
while value < 1:
print('==儲值金額需大於零==')
value = eval(input('儲值金額:'))
balance += value
print(f'儲值後餘額為{balance}元')
def buydrinks():
global balance,drinks
print('\nplease choose your product')
for i in range(0, len(drinks)):
print(f'({i + 1}).{drinks[i]["name"]}\t{drinks[i]["price"]}元')
choose = eval(input('請選擇:'))
while choose < 1 or choose > 6:
print('==請輸入1-6之間==')
choose = eval(input('請選擇:'))
buyd = drinks[choose - 1]
while balance < buyd['price']:
print('==餘額不足,需要儲值嗎?(y or n)==')
wantd=input('')
if wantd=='y':
deposit()
elif wantd=='n':
break
else:
print('==請重新輸入==')
if balance >= buyd['price']:
print(f'已購買{buyd["name"]} {buyd["price"]}元')
balance -= buyd['price']
print(f'購買後餘額為{balance}元')