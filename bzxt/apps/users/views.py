from django.contrib.auth.backends import ModelBackend
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserReSerializer, UserDetailSerializer
from utils.permissions import IsSuperAdmin, IsSuperAdminOrOwner


class CustomBackend(ModelBackend):
    # 自定义用户验证
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            users = UserProfile.objects.filter(isDelete=False)
            user = users.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(viewsets.ModelViewSet):
    # 用户
    queryset = UserProfile.objects.all()
    serializer_class = UserReSerializer
    lookup_field = 'username'

    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return UserReSerializer
    #     return UserDetailSerializer

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            return [IsAuthenticated(), ]
        elif self.action == 'create':
            return []
        else:
            return [IsAuthenticated(), IsSuperAdminOrOwner(), ]
            # return [IsAuthenticated(), IsSuperAdmin(), ]
            # return [IsAuthenticated(), ]

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['username'] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_update(self, serializer):
    #     if 'password' in serializer.validated_data.keys():
    #         user = self.get_object()
    #         user.set_password(serializer.validated_data['password'])
    #         serializer.validated_data['password'] = user.password
    #     serializer.save()

    def perform_destroy(self, instance):
        instance.isDelete = True
        instance.save()

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
