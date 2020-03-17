from django.db import models
from django.urls import reverse

# Create your models here.
# 글의 분류(일상, 유머, 정보)
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 카테고리를 입력하세요. (ex:일상)")

    def __str__(self):
        return self.name

# 블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    # 하나의 글은 여러가지 분류에 포함될 수 있다. (ex:정보, 유머), 하나의 분류는 여러가지 글이 포함될 수 있다.
    category = models.ManyToManyField(Category, help_text="글의 분류를 선택하세요.")

    def __str__(self):
        return self.title

    # 1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def is_comment_more300(self):
        return len(self.content) > 300

    def get_comment_under300(self):
        return self.content[:300]