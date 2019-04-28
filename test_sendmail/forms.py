from django import forms


class EmailForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'From Email',
                                                                'class': 'form-control'}))
    to_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'To Email',
                                                             'class': 'form-control'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'subject',
                                                                            'class': 'form-control'}))
    attach = forms.Field(widget=forms.FileInput, required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Email body',
                                                           'class': 'form-control',
                                                           'style': 'height:100px!important'}))
