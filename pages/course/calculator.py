class Calculator:
    
    def add(self, a, b):
        return int(a) + int(b)
    
    def subtract(self, a, b):
        return int(a) - int(b)
    
    def multiply(self, a, b):
        return int(a) * int(b)
    
    def divide(self, a, b):
        return int(a) / int(b)


c = Calculator()

entered_value = 0;

while(entered_value!='exit'):
    entered_value=input("enter something ")
    if(entered_value.__contains__('+')):
        values = entered_value.split('+')
        print(c.add(values[0],values[1]))
        continue
    if(entered_value.__contains__('-')):
        values = entered_value.split('-')
        print(c.subtract(values[0],values[1]))
        continue
    if(entered_value.__contains__('*')):
        values = entered_value.split('*')
        print(c.multiply(values[0],values[1]))
        continue
    if(entered_value.__contains__('/')):
        values = entered_value.split('/')
        print(c.divide(values[0],values[1]))
    else:
        print("Please enter smt like a+b")
1