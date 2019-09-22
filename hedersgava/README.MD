# Note
I upgrade django to ==2.1.7 to fix this issue related to sqlite version
https://stackoverflow.com/questions/53637182/django-no-such-table-main-auth-user-old#comment96910658_54995089

## URLs

- Push data using xml => `POST – /data`
- List of elements by data_id => `GET – /data/<id>`
- Search data by timestamp => `GET – /data?datetime=1569113600`
- Search data by datetime ISO format => `GET – /data?datetime=2071-09-09T02:11:13+00:00`
- Search data by id and timestamp => `GET – /data/<id>?datetime=1569113600`
- Search data by id and datetime ISO format => `GET – /data/<id>?datetime=2071-09-09T02:11:13+00:00`