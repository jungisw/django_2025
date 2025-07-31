from django.db import models

# Create your models here. # 모델을 변경하면 서버 종료 후 makemigrations 하고 migrate 하기
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True) # 생성
    updated_date = models.DateTimeField(auto_now=True, null=True) # 날짜 업데이트 해줌

    def __str__(self):
        return f'게시글제목:{self.title}- 게시글 내용 -{self.content} - 생성시간 - {self.created_date} - 수정시간 - {self.updated_date}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

