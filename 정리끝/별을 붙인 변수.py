
def func(*file):
    print(type(file))
    for i in file:
        print(i)

# a = [1,2,3,5,6], [1,2,3,5,4]
# b = 1   
# a = "Sample"
# b = ["Sample", "Sample2", "Sample3"]  
c = "Sample", "Sample2"   
# func(a)
# func(b)
func(c)


# *variable 을 할경우에 파일이 안으로 들어가며 (,) 로 감싸주며 튜플로 변환된 상태로 출력이 됨. 그래서 

# b = 1 이라는 값이 들어간다고 해도, 출력이 정상적으로 됨

# 이를 활용하면 즉각적으로 튜플로 만들어서 사용할 수 있다는 장점이 있음.

# def func2(file):
#     for i in file:
#         print(i)


# a = [1,2,3,5,6], [1,2,3,5,4]
# b = 1       
# a = "Sample", "Sample2"
# b = ["Sample", "Sample2", "Sample3"]  
# func2(a)
# func2(b)

# 변수 자체가 그냥 들어감, 그래서 for 반복문을 활용하면 

# b =1 이라는 값이 들어갈 때, in 이라는 값안에 int 값이 들어갈 수 없기 때문에, 오류가 발생함.

# Sample 이라는 문자열 변수가 들어가면 문자열 하나하나씩 출력을 해주게 된다.