from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    #generator form based on Project modeo
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']