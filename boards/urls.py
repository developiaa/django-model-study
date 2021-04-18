from rest_framework import routers
from django.urls import path, include
from rest_framework.routers import DynamicRoute

from boards.views.post import PostView
from boards.views.comment import CommentView

router = routers.DefaultRouter()

router.register(r'post', PostView)
# router.register(r'post/<int:pk>/comment', CommentView)

urlpatterns = [
	# path(r'post/', include(router.urls)),
	path(r'post/<int:post_id>/comment/<int:comment_id>/', CommentView.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns += router.urls
