from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserLoginSerializer, SingupSerializer, UserInfoSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class SingupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SingupSerializer

    def post(self, request):
        serializer = SingupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "user registered successfully"}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

    class UserProfileView(generics.RetrieveUpdateAPIView):
        serializer_class = UserInfoSerializer
        permission_classes = [IsAuthenticated]
        
        def get_object(self):
            return self.request.user