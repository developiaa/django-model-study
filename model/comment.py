from django.db import models

from model.post import Post


class Comment(models.Model):
	writer = models.CharField(max_length=20)
	content = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	group = models.IntegerField()
	depth = models.IntegerField(default=1)
	sequence = models.IntegerField(default=1)

	# def __str__(self):
	# 	return self.content

	class Meta:
		db_table = 'comment'
