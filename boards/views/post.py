from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.db.models import Max

from model.comment import Comment
from model.post import Post
from serializer.comment import CommentSerializer
from serializer.post import PostSerializer


# Create your views here.
class PostView(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def create(self, request, *args, **kwargs):
		# 둘 다 가능
		# get_serializer 함수는 위에서 serializer_class에서 선언한 serializer을 가져온다
		# serializer = PostSerializer(data=request.data)
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=200, data=serializer.data)
		else:
			return Response(status=400)

	@action(methods=['post'], detail=True)
	def comment(self, request, *args, **kwargs):
		serializer = CommentSerializer(data=request.data)
		if serializer.is_valid():
			# 댓글을 달 post 번호
			post_id = kwargs["pk"]
			# 그룹 번호 갱신
			group_max = Comment.objects.all().aggregate(Max('group'))
			group = group_max["group__max"] + 1

			post = Post(id=post_id)
			Comment.objects.create(post=post, group=group, **request.data)

			return Response(status=200)
		else:
			return Response(status=400)
