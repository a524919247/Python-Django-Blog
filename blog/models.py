from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail

class BlogType(models.Model):
    type_name = models.CharField('博客类型',max_length=15)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField('题目',max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail)
    created_time =  models.DateTimeField('创建时间',auto_now_add=True)
    last_updated_time = models.DateTimeField('最后更新时间',auto_now=True)

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return '<Blog:%s>'% self.title

    class Meta:
        verbose_name = '博客列表'
        verbose_name_plural = '博客列表'
        ordering = ['-created_time']