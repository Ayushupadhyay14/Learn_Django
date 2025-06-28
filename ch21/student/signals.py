from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

# Signal receiver function for successful login


def login_success(sender, request, user, **kwargs):
    print("---------------------")
    print("Login successful!")
    print(f"Sender: {sender}")
    print(f"User: {user} (username: {user.username})")
    # Note: this is a hashed password
    print(f"User password hash: {user.password}")
    print(f"Request: {request}")
    print(f"Extra kwargs: {kwargs}")


# Connect the receiver function to the user_logged_in signal
user_logged_in.connect(login_success, sender=User)
