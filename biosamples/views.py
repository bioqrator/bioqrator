from django.views import generic 
from django.urls import reverse_lazy 

from .models import Biosample
from .forms import BiosampleForm

class IndexView(generic.ListView):
    template_name = 'biosamples/index.html'
    context_object_name = 'whole_biosamples'
    paginate_by = 20

    def get_queryset(self):
        return Biosample.objects.all()

class DetailView(generic.DetailView):
    model = Biosample 
    template_name = 'biosamples/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'test'
        context['similars'] = self.object.src.all().order_by('-score')[:5]
        return context

class BiosampleView(generic.edit.FormView):
    template_name = 'biosamples/form.html'
    form_class = BiosampleForm

    def get_success_url(self):
        return self.biosample.get_absolute_url()

    def form_valid(self, form):
        self.biosample = form.save()
        form.measure()
        return super().form_valid(form)