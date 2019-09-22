from datetime import datetime
from django.utils import dateparse
from apps.data.exceptions import NotValidDatetimeParamAPIException


class DataFilterMixin:
    """
    enable datetime filtering on
    - /data
    - /data/<id>

    Usage:
    - /data?datetime=1569113600 => use timestamp
    - /data?datetime=2071-09-09T02:11:13+00:00 => use datetime ISO format
    """

    def get_datetime_filter(self):
        datetime_filter = self.request.GET.get('datetime')
        if datetime_filter:
            try:
                datetime_filter = datetime.fromtimestamp(float(datetime_filter))
            except ValueError:
                try:
                    datetime_filter = datetime_filter.replace(' ', '+')
                    datetime_filter = dateparse.parse_datetime(datetime_filter)
                except ValueError:
                    raise NotValidDatetimeParamAPIException()
            return datetime_filter
        return ''
