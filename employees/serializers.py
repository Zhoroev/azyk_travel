from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'mobile', 'mobile2', 'email', 'image',)

    # def _get_image_url(self, obj):
    #     try:
    #         if obj.image is None:
    #             return None
    #
    #         url = obj.image.url
    #         request = self.context.get('request')
    #         if request is not None:
    #             return request.build_absolute_uri(url)
    #         return url
    #     except:
    #         return ''
    #
    # def to_representation(self, instance):
    #     res = super().to_representation(instance)
    #     res['image'] = self._get_image_url(instance)
    #     return res