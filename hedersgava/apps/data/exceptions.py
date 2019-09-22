from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class NotValidTimestampParamAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('datetime param has not valid Timestamp value.')


class NotValidDatetimeParamAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('datetime param has not valid Datetime format value. valid format: 2019-09-20T18:45:45Z')