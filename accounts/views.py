from rest_framework import views,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from .forms import RegisterForm,LoginForm
from .serializers import UserSerializer

# Create your views here.
class RegisterAPIView(views.APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        form = RegisterForm(request.data)
        if form.is_valid():
            user = form.save()
            token,_ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User registered successfully",
                "token": token.key,
                "user": UserSerializer(user).data
            },status = status.HTTP_201_CREATED)
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(views.APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        form = LoginForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            token,_ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message": "Login successful",
                    "token": token.key,
                    "user": UserSerializer(user).data
                },
                status=status.HTTP_200_OK
            )
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)
    


class ProtectedAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({
            "message": "This is a protected endpoint",
                "user": UserSerializer(request.user).data
        },status=status.HTTP_200_OK)
    
    