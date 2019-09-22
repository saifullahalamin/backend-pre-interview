from datetime import datetime
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.data.exceptions import NotValidTimestampParamAPIException, NotValidDatetimeParamAPIException
from apps.elements.models import Element
from apps.elements.serializers import ElementSerializer


class DataRetrieveAPIView(RetrieveAPIView):
    serializer_class = ElementSerializer

    def get_queryset(self):
        return Element.objects.filter(data__id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DataListCreateAPIView(ListCreateAPIView):
    serializer_class = ElementSerializer

    def get_queryset(self):
        elements = Element.objects.all()

        # filtering by datetime if exists
        datetime_filter = self.get_datetime_filter()
        if datetime_filter:
            elements = elements.filter(data__record_time=datetime_filter)
        return elements

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def get_datetime_filter(self):
        datetime_filter = self.request.GET.get('datetime')
        if datetime_filter:
            if datetime_filter.isdigit():
                try:
                    datetime_filter = datetime.fromtimestamp(int(datetime_filter))
                except ValueError:
                    raise NotValidTimestampParamAPIException()
            else:
                try:
                    datetime_filter = datetime.strptime(datetime_filter, '%Y-%m-%dT%H:%M:%SZ')
                except ValueError:
                    raise NotValidDatetimeParamAPIException()
            return datetime_filter
        return ''
