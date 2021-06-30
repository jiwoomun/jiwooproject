from rest_framework import serializers
from member.models import MemberVO as member


class MemberSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = member
        fields = ['username', 'password', 'name', 'email']

    def create(self, validated_data):
        return member.objects.create(**validated_data)

        """
        Create and return a new `Snippet` instance, given the validated data.
        """

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        return instance

        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
