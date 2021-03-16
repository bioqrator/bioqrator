import datetime 
from django.db import models
from django.urls import reverse

class Biosample(models.Model):
    sample_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sample_name

    def get_absolute_url(self):
        return reverse('biosamples:detail', kwargs={'pk': self.pk})

    @staticmethod
    def create_new(sample_name):
        biosample = Biosample.objects.create(sample_name=sample_name)
        return biosample 

class Similarity(models.Model):
    src = models.ForeignKey(Biosample, on_delete=models.CASCADE, related_name='src')
    dst = models.ForeignKey(Biosample, on_delete=models.CASCADE, related_name='dst')
    score = models.FloatField()

    def __str__(self):
        return f'[{self.src.sample_name}]-{self.score}-[{self.dst.sample_name}]'

    class Meta:
        unique_together = ('src', 'dst')