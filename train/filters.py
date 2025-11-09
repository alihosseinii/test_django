import django_filters


class filter_trains(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    origin = django_filters.CharFilter(field_name='origin', lookup_expr='icontains')
    departure_after = django_filters.DateTimeFilter(field_name='departure_time', lookup_expr='gte')
    departure_before = django_filters.DateTimeFilter(field_name='departure_time', lookup_expr='lte')
    departure_date = django_filters.DateFilter(field_name='departure_time__date', lookup_expr='exact')
