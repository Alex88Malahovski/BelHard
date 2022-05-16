class Phone:
    def __init__(self, brand, model, issue_year,name):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.name=name

    def receive_call(self, name):
        return f'{self.name} вам звонит'
    def __str__(self):
        return f'{self.brand, self.model, self.issue_year,self.name}'
dfdf=Phone('Xiaomi','mi','2021','Doc')
print(dfdf.receive_call('mobile'))