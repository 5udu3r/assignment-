from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializing Categories
    """
    class Meta:
        # model = Category
        fields = [
            'id', 'name', 'slug'
        ]
        read_only_fields = [
           'slug',
        ]