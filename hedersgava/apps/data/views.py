from datetime import datetime
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response
from apps.data.exceptions import NotValidXmlDataAPIException
from apps.data.mixin import DataFilterMixin
from apps.data.models import Data
from apps.data.parsers import DataXMLParser
from apps.devices.models import Device
from apps.elements.models import Element
from apps.elements.serializers import ElementSerializer


class DataRetrieveAPIView(DataFilterMixin, RetrieveAPIView):
    serializer_class = ElementSerializer

    def get_queryset(self):
        elements = Element.objects.filter(data__id=self.kwargs.get('pk'))

        # filtering by datetime if exists
        datetime_filter = self.get_datetime_filter()
        if datetime_filter:
            elements = elements.filter(record_time=datetime_filter)
        return elements

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DataListCreateAPIView(DataFilterMixin, ListCreateAPIView):
    serializer_class = ElementSerializer
    parser_classes = (DataXMLParser, )

    def get_queryset(self):
        elements = Element.objects.all()

        # filtering by datetime if exists
        datetime_filter = self.get_datetime_filter()
        if datetime_filter:
            elements = elements.filter(record_time=datetime_filter)
        return elements

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if 'id' in request.data and request.data.get('id') \
                and 'record_time' in request.data and request.data.get('record_time') \
                and 'devices' in request.data and request.data.get('devices') \
                and 'data' in request.data and request.data.get('data'):
            # get or create specific data by id
            data, created = Data.objects.get_or_create(id=request.data.get('id'))

            # add devices if not exist
            self.add_devices_if_not_exists(request)

            # push elements to specific data object
            self.push_elements(data, request)

            serializer = self.serializer_class(data.elements.all(), many=True)
            return Response(serializer.data)
        else:
            raise NotValidXmlDataAPIException()

    def push_elements(self, data, request):
        for element in request.data.get('data'):
            if isinstance(element, dict):
                device = Device.objects.get(code=element.get('device'))
                record_time = datetime.fromtimestamp(float(request.data.get('record_time')))
                data.elements.create(device=device, value=element.get('value'), record_time=record_time)

    def add_devices_if_not_exists(self, request):
        for code, name in request.data.get('devices').items():
            if not Device.objects.filter(code=code).exists():
                Device.objects.create(code=code, name=name)
