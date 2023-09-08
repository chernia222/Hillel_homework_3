# import requests
# test_dict = {
#   "name": "Ilonnovich",
#   "lastName": "Jonhson",
#   "email": "qwerty99@test.com",
#   "password": "Qwerty12345",
#   "repeatPassword": "Qwerty12345"
# }
#
# get_current_user = requests.get("https://qauto2.forstudy.space/api/users/current")
# post_new_user = requests.post(url="https://qauto2.forstudy.space/api/auth/signup", json=test_dict)
# print(get_current_user.text)
# print(post_new_user .text)

import requests


class UserSignUpModel:

    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

user_to_sign_up = UserSignUpModel("Vova", "John", "qwertyyyy@test.com", "Qwerty12345", "Qwerty12345")

session = requests.session()
get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_to_sign_up.__dict__)
get_current_user_after = session.get("https://qauto2.forstudy.space/api/users/current")
print(get_current_user.text)
print(post_new_user.text)
print(get_current_user_after.text)
