from crispy_forms.helper import  FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet, entervaluesAOFT1





# class entervaluesAOFT(forms.Form):
#     # name =  forms.CharField( )
#     # email = forms.EmailField(label='E-Mail')
#     category = forms.ChoiceField(choices = [('area_of_triangle', 'Area_of_triangle')]) #, ('convert_to_secondns, "Convert_to_seconds'), ('text_repeater', 'Text_repeater')] )
#     number1 = forms.FloatField(label= 'First side')
#     number2 = forms.FloatField(label= 'Second side')
#     number3 = forms.FloatField(label= 'Third side') #widget= forms.FloatField)
#     body = forms.CharField(widget = forms.Textarea)
#     def __init__(self, *arg, **kwargs):
#         super(). __init__(*args, **Kwargs)
#
#         self.helper = FormHelper
#         self.helper.form_method = 'post'

class entervaluesAOFT(forms.ModelForm):

    class Meta:
        model = entervaluesAOFT1
        fields = ('number1', 'number2', 'number3')

# class response(forms.ModelForm):
#     class Meta:
#         model = data_process
#         fields = ('result')

class sippetform (forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('number1', 'number2', 'number3')