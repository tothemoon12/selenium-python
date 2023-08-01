class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = f'{self.first_name} {self.last_name}'
        self.initials = f'{self.first_name[0]}.{self.last_name[0]}'
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.full_name}, {self.initials}'
        
n = Name('alEx', 'TSA')
print(n)