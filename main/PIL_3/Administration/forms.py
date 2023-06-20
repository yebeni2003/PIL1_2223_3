from .models import Administrator
#formulaire d'inscription
class signup(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['name','prenom','email','phone','age','password']
        widgets = {
            'name': forms.TextInput(attrs={'class','form-control'})
            'prenom': forms.TextInput(attrs={'class','form-control'})
            'email' : forms.EmailInput(attrs={'class','form-control'})
            'password' : forms.TextInput(attrs={'class','form-control'})
        }
