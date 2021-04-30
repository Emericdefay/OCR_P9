from django import forms


class FollowSomeone(forms.Form):
    user = forms.CharField()

