from django import forms


class CreateTicket(forms.Form):
    """[summary]

    Args:
        forms ([type]): [description]
    """
    title = forms.CharField(min_length=2)
    description = forms.CharField(widget=forms.Textarea)
    # image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        """[summary]
        """
        super(CreateTicket, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = "width:100%; height: 100%;"
        # self.fields['description'].widget.attrs['rows'] = 10
        self.fields['title'].widget.attrs['style'] = "width:100%; height: 100%;"
        # self.fields['title'].widget.attrs['rows'] = 1
