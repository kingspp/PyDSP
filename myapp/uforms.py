from django import forms

class Output(forms.Form):
    input1 = forms.CharField(label='x(n)',max_length=20)
    input2 = forms.CharField(label='h(n)',max_length=20)

class Ndft_form(forms.Form):
    input1 = forms.CharField(label='x(n)',max_length=20)

class Imp_form(forms.Form):
    input1 = forms.CharField(label='x(n)',max_length=20)
    input2 = forms.CharField(label='y(n)',max_length=20)


