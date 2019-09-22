from rest_framework import serializers


class ElementSerializer(serializers.Serializer):
    datetime = serializers.SerializerMethodField()
    value = serializers.DecimalField(read_only=True, max_digits=19, decimal_places=5)
    unit = serializers.SerializerMethodField()

    def get_datetime(self, instance):
        return instance.data.record_time

    def get_unit(self, instance):
        return instance.device.unit
