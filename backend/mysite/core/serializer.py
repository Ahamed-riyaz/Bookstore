from rest_framework import serializers
from .models import Person, Color

# class color_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Color
#         fields = ['name']
class person_serializer(serializers.ModelSerializer):
    # color = color_serializer()
    country = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1

    def get_country(self, obj):
        color_name = Color.objects.get(id = obj.color.id)
        return {"color_name": color_name.color_name, "hex_code": '000'}

