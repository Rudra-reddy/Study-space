from django.forms import ModelForm,PasswordInput
from .models import User,Room,Message,Question,Answer
class Userform(ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
class Loginform(ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'password':PasswordInput(attrs={'class':'passclass'})}
class Roomform(ModelForm):
    class Meta:
        model=Room
        fields=['name','description','topic']
class Messageform(ModelForm):
    class Meta:
        model=Message
        fields=['body']
class Questionform(ModelForm):
    class Meta:
        model=Question
        fields=['topic','question']
class Answerform(ModelForm):
    class Meta:
        model=Answer
        fields=['answer']
class Filterform(ModelForm):
    class Meta:
        model=Question
        fields=['topic']