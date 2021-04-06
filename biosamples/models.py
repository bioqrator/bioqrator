import datetime 
from django.db import models
from django.urls import reverse

import datetime

class Biosample(models.Model):
    sample_name = models.CharField(max_length=8)
    organism = models.CharField(default='', max_length=32)
    biosample = models.CharField(default='', max_length=32)
    condition = models.CharField(max_length=255, blank=True)
    treatment = models.CharField(max_length=255, blank=True)
    treatment_time = models.CharField(max_length=32, blank=True)
    treatment_conc = models.CharField(max_length=32, blank=True)
    target = models.CharField(max_length=32, blank=True)
    assay = models.CharField(max_length=32, blank=True)
    layout = models.CharField(max_length=32, blank=True)
    platform = models.CharField(max_length=32, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.sample_name

    def get_absolute_url(self):
        return reverse('biosamples:detail', kwargs={'pk': self.pk})

    @staticmethod
    def create_new(sample_name, organism, biosample, condition, treatment,
                treatment_time, treatment_conc, target, assay, layout, platform):
        biosample = Biosample.objects.create(sample_name=sample_name,
                                            organism=organism,
                                            biosample=biosample,
                                            condition=condition,
                                            treatment=treatment,
                                            treatment_time=treatment_time,
                                            treatment_conc=treatment_conc,
                                            target=target,
                                            assay=assay,
                                            layout=layout,
                                            platform=platform)
        return biosample 

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Biosample._meta.fields]

class Similarity(models.Model):
    src = models.ForeignKey(Biosample, on_delete=models.CASCADE, related_name='src')
    dst = models.ForeignKey(Biosample, on_delete=models.CASCADE, related_name='dst')
    score = models.FloatField()

    def __str__(self):
        return f'[{self.src.sample_name}]-{self.score}-[{self.dst.sample_name}]'

    class Meta:
        unique_together = ('src', 'dst')