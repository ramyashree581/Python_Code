class MyClass:
    def method(self):
        print 'instance method called', self

    @classmethod
    def classmethod(cls):
        print 'class method called', cls

    @staticmethod
    def staticmethod():
        print 'static method called'

obj = MyClass()    
obj.classmethod()
obj.method()
obj.staticmethod()
