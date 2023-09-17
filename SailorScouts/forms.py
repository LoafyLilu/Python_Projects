from django.forms import ModelForm
from .models import Scout

#Creates Scout Form based on Scout Model
class ScoutForm(ModelForm):
    class Meta:
        model = Scout
        fields = '__all__'
