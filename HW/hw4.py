#def square_result(func):
   # def wraper(*args, **kwargs):
        #result = func(*args, **kwargs)
       # return result ** 2
    #return wraper()
#@square_result
#def add(a,b):
    #return a + b
#print(add(5,9))

def check_user(user):
    def wraper():
        if user == "admin":
            return True
        else:
            return False
    return wraper

@check_user("admin")
def delete_database():
    print("база данных удалена")

@check_user("quest")
def delete_logs():
    print("логи удалены")
