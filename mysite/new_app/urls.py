from django.urls import path, include
from .views import QuestionViewSet, ChoiceViewSet, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('question', QuestionViewSet, basename='question')
router.register('choice', ChoiceViewSet, basename='choice')

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterView.as_view(), name='register'),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token')
]