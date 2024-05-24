from django_filters import rest_framework as filters, DateFromToRangeFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    creator = filters.NumberFilter(field_name='creator_id')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
