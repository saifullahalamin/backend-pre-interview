from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class NotValidTimestampParamAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('datetime param has not valid Timestamp value.')


class NotValidDatetimeParamAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('datetime param has not valid Datetime format value. Please use ISO format')


class NotValidXmlDataAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Please provide valid xml data.')
