from django import forms
from AutoSpa.myapp.models import User

class UserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Użytkownik o podanym adresie email już istnieje.")
        return email

    def save(self):
        pass


class ReservationForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    date = forms.DateField()
    time = forms.TimeField()

    def clean_date(self):
        date = self.cleaned_data.get('date')

        return date
