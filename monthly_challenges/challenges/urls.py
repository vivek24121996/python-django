from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february)
    # path("<month>", views.monthly_challenge)
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_month),
    # path("<str:month>", views.monthly_challenge)
    path("<str:month>", views.monthly_challenge, name="monthly_challenge")
]
