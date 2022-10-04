from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('category', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('category/<int:category_id>/material/<int:material_id>', views.material, name="material"),
    path('material/<int:material_id>/comment', views.comment, name="comment")
]