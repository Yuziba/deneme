from django.forms import ModelForm
from denemeapp.models import AaModel

class DenemeForm (ModelForm):
    class Meta:
        model = AaModel
        fields = ["nick", "mesaj"]