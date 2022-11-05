# 주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성하세요. 단, 문자열 입력은 모두 소문자로 이뤄지며 공백을 포함하지 않는다고 가정합니다.

def palindrome(text):
    if text[::-1] == text[0:]:
        return True
    else :
        return False

print(palindrome('anna'))

# # 대문자와 소문자가 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.

def palindrome(Sample):
    text = Sample.lower()
    if text[::-1] == text[0:]:
        return True
    else :
        return False

print(palindrome('Anna'))

# 공백이 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.

def palindrome(Sample):
    Sample = Sample.split()
    Sample = "".join(Sample)
    text = Sample.lower()
    if text[::-1] == text[0:]:
        return True
    else :
        return False

print(palindrome('My Gym'))

#  ----------------------------------------------------------
# 정답으로 올라온 코드

# 내가 작성한 코드와 비교했을 시

# 내가 작성한 코드는 매번 내가 입력을 해줘야 한다는 점이 문제인 것 같다. 한번 출력에 매번 print 문을 반복적으로 사용하거나 for, while 문을 다시 사용해야 한다는 단점이 있어 보인다.

# 밑에 정답으로 올라온 코드는 리스트안에 있는 값들을 추가하기만 하면 된다는 점에서 보다 간결하게 코드를 작성할 수 있어 보인다. 그리고 return 문을 불린 형식으로 넣으니 자연스럽게 그냥 True, False 값으로 들어가는 것을 확인할 수 있다.

def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    return s[:] == s[::-1]

if __name__ == '__main__':
    for x in ['anna', 'banana', 'Anna', 'My gym']:
        if palindrome(x):
            print(f"'{x}' is a panlindrome")
        else:
            print(f"'{x}' is not a palindrome")