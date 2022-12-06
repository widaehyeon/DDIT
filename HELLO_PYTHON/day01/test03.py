# 홀/짝을 넣으세요 홀
# 나: 홀
# 컴: 짝
# 결과: 졌음
import random

me = input("홀/짝을 넣으세요")
print("나: {}".format(me))
rnd = random.random()

if(rnd > 0.5):
    com = "홀"
else:
    com = "짝"

print("컴: {}".format(com))

if(me == com):
    print("결과 : 이겼음")
else :
    print("결과 : 졌음")