from django.urls import path

from .views import QuestionViewSet, ChoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('question', QuestionViewSet, basename='question')
router.register('choice', ChoiceViewSet, basename='choice')
urlpatterns = router.urls