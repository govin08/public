# 표값
표값 = 48000 # 결제자 : 종원

# 점심
닭도리탕 = 32000 # 결제자 : 선중 - 닭도리탕소짜, 음료, 공기밥

# 투썸
아메리카노 = 5000
콤부차 = 7600 # = 3800 x 2
투썸 = 아메리카노 + 콤부차 # 결제자 : 선중

# 푸드트럭
쉬림프킹 = 7000 # 결제자 : 선중

# 편의점
편의점1 = 10200 # 생수, 파워에이드, 과자 등
편의점2 = 4500 # 홈런볼
편의점3 = 8200 # 맥주 두 캔
편의점 = 편의점1 + 편의점2 + 편의점3 # 결제자 : 선중

# 결제액 정리
종원결제 = 표값
선중결제 = 닭도리탕 + 투썸 + 쉬림프킹 + 편의점
print(f'종원결제 : {종원결제}')
print(f'선중결제 : {선중결제}')
print(f'결제총합 : {종원결제 + 선중결제}')
print()

# 지출액 정리
종원지출 = 표값 // 2 + 닭도리탕 // 2 + 아메리카노 + 쉬림프킹 // 2 + 편의점 // 2
선중지출 = 표값 // 2 + 닭도리탕 // 2 + 콤부차 + 쉬림프킹 // 2 + 편의점 // 2
print(f'종원지출 : {종원지출}')
print(f'선중지출 : {선중지출}')
print(f'지출총합 : {종원지출 + 선중지출}')
print()

# 결론
if 종원지출 > 종원결제:
    print(f'종원은 선중에게 {종원지출 - 종원결제}원을 송금한다.')
elif 선중지출 > 선중결제:
    print(f'선중은 종원에게 {선중지출 - 선중결제}원을 송금한다.')