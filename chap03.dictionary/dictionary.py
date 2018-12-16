## array 일반적인 언어에서 사용하는 배열 
arr = [1,2,3,4,5,6,7,8,9,10]
#arr = [] # 빈 배열을 만들 때 []사용
#arr = [1,2,3,4] #원소가 있는 배열을 만들 때 []사용
#arr[3] #배열의 3번째 원소에 접근할 때 []사용

for value in arr:
    print(value)


print("###############################",end='\n\n')
## tuple 은 자바로 치면 final? 흠... 파이썬 만에 독특한 자료형 변경 불가능 하고 
mytuple = () #빈 튜플 생성할 때 ()사용
mytuple = (1,2,3,4) # 원소가 있는 튜플을 만들 때 ()사용

mytuple[3] # 튜플의 원소에 접근할 때 []사용

val = (10,)

print(val[0])

print("###############################",end='\n\n')

## dictionary key : value에 조합 자바와 비슷한 기능으론 map 

mydictionary = {} #빈 딕셔너리 생성 시 {}사용
mydictionary = {"mouse":3, "penguin":5}

mydictionary["mouse"] # key("mouse")에 대응하는 value(3)에 접근할 때 사용
mydictionary["cat"] = 1 # key("cat")에 대한 value(1) 생성

print(mydictionary["mouse"])
print(mydictionary.get("mmm") is None) ## python은 null 대신 None 기억해두자 ㅎㅎ