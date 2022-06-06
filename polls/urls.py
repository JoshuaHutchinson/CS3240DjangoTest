from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('deepthoughts/', views.deepthoughtsview, name='deep thoughts'),
    path('deepthoughts/list/', views.deepthoughtslist, name="list"),
    path('deepthoughts/<str:url>/', views.deepthoughtsdetail, name="deep thoughts detail"),
    path('home/', views.homeview, name='home'),
]