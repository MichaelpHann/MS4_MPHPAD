from django import forms
from .models import Project, ProjectCategory


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = ProjectCategory.objects.all()
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
