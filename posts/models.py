from django.db import models
from django.contrib.auth import get_user_model
#이미지, 조회수, 작성자, 내용, 날짜
User=get_user_model()
class Post(models.Model):
    image=models.ImageField(verbose_name='이미지',null=True,blank=True)
    content=models.TextField(verbose_name='내용')
    created_at=models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    view_count=models.IntegerField(verbose_name='조회수',default=0)
    writer=models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
#댓글 모델 만들어보기 / 내용,작성일, 게시글 ,작성자
class Comment(models.Model):
    content=models.TextField(verbose_name='내용')
    created_at=models.DateTimeField(verbose_name='작성일')
    post=models.ForeignKey(to='Post',on_delete=models.CASCADE)
    writer=models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)

# Create your models here.
