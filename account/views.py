from django.contrib.auth import login, logout, authenticate
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.middleware.csrf import get_token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  # 新規登録は認証不要
        return [IsAuthenticated()]  # その他は認証必須
    
    
# ログイン用の関数ベースビュー
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    
    print("Received login request with email:", email)
    
    if user is not None:
        # 認証成功時にトークンを取得または新規作成
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return JsonResponse({
            "message": "Login successful",
            "token": token.key,
            })
    else:
        print("認証に失敗しました:", email)  # デバッグ出力
        return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# ログアウト
@api_view(['POST'])
def logout_user(request):
    logout(request)  # ユーザーをログアウトさせる（セッションを削除）
    return JsonResponse({"message": "Logout successful"}, status=status.HTTP_200_OK)

# login_userを返す
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def current_user(request):
    if request.user.is_authenticated:
        # ユーザーがログインしている場合、ユーザー情報を返す
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # 未ログインの場合はエラーレスポンスを返す
        return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

# csrftokenのエンドポイント アプリ起動時にアクセス
@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrftoken': csrf_token})
