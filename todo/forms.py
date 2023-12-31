from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create/Register a new user (Model form)
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
