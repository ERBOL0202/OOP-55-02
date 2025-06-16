class BankAccount:
    def __init__(self, user_name, balance, pin_code):
        self.user_name = user_name
        #protected
        self._balance = balance
        #private
        self.__pin_code = pin_code