# 정수 num을 매개변수로 받아 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits() 함수를 작성하세요. 단, 나눗셈을 이용하지 말고 풀어보세요.

def sumofDigit(text):
    text_sum=0
    for i in range(len(text)):
        text_sum += int(text[i])
    return text_sum


print(sumofDigit(input("숫자입력하시오")))


# stem_leaf에 데이터를 채우는 프로그램을 작성하세요. 데이터가 채워진 결과는 다음과 같습니다.

# >>> stem_leaf
# [[0, 0, 2, 4, 7, 7, 9], [1, 1, 3, 8], [0]]
# >>> stem_leaf[0]
# [0, 0, 2, 4, 7, 7, 9]
# >>> stem_leaf[1]
# [1, 1, 3, 8]
# >>> stem_leaf[2]
# [0]

total_teamScore = [[0,0,2,4,7,7,9],[1,1,3,8],[0]]

for i in range(len(total_teamScore)):
    print("{} : {}".format(i, total_teamScore[i]))