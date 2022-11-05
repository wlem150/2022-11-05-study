# 십진수를 입력받아 그 숫자에 해당하는 이진수의 각 자리를 리스트로 출력하는 프로그램을 작성하세요. (순서에 유의)


def Sample(num):
    binary_list = []
    num = bin(num)[2:]
    for i in num :
        binary_list.append(int(i))
    return binary_list
if __name__ == "__main__":
    print(Sample(13))

# --------------------------------------------------------
# 정답으로 올라온 정보

d = int(13)
m = d
b = []

while True:
    d, m = divmod(d, 2)
    b.insert(0, m)
    if d == 0:
        break

print(b)

