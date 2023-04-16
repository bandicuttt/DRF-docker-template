from django.urls import path, include
from users.views.users import CreateUserViewSet, LoginAPIView
from knox.views import LogoutView, LogoutAllView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'create-user', CreateUserViewSet,'create-user')

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]
urlpatterns += router.urls
