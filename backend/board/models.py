from django.db import models


class PostVO(models.Model):
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_as = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True
        db_table = 'posts'
