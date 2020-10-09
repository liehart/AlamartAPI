from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from AlamartAPI.authsys.serializers import LoginReqSerializers, UserSerializers


class LoginView(APIView):
    def post(self, req):
        req_serializers = LoginReqSerializers(data=req.data)
        req_serializers.is_valid(raise_exception=True)

        user = authenticate(
            email=req_serializers.validated_data['email'].lower(),
            password=req_serializers.validated_data['password']
        )

        if user is None:
            return Response(
                {
                    'message': 'User email or password incorrect',
                    'status': 'failed'
                }, status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_verified and not user.is_staff:
            return Response(
                {
                    'message': 'User has not been confirmed',
                    'status': 'failed'
                }, status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        user.last_login = timezone.now()
        user.save()

        resp_serializers = UserSerializers(user)

        return Response(
            {
                'user': resp_serializers.data,
                'token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK
        )
