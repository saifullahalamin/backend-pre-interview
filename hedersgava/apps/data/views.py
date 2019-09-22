from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

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
