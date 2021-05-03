from django import forms

from .models import Ticket


class CreateTicket(forms.ModelForm):
    """Form to create a ticket

    Args:
        forms ([module]): Form's fields collection.
    """
    title = forms.CharField(min_length=2)
    description = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(
                            label="Télécharger une image",
                            required=False,
                            widget=forms.FileInput)

    class Meta:
        """Allow edition of fields mentionned.
        """
        model = Ticket
        fields = ["title", "description", "image"]

    def __init__(self, *args, **kwargs):
        """Allow edition of fields mentionned.
        """
        super(CreateTicket, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs[
                                'style'] = "width:100%; height: 100%;"
        self.fields['title'].widget.attrs[
                                'style'] = "width:100%; height: 100%;"
        # self.fields['image'].widget.attrs[
        #           'style'] = "width:100%; height: 100%;"
