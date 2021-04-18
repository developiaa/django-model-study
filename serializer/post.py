from rest_framework import serializers

from model.post import Post


class PostSerializer(serializers.ModelSerializer):
	writer = serializers.CharField(max_length=20)
	title = serializers.CharField()
	content = serializers.CharField()

	class Meta:
		model = Post
		fields = ('writer', 'title', 'content')
