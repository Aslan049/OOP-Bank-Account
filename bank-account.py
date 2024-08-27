import datetime

class Customer:                                                                 # created a class for customer information.
    def __init__(self,name,surname,Id,gender,birth_date,type ="Customer") -> None:
        self.name = name
        self.surname = surname
        self.Id = Id
        self.gender = gender
        self.birth_date = birth_date
        self.type = type

    def calculate_Age(self):
        today = datetime.date.today()
        cal_Age = today.year - self.birth_date
        return cal_Age        

    def show_info(self):                                                        # that structure makes code more clean and readable.
        return f"""
        {self.type}
        Name: {self.name}
        Surname: {self.surname}
        CustomerId : {self.Id}
        Gender : {self.gender}
        Age : {self.calculate_Age()}
        """
    


class Account:                                                                  # created a class for account information.
    def __init__(self,opendate,moneytype,totalmoney,interestdays,type = "Account") -> None:
        self.opendate = opendate
        self.moneytype = moneytype
        self.totalmoney = totalmoney
        self.interestdays = interestdays
        self.type = type

    def MoneyType(self):                                                        # gives information about type of money.
        if self.moneytype == "USD":
            return f"{self.moneytype} Valid Currency"
        elif self.moneytype== "EUR":
            return f"{self.moneytype} Valid Currency"
        elif self.moneytype == "TRY":
            return f"{self.moneytype} Valid Currency"
        else:
            return f"{self.moneytype} Unknown Currency"

    def calculate_Interest(self):                                               # here is some information rate of interest.
        rate_interest_dolar = 0.01
        rate_interest_euro = 0.02
        rate_interest_tl = 0.001
        
        if self.moneytype == "USD":
            CalInterest = (self.totalmoney * (rate_interest_dolar * self.interestdays))
            return CalInterest
        elif self.moneytype == "EUR":
            CalInterest = (self.totalmoney * (rate_interest_euro * self.interestdays))
            return CalInterest
        elif self.moneytype == "TRY":
            CalInterest = (self.totalmoney * (rate_interest_tl * self.interestdays))
            return CalInterest
        else:
            return 0
    
    def sum(self):                                                              # for total money.          
        sumMoney = (self.calculate_Interest() + self.totalmoney)
        return sumMoney

    
    def info(self):                                                             # that structure makes code more clean and readable.
        return f"""
        {self.type}
        Money : {self.moneytype}
        Total : {self.totalmoney}
        Interest : {self.calculate_Interest()}
        End Of Days : {self.sum()}
        """

                                                                                    
try:                                                                            # checking if it works or not.
    customer1 = Customer("Aslan","Korkmaz",2458879,"True",2003)
    acount1 = Account(2024-8-26,"TRY",3500,32)
    print(customer1.show_info())
    print(acount1.info())
    print(acount1.MoneyType(),)

except Exception as ex:                                                         # it explains if you have bugs.
    print("pls check your informations and make them true!",ex)

