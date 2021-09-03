from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView


urlpatterns = [
    # 루트페이지, 보통 클래스형 뷰일 경우 .as_view()를 붙여줘야 정상적으로 처리, name은 URL패턴 찾을 이름
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
