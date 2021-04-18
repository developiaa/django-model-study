from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Max

from model.comment import Comment
from model.post import Post
from serializer.comment import CommentSerializer


class CommentView(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	# 대댓글 생성
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			# 대댓글을 달 post, comment 확인
			post_id = kwargs["post_id"]
			comment_id = kwargs["comment_id"]

			comment = Comment.objects.get(id=comment_id, post_id=post_id)
			if comment:
				sequence_max = Comment.objects.filter(group=comment.group, post_id=post_id).aggregate(Max('sequence'))
				sequence = sequence_max["sequence__max"] + 1
				post = Post(id=post_id)

				Comment.objects.create(post=post, sequence=sequence, depth=2, group=comment.group, **request.data)
				return Response(status=200, data=serializer.data)
			else:
				# 데이터 없음
				return Response(status=400)
		else:
			return Response(status=400)
