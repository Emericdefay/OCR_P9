from django import forms

from .models import Review


class CreateReview(forms.ModelForm):
    """Form to create a review

    Args:
        forms ([module]): Form's fields collection.
    """
    headline = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(widget=forms.RadioSelect(choices=(
                                                                (1, "1"),
                                                                (2, "2"),
                                                                (3, "3"),
                                                                (4, "4"),
                                                                (5, "5"))))

    class Meta:
        """Allow edition of fields mentionned.
        """
        model = Review
        fields = ["headline", "rating", "body"]

    def __init__(self, *args, **kwargs):
        """Surcharge init to stylish headline form and body form
        """
        super(CreateReview, self).__init__(*args, **kwargs)
        self.fields['headline'].widget.attrs[
                            'style'] = "width:100%; height: 100%;"
        self.fields['body'].widget.attrs[
                            'style'] = "width:100%; height: 100%;"
