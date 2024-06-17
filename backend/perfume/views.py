from django.views.generic import TemplateView, ListView
from django.db.models import Min
from perfume.models import Perfume, Aroma, Vendor


class PerfumeListView(ListView):
    model = Perfume
    template_name = 'perfume/index.html'
    queryset = (
        Perfume.objects.prefetch_related('vendors', 'aromas')
        .filter(sex='M')
        .annotate(price=Min('perfumevendor__price'))
    )
    ordering_by = 'perfume.price'
    paginate_by = 10
    context_object_name = 'perfumes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aromas'] = Aroma.objects.all()
        context['types'] = Perfume.TYPE_CHOICES
        return context
