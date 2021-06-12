class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def authenticate_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in is True:
            function(args[0])
        else:
            print(f"{args[0].name}, you must be logged in to post a new comment!")
    return wrapper_function

@authenticate_decorator
def create_post(user):
    print(f"this is {user.name} new post.")

new_user = User("Indiko")
create_post(new_user)