class Counter:

    counter = 0

    def __init__(self,x):
        self.x = x
        Counter.counter +=1
    @classmethod
    def class_method(cls,x):

        cls(x)
        print('Value of counter is: {}'.format(cls.counter))
        print('Here I am calling cls')
        return None

Counter(1)
Counter(2)
Counter.class_method(3)
Counter.class_method(4)
Counter.class_method(3)
Counter.class_method(3)
