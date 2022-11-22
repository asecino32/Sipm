from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas


class NewRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password1','password2']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ElegirInlineformset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineformset, self).clean()

        repuesta_correcta = 0
        for formulario in self.forms:
            if not formulario.is_valid():
                return
            
            if formulario.cleaned_data and  formulario.cleaned_data.get('correcta') is True:
                repuesta_correcta +=1
            
class ElegirInlineformset_mat021_iv1(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineformset1, self).clean()

        repuesta_correct1 = 0
        for formulario1 in self.forms:
            if not formulario1.is_valid():
                return
            
            if formulario1.cleaned_data and  formulario1.cleaned_data.get('correcta1') is True:
                repuesta_correcta1 +=1