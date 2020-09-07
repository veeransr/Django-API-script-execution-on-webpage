from django import forms
from .models import Snippet, entervaluesFME

# class entervalues1(forms.Form):
#     # name =  forms.CharField( )
#     # email = forms.EmailField(label='E-Mail')
#     category = forms.ChoiceField(choices = [('find_max_edge', 'Find_max_edge')]) #, ('convert_to_secondns, "Convert_to_seconds'), ('text_repeater', 'Text_repeater')] )
#     number1 = forms.FloatField(label= 'First side')
#     number2 = forms.FloatField(label= 'Second side')
#      #widget= forms.FloatField)
#     # body = forms.CharField(widget = forms.Textarea)

class entervaluesFME (forms.ModelForm):

    class Meta:
        model = entervaluesFME
        fields = ('number1', 'number2')

class snippetform (forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('number1', 'number2')