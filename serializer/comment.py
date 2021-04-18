from rest_framework import serializers

from model.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
	writer = serializers.CharField(max_length=20)
	content = serializers.CharField()
	# depth = serializers.IntegerField(required=False)
	# sequence = serializers.IntegerField(required=False)

	class Meta:
		model = Comment
		fields = ('writer', 'content')
