from django.urls import resolve, reverse 
from django.test import TestCase 

from .models import Biosample


class BiosampleIndexViewTest(TestCase):

    def test_index_uses_right_template(self):
        response = self.client.get(reverse('biosamples:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'biosamples/index.html')

    def test_no_biosamples(self):
        response = self.client.get(reverse('biosamples:index'))
        self.assertContains(response, "Sorry, no biosamples found on our server")
        self.assertQuerysetEqual(response.context['whole_biosamples'], [])

    def test_with_biosamples(self):
        for i in range(3):
            Biosample.objects.create(sample_name=f"sample {i}")

        response = self.client.get(reverse('biosamples:index'))
        self.assertContains(response, "Qrated Biosamples")

        for i in range(3):
            self.assertContains(response, f"sample {i}")
