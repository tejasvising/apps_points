# serializers.py

from rest_framework import serializers
from .models import App, Task,Image

class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ('id', 'image','date')

class TaskSerializer(serializers.ModelSerializer):
     class Meta:
         model = Task
         fields = ('id', 'name','points','image')
# class TaskSerializer(serializers.ModelSerializer):
#     #parameters = ParameterSerializer(many=True, required=False)

#     #id = AndroidAppSerializer(many=True,required=True) 
#     image = ImageSerializer(required=False,read_only=True) # Set read_only to True

#     class Meta:
#         model =Task
#         fields = ['id','name','points','image']

#         def create(self, validated_data):
#             return super().create(validated_data)
#     #     """
#     #     Serializes an image if it has been uploaded, then passes the image
#     #     back to the validated_data to finish creating the Announcement.
#     #     """
#         #  print("iamaserializer")
#         #  image_data = self.context['request'].FILES
#         #  if image_data:
#         #      serializer = ImageSerializer(data=image_data)
#         #      serializer.is_valid(raise_exception=True)
#         #      image = serializer.save()
#         #      validated_data['image'] = image
            






