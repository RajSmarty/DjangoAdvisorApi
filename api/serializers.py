from rest_framework import fields, serializers
from api.models import advisor, booking


class bookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = booking
        fields = '__all__'


class advisorListSerializer(serializers.ModelSerializer):
    bookinghistory = bookingSerializer(
        source="booking_set", many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = advisor
        fields = '__all__'
