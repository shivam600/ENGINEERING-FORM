from django import forms
from .models import student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class studentForm(forms.ModelForm):

    class Meta:
        model=student
        fields=("fullname","address","contact_no","college_name","stream")
        labels={
            "fullname": "Full name",
            "address":"ADDRESS",
            "contact_no":"CONTACT NO",
            "college_name":"COLLEGE NAME",
            "stream":"STREAM",         

        }
      
    def __init__(self,*args,**kwargs):
        super(studentForm,self).__init__(*args,**kwargs)
        self.fields['stream'].empty_label="select"
        self.fields['college_name'].empty_label="select" 
        self.fields['address'].required=False


class ExtendedUserCreationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=("username","email","first_name","last_name","password1","password2")

    # def save(self,commit=True):
    #     user=super().save(commit=False)

    #     user.email=self.cleaned_data['email']  
    #     user.first_name=self.cleaned_data['first_name']   
    #     user.last_name=self.cleaned_data['last_name']

    #     if commit:
    #         user.save()
    #     return user   
       

class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=("email","first_name","last_name")
        


         
   


        