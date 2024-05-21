from django.urls import path
from .views import (index, models_by_brands, detail, add, user_register, user_login, user_logout, edit, delete,
                    user_profile, save_comment)

urlpatterns = [
    path('', index, name='index'),
    path('models_by_brands/<int:id>/', models_by_brands, name='models_by_brands'),
    path('detail/<int:id>/', detail, name='detail'),
    path('add/', add, name='add'),
    path('edit<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('user_register/', user_register, name="user_register"),
    path('profile/<str:username>/', user_profile, name="user_profile"),
    path('comment/<int:model_id>/', save_comment, name='comment'),
]
