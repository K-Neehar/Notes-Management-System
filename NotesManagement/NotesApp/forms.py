from .models import Student
from django import forms

class StForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=["name","password","email"]
		widgets={
		"name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Name",
			}),
		"password":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Password",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Email",
			}),
		}
