# 첫번째 수를 넣으세요 1
# 두번째 수를 넣으세요 10
# 1에서 10까지 합은 55입니다.

a = int(input("첫번째 수를 넣으세요"))
b = int(input("두번째 수를 넣으세요"))
arr = range(a, b+1)
sum = 0

for i in arr:
    sum += i

print("{}에서 {}까지 합은 {}입니다.".format(a,b,sum))