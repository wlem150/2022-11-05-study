"""
1 과 자기 자신으로만 나누어떨어지는 자연수를 소수(素數, prime number)라고 합니다

소수를 구하는 방법은 다음과 같습니다.

찾고자 하는 범위의 자연수를 나열한다.
2부터 시작하여, 2의 배수를 지워나간다.
다음 소수의 배수를 모두 지운다.
다음은 파이썬 셸에서 수작업으로 10 이하의 소수를 구하는 예입니다.

>>> L = list(range(2, 11))             # 찾고자 하는 범위의 자연수를 나열
>>> L
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> L.remove(4); L.remove(6); L.remove(8); L.remove(10) # 2의 배수를 지움
>>> L.remove(9)                                         # 3의 배수를 지움
>>> L                                                   # 결과
[2, 3, 5, 7]

이와 같은 방식으로 찾고자 하는 범위(예: 30 이하)의 소수를 구하는 것이 문제입니다. 수작업으로 하지 말고 반복문을 사용하세요.

"""

import math
import time

start = time.time()

def isPrime(num):
    if num < 2 :
        return False
    if num == 2 or num == 3:
        return True
    if (num & 1) == 0 or num % 3 ==0 :
        return False
    
    sqrtN = int(math.sqrt(num)+1)
    for i in range(6,sqrtN,6):
        if num % i+1 == 0 or num % i-1 == 0 :
            return False
            
    return True

for i in range(30):
    if isPrime(i):
        print(i)
end = time.time()

print("측정시간 : {} ".format(end-start))

# -------------------------------------------
# 정답으로 올라온 답안

from math import sqrt

def prime(n):
    N = list(range(2, n + 1))

    i = 0
    while i <= sqrt(n) and len(N) > i:
        #print('\ncheck multiple of ', N[i])
        j = i
        while i <= j <= n and len(N) > j:
            #print(f'N[{j}]: {N[j]}', end='')
            if N[j] != N[i] and N[j] % N[i] == 0:
                del N[j]
                #print(' <= deleted')
                if len(N) == j:
                    break
            else:
                #print('')
                j += 1
        if len(N) == i:
            break
        else:
            i += 1

    #print(f'\nprime numbers under {n}: ', end='')
    print(N)

if __name__ == '__main__':
    prime(int(input()))