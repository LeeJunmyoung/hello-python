class Student:
    def __init__(self,name,math,science,english):
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



a = Student("이준명",90,80,100)

print(str(a))