from django import forms
from .widgets import CustomClearableFileInput
from .models import Project, ProjectCategory


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = ProjectCategory.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
