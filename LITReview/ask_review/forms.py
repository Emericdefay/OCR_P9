from django import forms

from .models import Ticket


class CreateTicket(forms.ModelForm):
    """[summary]

    Args:
        forms ([type]): [description]
    """
    title = forms.CharField(min_length=2)
    description = forms.CharField(widget=forms.Textarea)
    # image = forms.ImageField()
    class Meta:
                model = Ticket
                fields = ["title", "description"]
                
    def __init__(self, *args, **kwargs):
        """[summary]
        """
        super(CreateTicket, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = "width:100%; height: 100%;"
        # self.fields['description'].widget.attrs['rows'] = 10
        self.fields['title'].widget.attrs['style'] = "width:100%; height: 100%;"
        # self.fields['title'].widget.attrs['rows'] = 1

        

""" 
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField()
"""