from django.forms import ModelForm, DateTimeInput, HiddenInput, FileField
from django import forms
from notesapp.models import Notes


class NoteUpdateForm(ModelForm):
    image_with_text = FileField(required=False, widget=forms.FileInput(attrs={"accept": "image/*",
                                                                              "onchange": ""}))

    class Meta:
        model = Notes
        fields = ['title', 'category', 'text', 'reminder']
        widgets = {
            'reminder': DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class NoteCreateForm(ModelForm):
    image_with_text = FileField(required=False, widget=forms.FileInput(attrs={"accept": "image/*",
                                                                              "onchange": ""}))
    class Meta:
        model = Notes
        fields = "__all__"
        widgets = {
            'reminder': DateTimeInput(attrs={'type': 'datetime-local'}),
            'author': HiddenInput(),
        }
