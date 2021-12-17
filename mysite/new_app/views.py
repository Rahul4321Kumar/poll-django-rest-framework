from rest_framework import viewsets
from rest_framework.views import APIView

from new_app import models
from new_app import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [IsAuthenticated]


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
    permission_classes = [IsAuthenticated]


class RegisterView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status" : "success",
                "user_id" : user.id,
                "refresh" : str(refresh),
                "access" : str(refresh.access_token)
            }
        )
