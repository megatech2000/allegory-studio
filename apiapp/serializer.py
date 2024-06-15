from rest_framework import serializers
from .models import Work,Featured,GearCategory,GearItem

class WorkSerializer(serializers.ModelSerializer):
    image_fields = ['home_image', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6']

    # Dynamically add the ImageFields to the class
    for field in image_fields:
        exec(f"{field} = serializers.ImageField(max_length=None, use_url=True)")

    class Meta:
        model = Work
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    image_fields = ['image']

    # Dynamically add the ImageFields to the class
    for field in image_fields:
        exec(f"{field} = serializers.ImageField(max_length=None, use_url=True)")

    class Meta:
        model = Featured
        fields = '__all__'

class GearCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GearCategory
        fields = '__all__'

class GearItemSerializer(serializers.ModelSerializer):
    image_fields = ['image']

    # Dynamically add the ImageFields to the class
    for field in image_fields:
        exec(f"{field} = serializers.ImageField(max_length=None, use_url=True)")
    class Meta:
        model = GearItem
        fields = '__all__'

        

    