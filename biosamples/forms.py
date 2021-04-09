from django import forms 
from .models import Biosample, Similarity
import random


class BiosampleForm(forms.Form):
    sample_name = forms.CharField(max_length=8)
    organism = forms.CharField(max_length=32)
    biosample = forms.CharField(max_length=32)
    condition = forms.CharField(max_length=255, required=False)
    treatment = forms.CharField(max_length=255, required=False)
    treatment_time = forms.CharField(max_length=32, required=False)
    treatment_conc = forms.CharField(max_length=32, required=False)
    target = forms.CharField(max_length=32, required=False)
    assay = forms.CharField(max_length=32, required=False)
    layout = forms.CharField(max_length=32, required=False)
    platform = forms.CharField(max_length=32, required=False)

    def send_mail(self):
        pass 
    
    def measure(self):
        print("Measuring similarity...")
        for other in Biosample.objects.exclude(id=self.biosample.pk):
            score = random.random()
            Similarity.objects.create(src=self.biosample, dst=other, score=score)
            Similarity.objects.create(src=other, dst=self.biosample, score=score)

    def save(self):
        print(self.cleaned_data)
        self.biosample = Biosample.create_new(
            self.cleaned_data['sample_name'],
            self.cleaned_data['organism'],
            self.cleaned_data['biosample'],
            self.cleaned_data['condition'],
            self.cleaned_data['treatment'],
            self.cleaned_data['treatment_time'],
            self.cleaned_data['treatment_conc'],
            self.cleaned_data['target'],
            self.cleaned_data['assay'],
            self.cleaned_data['layout'],
            self.cleaned_data['platform'],
        )
        return self.biosample