# 데이터 구조 정의
from django.db import models
from django.urls import reverse


# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # 수정이 완료된 후 이동할 페이지는 뷰에 success_url 이 설정되어 있거나 모델에 get_absolute_url 메소스로 결정
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
