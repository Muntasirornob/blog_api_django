from django.contrib.auth import get_user_model, password_validation
def create_user_account(username, email, password, first_name="",
                        last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        username=username,email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)
    return user