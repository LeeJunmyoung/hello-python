list_a = [1,2,3,4,5]
list_b = reversed(list_a)
for i in list_a:
    print(i) # 1 2 3 4 5 

print("=================")

for i in list_b:
    print(i) # 5 4 3 2 1

print("=================")

for i in list_b:
    print(i) #noting

print("=================")

#### for문 index,element
print("변수 추가")
# 가장 쉬운 방법
example_list = ["요소 A", "요소 B", "요소 C"]
i=0

for item in example_list: 
    print("{} 번째 {}입니다".format(i,item) )
    i+=1

print("=================")
print("Range length 활용")
# Range length 활용

for i in range(len(example_list)):
    print("{} 번째 {}입니다".format(i,example_list[i]) )


print("=================")
print("enumerate 활용")

for index, element in enumerate(example_list):
    print("{} 번째 {}입니다".format(index,element) )


print("=================")
print("Json 형태 key , value 출력")

example_dictionary={
    "KEY1":"value A",
    "KEY2":"value B",
    "KEY3":"value C"
}

print(example_dictionary)
for key , element in example_dictionary.items():
    print("{}는 {}입니다.".format(key,element))


print("=================")
print("array 넣기")

array = []

for i in range(0,20,2):
    if i<10:
        array.append(i*i)

print(array)

array1 = [i*i for i in range(0,20,2) if i<10]
print(array1)