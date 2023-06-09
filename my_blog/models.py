from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Aqui o status da publicação ficaria 0 por rascunho e 1 para publicação
STATUS = ((0, 'Draft'), (1, 'Publised'))

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts') #Com usuário deletado, a autoria também será
    created_on = models.DateField(auto_now_add=True)
    update_on = models.DateField(auto_now=True)
    content = RichTextUploadingField()
    status = models.IntegerField(choices=STATUS, default=0)

    class meta:
        ordering = ['-created_on']

def __STR__(self):
    return self.title
