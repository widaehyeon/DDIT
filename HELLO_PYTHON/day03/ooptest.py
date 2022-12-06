class animal:
    def __init__(self):
        print("생성자")
        self.age = 0
    
    def getOlder(self):
        self.age += 1
        
    def __del__(self):
        print("소멸자")
        
        
class human(animal):
    def __init__(self):
        super().__init__()
        self.language = 0
    
    def momstouch(self, stroke):
        self.language += stroke
        
if __name__ == '__main__':  
    hum = human()
    print(hum.age)
    print(hum.language)
    hum.getOlder()
    hum.momstouch(5)
    print(hum.age)
    print(hum.language)