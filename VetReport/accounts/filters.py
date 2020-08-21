import django_filters
from django_filters import CharFilter

from .models import *

class CaseFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = Case
        fields = ('role', 'clinician', 'name_of_animal', 'key_words')

    def filter_by_ordering(self, queryset, name, value):
        expression = 'date_created' if value == 'ascending' else '-date_created'
        return queryset.order_by(expression)