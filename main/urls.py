from django.urls import include, path
from .views import ScoreIQView, ScoreEQView, ResultsView, create_test

urlpatterns = [
	path("",create_test),
    path("scoreiq/", ScoreIQView.as_view({"post": "create"})),
    path("scoreeq/", ScoreEQView.as_view({"post": "create"})),
    path('results/<str:login>', ResultsView.as_view({'get':'retrieve'}))
]