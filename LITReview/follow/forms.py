from django import forms


class FollowSomeone(forms.Form):
    """Form to follow an user.

    Args:
        forms ([module]): Form's fields collection.
    """
    user = forms.CharField(label="", widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur"}))

    def __init__(self, *args, **kwargs):
        """Edit the style of the user's textarea.
        """
        super(FollowSomeone, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['style'] = "width:89%; height: 100%;"
