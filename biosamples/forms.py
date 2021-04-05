from django import forms 
from .models import Biosample, Similarity
import random

class BiosampleForm(forms.Form):
    sample_name = forms.CharField()
    
    def send_mail(self):
        pass 
    
    def measure(self):
        print("Measuring similarity...")
        for other in Biosample.objects.exclude(id=self.biosample.pk):
            score = random.random()
            Similarity.objects.create(src=self.biosample, dst=other, score=score)
            Similarity.objects.create(src=other, dst=self.biosample, score=score)

    def save(self):
        self.biosample = Biosample.create_new(self.cleaned_data['sample_name'])
        return self.biosample