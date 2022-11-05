print(str) # str은 내장 힘수가 아니라 파이썬 내장 클래스이며, 객체를 만들고 그 객체의 정보를 알고 싶을 때, print(객체이름)를 사용하는데, 이는 object 클래스의 __str__ 메서드가 호출되어 반환된 문자열 정보이다.

#이 __str__ 의 문자열 반환 기능을 오버라이딩하여 쓸 수 있다.

# __init__ 은 컨스트럭터라고 불리는 초기화를 위한 함수이다.
# 인스턴스를 만들 때 반드시 처음에 만들어 줘야 한다.
class Sample(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return "객체 혼자 프린트하면 __str__ 값을 반환해 준다."
        

class IDinfo:
    def __init__(self):
        pass
    
    def __str__(self):
        return str(id(self)) # id함수는 주소값을 반환해 준다.


def main():
    a = Sample("JW", 28)
    b = IDinfo()
    print(a)
    print(b)
    print(type(b))

main()

"""
__str__의 목적은 문자열화를 하여 서로 다른 객체 간의 정보를 전달하는 데 사용하는 것이고

__repr__은 인간이 이해할 수 있는 표현으로 나타내기 위한 것입니다.

즉, 해당 클래스에 대해 사용자에게 정보를 전달하고 싶은 경우 __repr__을 사용하고

해당 클래스의 특정 데이터를 다른 객체들 간에 전달하고 싶은 경우 __str__을 사용하면 됩니다.

그래서 __str__이 우선순위가 더 높은 것이 아닐까 라는 생각이 됩니다.
"""

# class Color():
#     def __init__(self,name):
#         self.name = name

# red = Color('red')
# yellow = Color('yellow')
# green = Color('green')

# arr = [red, yellow, green]

# for ar in arr :
#     print(ar)


# Color 함수를 정의하고 객체를 3개 만들었다. 이후 출력을 하였을 때, Color 함수의 메모리 주소가 나오게 된다. 함수안에 __str__, __repr__ 을 정의하지 않았기 때문이다.


# --------------------------------------------------------

class Color():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'__str__: {self.name=}'
    def __repr__(self):
        return f'__repr__: {self.name=}'

red = Color('red')
yellow = Color('yellow')
green = Color('green')

arr = [red, yellow, green]
print(arr)
for ar in arr :
    print(ar)

# __str__: self.name='red'
# __str__: self.name='yellow'
# __str__: self.name='green'

# 만약 __str__ 가 없다면,

# __repr__: self.name='red'
# __repr__: self.name='yellow'
# __repr__: self.name='green'

#  출력됬을 것이다.

# 각 객체를 담은 리스트 arr 을 출력을 하면 

# [__repr__: self.name='red', __repr__: self.name='yellow', __repr__: self.name='green']

# 가 출력된다. 만약 color 클래스 안에 __repr__ 함수를 정의하지 않았다면 각 값들의 메모리 주소를 반환한다.