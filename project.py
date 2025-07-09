import time

menu = {'김치찌개':9000, '된장찌개':8900, '제육볶음':11000, '돈까스':12000}
yesNo = 0

print('저희 식당에 오신것을 환영합니다.')
time.sleep(0.8)
print('원하는 메뉴를 선택해주세요.')
time.sleep(0.8)
print(menu)
choose = input()
answer = 0
while answer == 0:
    if choose == '김치찌개' or choose == '된장찌개' or choose == '제육볶음' or choose == '돈까스':
        answer = 1
        print(choose + '를 선택하시겠습니까?. (예/아니오)')
        time.sleep(0.8)
        yesNo = input()
        if yesNo == '예':
            print('지불할 금액을 입력해주세요.')
            cost = input()
            while yesNo == '예' :
                if menu[choose] <= int(cost):
                    print('결제가 완료되었습니다. 거스름돈 :',int(cost) - menu[choose],'원')
                    break
                else : 
                    print('금액이 모자랍니다. 다시 입력해주세요.')
                    cost = input()
        else : 
            print('결제가 취소되었습니다.')
                
    else :
        print('존재하지 않는 메뉴입니다. 다시 선택해주세요.')
        choose = input()
        