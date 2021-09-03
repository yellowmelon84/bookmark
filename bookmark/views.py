# 기능/로직 구현
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark


# Create your views here.
# 뷰는 함수형과 클래스형이 있는데 장고의 기능을 상속받을 떄는 클래스형을 사용
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6                     # 한페이지에 몇개씩 출력하는지 설정


class BookmarkCreateView(CreateView):
    model = Bookmark                    # 어떤 모델을 가지고 올 것인지 정의
    fields = ['site_name', 'url']       # 어떤 필드를 받을 것인지 정의
    success_url = reverse_lazy('list')  # 글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create'    # 사용할 템플릿 접미사만 변경하는 설정 값


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

