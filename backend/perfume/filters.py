import django_filters as filters

from perfume.models import Perfume


class PerfumeFilter(filters.FilterSet):
    aromas = filters.CharFilter(field_name='aromas__name')

    class Meta:
        model = Perfume
        fields = (
            'aromas',
            'type',
        )

    def sort_by(self, queryset, value):
        expressions = {
            'mark': 'perfumevendor__evaluation',
            'price_asc': 'perfumevendor__price',
            'price_desc': '-perfumevendor__price',
        }
        return queryset.order_by(expressions.get(value, 'id'))
