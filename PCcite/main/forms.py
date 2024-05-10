from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Buyer
        fields = UserCreationForm.Meta.fields + ("fields")