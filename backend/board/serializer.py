from rest_framework import serializers
from board.models import PostVO as post

class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_as = serializers.DateTimeField(read_only=True)


    class Meta:
        model = post
        fields = ['title', 'content']

    def create(self, validated_data):
        return post.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        return instance