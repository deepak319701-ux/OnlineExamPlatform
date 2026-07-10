from django.urls import path
from . import views

urlpatterns = [
    
    
    path(
    "my-results/",
    views.my_results,
    name="my_results",
),

    path(
        "result/<int:exam_id>/",
        views.result_page,
        name="result_page",
    ),
    path(
    "leaderboard/",
    views.leaderboard,
    name="leaderboard",
),
   path(
    "certificate/<int:exam_id>/",
    views.download_certificate,
    name="download_certificate",
),
]