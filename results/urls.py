from django.urls import path
from . import views

urlpatterns = [

    path(
        "result/<int:exam_id>/",
        views.result_page,
        name="result_page",
    ),

]