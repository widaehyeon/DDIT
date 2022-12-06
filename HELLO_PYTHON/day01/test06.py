# 가위/바위/보를 넣으세요 가위
# 나: 가위
# 컴: 가위
# 결과: 비김
import random

mine = input('가위/바위/보를 넣으세요')
rnd = random.random()
com = ''
result = ''

if rnd >0.66 :
    com = "가위"
elif rnd > 0.33 :
    com = "바위"
else :
    com = "보"
    
if mine == "가위" and com == "보" or mine == "바위" and com == "가위" or mine == "보" and com == "바위" :
    result = "이김"
elif mine == "가위" and com == "가위" or mine == "바위" and com == "바위" or mine == "보" and com == "보" :
    result = "비김"
else :
    result = "짐"
    
print("나: {}".format(mine))
print("컴: {}".format(com))
print("결과: {}".format(result))