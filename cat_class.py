class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    def info(self):
        return ("Имя: "+self.name+"; Пол: "+self.sex+"; Возраст: "+str(self.age)+" года")
