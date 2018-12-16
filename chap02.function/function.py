# 함수
def hello():
    print("함수")

hello()

## 기본 매개변수
def dfVariableFunc(value,n):
    for i in range(n):
        print(value)

dfVariableFunc("안녕하세요",10)

## 가변 매개변수
def variableFunc(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

variableFunc(10,"안녕","하신","가요?")