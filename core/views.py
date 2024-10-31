from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer, SubscribeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            refresh = RefreshToken.for_user(user)  
            return Response({
                'message': 'User created successfully',
                'access': str(refresh.access_token),  
                'refresh': str(refresh),  
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        user = serializer.validated_data['user']  
        refresh = RefreshToken.for_user(user)  
        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'email': user.email,
            'access': str(refresh.access_token),  
            'refresh': str(refresh), 
        }, status=status.HTTP_200_OK)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token is None:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  
            return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class SubscribeAPIView(APIView):
    def post(self, request):
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)