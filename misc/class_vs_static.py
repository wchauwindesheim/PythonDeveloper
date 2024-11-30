class Dummy:
    name = "dummy"
    @staticmethod
    def static_method():
        print("static method called")
        name = "static"

    @classmethod
    def class_method(cls):
        print("class method called")    
        cls.name = "class"
        

d = Dummy()

d.static_method()
print(d.name)
d.class_method()
print(d.name)
Dummy.static_method()
print(d.name)
Dummy.class_method()
print(d.name)