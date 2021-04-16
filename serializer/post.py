from rest_framework import serializers
from model.post import Post


class PostSerializer(serializers.Serializer):

	def validate(self, data):
		print(data)

	class Meta:
		model = Post
		fields = '__all__'
