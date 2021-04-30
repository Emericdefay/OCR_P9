from django import forms


class CreateReview(forms.Form):
    """[summary]

    Args:
        forms ([type]): [description]
    """
    headline = forms.CharField()
    rating = forms.IntegerField(min_value=0, max_value=5)
    body = forms.CharField(widget=forms.Textarea)
    # image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        """[summary]
        """
        super(CreateReview, self).__init__(*args, **kwargs)
        self.fields['headline'].widget.attrs['style'] = "width:100%; height: 100%;"
        #self.fields['headline'].widget.attrs['rows'] = 1
        self.fields['body'].widget.attrs['style'] = "width:100%; height: 100%;"
        #self.fields['body'].widget.attrs['rows'] = 10
        #self.fields["rating"].widget = forms.ChoiceField(choices=[(1, 1)])


"""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
"""