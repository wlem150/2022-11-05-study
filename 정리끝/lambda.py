# # lambda 매개변수 : 표현식

# a = (lambda x,y: x + y)(10, 20)
# print(a)

# # lambda map(함수, 리스트) : 뒤에 오는 리스트 값을 하나씩 x 값에 넣어서 값을 도출한다.
# print(
#     list(map(lambda x: x ** 2, range(5))) 
# )

# # lambda reduce(함수, 시퀸스)

# from functools import reduce

# c = reduce(lambda x,y : x+y, [0,1,2,3,4,5,6])
# c = reduce(lambda x, y : y + x , 'abcde') # x 와 y 의 순서가 달라지면 출력값이 달라짐

# # lambda filter(함수, 리스트)

# f = list(filter(lambda x: x>5 , [1,2,3,4,5,6,7,8,9]))
# print(f)
# f2 = list(filter(lambda x : x=="a", ["a","b","c"]))
# print(f2)


def read(text):
    ridename, limit = map(str.strip, text.split(':'))
    cmmin = cmmax = None
    if '~' in limit:
        cmmin, cmmax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
        
    elif "이상" in limit:
        cmmin = int(limit.split("cm")[0])

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    while True :
        ridename, cmmin, cmmax = read(input())
        print("이름:", ridename)
        print("하한:", cmmin)
        print("상한:", cmmax)

# 기존에 사용하지 않던 형식이라 익숙하지가 않았다.

"""
일단 함수가 실행되는 순서를 기록해 놓자.

이 파일을 실행하면 __name__ == __main__ 이기 때문에, while True 문이 실행이 된다.

그리고 read(input()) 가 실행이 되어서 사용자가 입력하는 값을 받아 그 값을 read() 함수의 매개변수로 들어간다. 

함수가 실행될 때, 이 위에 있는 값을 기준으로 ridename 과 limit 에 변수가 저장이 된다.

Ex)
롤로코스터 : 160

롤로코스터 : 160cm 이상

롤로코스터 : 160 ~ 180

롤로코스터 : _

Ex)

//// ridename, limit = map(str.strip, text.split(':'))

파이썬에서 map은 (함수, 리스트 or 튜플 ) 이 오는 형태이다.

그 값을 받기 위해 text 라는 매개변수 안에 들어가는 값을 정확하게 받기 위해서 사용자 input 값에 뛰어쓰기를 포함한 2개의 문자가 (:) 사이에 놓고 출력되어야 한다.

굉장히 비효율적이고 하드코딩이지만, 익숙하지 않은 문법을 사용한다는 생각으로 적용해보자

특히 str.strip 을 함수로 넣어서 사용할 수 있다는 점이 새로웠다.

또한 text.split(':') 를 map(함수, 리스트or튜플) 이라는 함수안에 새로운 값을 넣을 수 있도록 생각의 폭을 넓혀줬다.

여튼 이 메소드안에 들어가게 되면 
limit: 160~180
ridename: 롤로코스터

라는 2개의 값으로 쪼개 지게 된다.
---------------------------------------------------------

Ex)
//// if '~' in limit:
            cmmin, cmmax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))

limit: 160~180
ridename: 롤로코스터

위에서 얻은 값에 따라서 limit 의 값이 limit.split('~') 을 통해서 ('~') 값은 사리지고 '160', '180' 의 값만 남게 된다.

그리고 그렇게 얻은 2개의 값은 int(x.replace('cm', '')) 값 안에 들어가게 되지만 얻은 값이 없으므로, 바로 'x' 값 안에 들어가게 되고,

cmmin = 160
cmmax = 180 

이라는 값을 얻게 된다.

만약에 input 값 안에 // 롤로코스터 : 160cm~180cm 로 한다면, limit.split('~') 에 따라서 160cm, 180cm 값이 남게 되고,  

이 값이 int(x.replace('cm', '')) 에 들어가서 다시 '160', '180' 이라는 값만 남게 되며 결과는 같아진다.

----------------------------------------------------------
"""

def Sample(text):
   
    text_1 = map(int , list(str(text)))
    return sum(text_1)

if __name__ == "__main__" :
    print(Sample(47253))
    
# map 을 어떻게 활용해야 할지 전혀 감지 잡히지 않는다. 이 문구 자체를 이해를 했지만, 내가 직접 이것을 활용하는 것은 또 다른 문제인것 같다.