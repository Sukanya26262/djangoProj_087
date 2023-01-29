from django import forms
from django.forms import ChoiceField

# Create your forms here.
BRAND_CHOICES = [
    ('acer', 'ACER'),
    ('hp', 'HP'),
    ('lenovo', 'LENOVO'),
	('asus', 'ASUS'),

]
RAM_CHOICES = [
    ('8gb', '8gb'),
    ('16gb', '16gb'),
    ('32gb', '32gb'),
]
CPU_CHOICES = [
    ('ryzen5', 'ryzen5'),
    ('ryzen7', 'ryzen7'),
    ('ryzen9', 'ryzen9'),
    ('inteli3', 'inteli3'),
    ('inteli5', 'inteli5'),
    ('inteli7', 'inteli7'),
    ('inteli9', 'inteli9'),
]
class ProductForm(forms.Form):
    model = forms.CharField()
    brand = forms.ChoiceField(choices=BRAND_CHOICES)
    ram = forms.ChoiceField(widget=forms.RadioSelect, choices=RAM_CHOICES)
    ssd = forms.DecimalField()
    cpu = forms.ChoiceField(widget=forms.RadioSelect, choices=CPU_CHOICES)
    price = forms.DecimalField()