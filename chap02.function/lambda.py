list_a = [1,2,3,4,5,6,7,8,9]

#람다 선언식 labmda 변수 : 수해할 리턴

funcDoubble = lambda value : value * value

list_b = map(lambda x : x * x,list_a)
list_c = filter(lambda x : x < 5,list_a)
list_d = map(funcDoubble,list_a)

print(list(list_b))
print(list(list_c))
print(list(list_d))

print("#####################")

dictionary = { 1:"일"
             , 2:"이"
             , 3:"삼"
             , 4:"사"
             , 5:"오"
            }
print(dictionary)
dic_a = map(lambda value : value*value  , dictionary)
dic_b = filter(lambda value : value>2,dictionary)
print(list(dic_a)) ## dictionary 가 array로 바뀌는듯하다
print(list(dic_b)) ## dictionary 가 array로 바뀌는듯하다

