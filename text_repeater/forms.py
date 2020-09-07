from django import forms
from .models import Snippet, entervaluesTR

class entervaluesTR(forms.ModelForm):
    # # name =  forms.CharField( )
    # # email = forms.EmailField(label='E-Mail')
    # category = forms.ChoiceField(choices = [('text_repeater', 'Text_repeater')]) #, ('convert_to_secondns, "Convert_to_seconds'), ('text_repeater', 'Text_repeater')] )
    # text = forms.CharField()
    # number = forms.IntegerField(label= 'Number of times to be repeated')
    #
    # # body = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = entervaluesTR
        fields = ('text', 'number')


class snippetform (forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('text', 'number')