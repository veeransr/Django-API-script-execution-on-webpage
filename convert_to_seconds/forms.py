from django import forms
from .models import Snippet, entervaluesCTS

class entervaluesCTS(forms.ModelForm):
    # name =  forms.CharField( )
    # email = forms.EmailField(label='E-Mail')
    # category = forms.ChoiceField(choices = [('convert_to_seconds', 'Convert_to_seconds')]) #, ('convert_to_secondns, "Convert_to_seconds'), ('text_repeater', 'Text_repeater')] )
    # days = forms.IntegerField(label= 'Days')
    # hours = forms.IntegerField(label='Hours')
    # minutes = forms.IntegerField(label='Minutes')
    # seconds = forms.IntegerField(label='Seconds')
 #widget= forms.FloatField)
    # body = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = entervaluesCTS
        fields = ('days', 'hours', 'minutes', 'seconds')


class snippetform (forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('days', 'hours', 'minutes', 'seconds')