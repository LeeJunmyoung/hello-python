

class Student:
    
    __count=0

    def __init__(self,name,math,science,english):
        Student.__count += 1
        self.name=name
        self.math=math
        self.science=science
        self.english=english
    
    
    def getSum(self):
        return self.math+self.science+self.english
    
    def getAvarage(self):
        return self.getSum() / 3

    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.getSum(),self.getAvarage())

    def __eq__(self,value):
        print("eq 함수가 호출되었습니다.")
        return value == self.getAvarage()

    @classmethod
    def getCount(cls):
        print(Student.__count)
    

a = Student("이준명",90,80,100)
b = Student("이준명",90,80,98)
c = Student("이준명",90,80,99)

print(str(a))

print(a==80)

Student.getCount()
print(Student.__count)

## __num  =  private
## _num   =  protected
## num    =  public 
