# 함수
def hello():
    print("함수")

hello()

print("###########################")

## 기본 매개변수
def dfVariableFunc(value,n):
    for i in range(n):
        print(value)

dfVariableFunc("안녕하세요",10)

print("###########################")

## 가변 매개변수
def variableFunc(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

variableFunc(10,"안녕","하신","가요?")

print("###########################")

## 매개변수(디폴트 값)
def valueDfFunc(value,n=2):
    for i in range(n):
        print(value)

valueDfFunc("안녕")

print("###########################")

valueDfFunc("안녕",5)

print("###########################")

valueDfFunc(value="안녕",n=10)

print("###########################")
## 함수 리턴
def sum_all(*values):
    output = 0
    for i in values:
        output+=i
    
    return output

print(sum_all(1,2,3,4,5,6,7,8,9,10))

print("###########################")

## 리스트 최대값 
def custom_max(input_list):
    output = input_list[0]
    for element in input_list:
        if output < element:
            output=element

    return output

print(custom_max([100,22,55,33,88,500,200]))