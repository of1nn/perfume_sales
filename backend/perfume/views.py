from django.views.generic import ListView
from django.db.models import Min
from perfume.models import Perfume, Aroma
from perfume.filters import PerfumeFilter


class PerfumeListView(ListView):
    model = Perfume
    template_name = 'perfume/index.html'

    ordering = 'perfumevendor__price'
    paginate_by = 10
    context_object_name = 'perfumes'
    filterset_class = PerfumeFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by')
        if sort_by:
            queryset = self.filterset_class().sort_by(
                queryset, sort_by
            )
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset
        )
        return self.filterset.qs.prefetch_related(
            'vendors', 'aromas'
        ).annotate(price=Min('perfumevendor__price'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aromas'] = Aroma.objects.all()
        context['types'] = Perfume.TYPE_CHOICES
        return context
