class Student:
    count=0
    def __init__(self,id,name) -> None:
        self.id=id
        self.name=name
        Student.count+=1
    def add(self,id,name): 
        self.id=id
        self.name=name
    def show(self):
        print(f'{self.id} {self.name}')
