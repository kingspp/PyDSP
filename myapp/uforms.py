from django import forms

YESNO = (
    ('Yes','DFT'),
    ('No','IDFT'),
)

class Output(forms.Form):
    input1 = forms.CharField(label='x(n)',max_length=20)
    input2 = forms.CharField(label='h(n)',max_length=20)

class Ndft_form(forms.Form):
    input1 = forms.CharField(label='x(n)',max_length=20)

class Imp_form(forms.Form):
    input1 = forms.CharField(label='x(n)',max_length=20)
    input2 = forms.CharField(label='y(n)',max_length=20)

class Dft_idft(forms.Form):
    input1 = forms.CharField(label='x(n)',max_length=20)
    choice = forms.ChoiceField(widget=forms.RadioSelect,choices=YESNO,initial='Yes',label='Choose between DFT / IDFT')



