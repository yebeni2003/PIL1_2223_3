from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Emploi,Salle, Matiere, Professeur, Filiere, Semestre
User=get_user_model()
"""
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'password1',
            'password2',
        ]
class CourseForm:
    semaine = forms.CharField()

    class Meta:
        model = Course
        fields = ['semaine', 'day', 'start_time', 'end_time', 'subject', 'classroom', 'teacher', 'groupe', 'masse_horraire', 'classe']


from django import forms
from .models import Course, Filiere, Matiere

class CourseForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semaine'] = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}))
        self.fields['semaine'].label = 'Date du premier jour de la semaine'
        self.fields['subject'] = forms.ModelChoiceField(queryset=Matiere.objects.all())
        self.fields['groupe'] = forms.ChoiceField(choices=[(f.nom_fil, f.nom_fil) for f in Filiere.objects.all()])
        self.fields['classe'] = forms.ChoiceField(choices=[(m.classe, m.classe) for m in Matiere.objects.all()])

    class Meta:
        model = Course
        fields = ['semaine', 'classe', 'day', 'start_time', 'end_time', 'subject', 'classroom', 'teacher', 'groupe', 'masse_horraire']

"""
