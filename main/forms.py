from django import forms
from accounts.models import User

class FriendRequestForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'biography', 'profile_image']
