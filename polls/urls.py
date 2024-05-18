from django.urls import path
from polls import views

# app_name = "polls"
# urlpatterns = [
#     #ex: /polls/
#     path('', views.index, name='index-page'),
#     #ex: /polls/5/
#     path("<int:question_id>/", views.detail, name='detail-page'),
#     #ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name='results-page'),
#     #ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name='vote-page'),
# ]


app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail-page"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results-page"),
    path("<int:question_id>/vote/", views.vote, name="vote-page"),
]