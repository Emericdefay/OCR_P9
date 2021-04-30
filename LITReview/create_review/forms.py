from django import forms

from .models import Review

class CreateReview(forms.ModelForm):
    """[summary]

    Args:
        forms ([type]): [description]
    """
    headline = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(widget=forms.RadioSelect(choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))))
    # image = forms.ImageField()

    class Meta:
        """[summary]
        """
        model = Review
        fields = ["headline", "rating", "body"]
                

    def __init__(self, *args, **kwargs):
        """[summary]
        """
        super(CreateReview, self).__init__(*args, **kwargs)
        self.fields['headline'].widget.attrs['style'] = "width:100%; height: 100%;"
        self.fields['body'].widget.attrs['style'] = "width:100%; height: 100%;"
