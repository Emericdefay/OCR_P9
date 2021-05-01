from django import forms

from .models import UserFollows


class FollowSomeone(forms.Form):
    user = forms.CharField(label="", widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur"}))

    def __init__(self, *args, **kwargs):
        """[summary]
        """
        super(FollowSomeone, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['style'] = "width:89%; height: 100%;"