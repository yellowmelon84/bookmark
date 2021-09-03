# 모델을 관리자 페이지에 등록해 관리할 수 있도록 하는 역할과 관리자 페이지 내용을 변경하는 코드
from django.contrib import admin

from .models import Bookmark


# Register your models here.
admin.site.register(Bookmark)