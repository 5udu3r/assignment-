from rest_framework import serializers


class AuthMobileSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(max_length=200)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['username'] = serializers.CharField()
    #     self.fields['password'] = serializers.CharField()
