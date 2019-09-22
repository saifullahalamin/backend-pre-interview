from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response as response
# Create your views here.

@api_view(['POST'])
def echo(request):
    """
    Request json data and return it
    """
    if request.method == 'POST':
        data = request.data
        if data:
            return response(data, status=200, content_type=request.content_type)
        return response(status=status.HTTP_400_BAD_REQUEST)
