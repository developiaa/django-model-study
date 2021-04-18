from django.db import models


class Post(models.Model):
	writer = models.CharField(max_length=20)
	title = models.TextField()
	content = models.TextField()
	is_delete = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	return self.title

	class Meta:
		db_table = 'post'
