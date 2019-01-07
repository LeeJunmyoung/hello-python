import sys
a = 10
b = 0
try: 
    print('zeroDivisionError')
    c = a/b
except Exception as err: 
    print("Unexpected error:", sys.exc_info())
    print("err:",err)
else:
    print("실행 되나요?")
finally:
    print("실행 됩니다.")

# java  의 try-catch-finally 문법과 비슷하나 else라는 try 문 이후에 실행되는 구문이 있다.
# 잘쓰이지는 않는듯?