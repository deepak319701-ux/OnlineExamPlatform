from django.urls import path
from . import views

urlpatterns = [

    path(
        "exam/<int:exam_id>/",
        views.exam_page,
        name="exam_page",
    ),

]