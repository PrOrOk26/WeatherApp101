from django import forms


class WeatherDataForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
    country = forms.CharField(label='Country', max_length=100)
    date = forms.DateField(label='Date', widget=forms.SelectDateWidget)
