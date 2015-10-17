__author__ = 'ishant'

from django import forms

class ToolForm(forms.Form):
    name = forms.FileField()

class FileForm(forms.Form):
    file = forms.FileField()

class IntForm(forms.Form):
    int_field = forms.IntegerField()

class FloatForm(forms.Form):
    float_field = forms.FloatField()

class StringForm(forms.Form):
    string_field = forms.CharField(max_length=3000)