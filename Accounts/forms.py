from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# User = get_user_model()



# Create your forms here.

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username",  "password1", "password2", 'email')
#         # fields = '__all__'

#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.is_staff = True
#         # user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user