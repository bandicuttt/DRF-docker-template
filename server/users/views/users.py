from rest_framework.permissions import AllowAny
from users.serializers.users import CreateUserSerializer, LoginSerializer
from users.models.users import User
from knox import views as knox_views
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import action
from rest_framework import mixins, viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse

@extend_schema_view(
    create=extend_schema(
    summary='Регистрация пользователя',
    tags=['users'],
    responses={201:OpenApiResponse(response=CreateUserSerializer)}
    )
)
class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


@extend_schema_view(
    post=extend_schema(summary='Авторизация пользователя', tags=['users']),
)
class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response.data, status=status.HTTP_200_OK)