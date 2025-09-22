# fizzbuzz
# 1 부터 임의의 양의 정수 i에 대해
# i가 3의 배수라면, fizz
# i가 5의 배수라면, buzz
# i가 15의 배수라면, fizzbuzz
# 나머지, i

for i in range(1,15+1):
    if i % 3 == 0:
        print('fizz')
    else:
        print(i)
