import django_filters
from django_filters import CharFilter

from .models import *

class CaseFilter(django_filters.FilterSet):

    key_words = CharFilter(field_name='key_words', lookup_expr='icontains')

    class Meta:
        model = Case
        fields = ('role', 'clinician', 'name_of_animal')