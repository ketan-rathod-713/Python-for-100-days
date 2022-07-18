def my_function():
    pass


# It will not show any error using pass keyword , also can be used in classes

# Pascal case , Camel case , Snake case --> Way of writing names of variables , classes and all

class User:
    pass


user1 = User()
user1.name = "JUST"
user1.value = "123"

print(user1.name)  # Now we can access that variable that we defined


# If we have lots of attributes then there may be too much conflicts so ,

# Constructor , initializing an object
# add init function inside class , it is a special function

class User2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0  # default value
        self.following = 0
        print("new user created")  # each time printed as user created

    def follow(self, user):  # method
        user.followers += 1
        self.following += 1


user2 = User2("ketan", 14)
print(f"{user2.name} {user2.age}")
user3 = User2("other",23)
user3.follow(user2)
print(user2.followers)

