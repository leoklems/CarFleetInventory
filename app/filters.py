import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class VehicleFilter(django_filters.FilterSet):
    search = CharFilter(lookup_expr='icontains')
    # icontains means ignore case sensetivity
    # table = CharFilter(field_name='table', lookup_expr='icontains')
    serial_number = CharFilter(field_name='serial_number', lookup_expr='icontains')
    # date = django_filters.DateFilter()
    # date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Vehicle
        fields = ['name','serial_number', 'year_purchased', 'year_alloted']
        strict = False  # Set strict to False to allow no filtering when no parameters are present


# class StockingFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#     date = django_filters.DateFromToRangeFilter()

#     class Meta:
#         model = Stock
#         fields = ["item", "staff", "kind", "date"]


# class VisitorFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#     name = CharFilter(field_name='name', lookup_expr='icontains')

#     class Meta:
#         model = Visitor
#         fields = []


# class StaffAttendanceFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#     # lib_no = CharFilter(field_name='user.lib_no', lookup_expr='icontains')

#     class Meta:
#         model = StaffAttendance
#         fields = ['user__lib_no']


# class BookFilter(django_filters.FilterSet):

#     # icontains means ignore case sensetivity
#     title = CharFilter(field_name='title', lookup_expr='icontains')
#     other_contributors = CharFilter(field_name='other_contributors', lookup_expr='icontains')
#     author = CharFilter(field_name='author', lookup_expr='icontains')

#     class Meta:
#         model = OfflineBook
#         fields = ['call_no',]


# class EbookFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#     title = CharFilter(field_name='title', lookup_expr='icontains')
#     other_contributors = CharFilter(field_name='other_contributors', lookup_expr='icontains')
#     author = CharFilter(field_name='author', lookup_expr='icontains')

#     class Meta:
#         model = Ebook
#         fields = ['call_no',]


# class BorrowFilter(django_filters.FilterSet):
#     # icontains means ignore case sensetivity
#     title = CharFilter(field_name='title__title', lookup_expr='icontains')

#     class Meta:
#         model = BorrowedBook
#         fields = []

