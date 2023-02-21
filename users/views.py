import jwt
import requests
from config import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, NotFound
from rest_framework import status
from .serializers import PrivateUserSerializer
from .models import User


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError("You should be insult password.")

        serializer = PrivateUserSerializer(data=request.data)

        if serializer.is_valid():
            saved_user = serializer.save()
            saved_user.set_password(password)
            saved_user.save()
            serializer = PrivateUserSerializer(saved_user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PublicUser(APIView):
    def get(sefl, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)


class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response(
                {"ok": "welcome!"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Wrong Password."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "bye!"})


class JWTLogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",  # 업계 표준
            )
            return Response({"token": token})
        else:
            return Response({"error": "Wrong password"})


class GithubLogIn(APIView):
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                f"https://github.com/login/oauth/access_token?code={code}&client_id=f61c955f466d92d1cac9&client_secret={settings.GH_SECRET}",
                headers={"Accept": "application/json"},
            )
            access_token = access_token.json().get("access_token")
            user_data = requests.get(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_data = user_data.json()
            user_emails = requests.get(
                "https://api.github.com/user/emails",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_emails = user_emails.json()
            try:
                user = User.objects.get(email=user_emails[0]["email"])
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                if user_data.get("name") == None:
                    user_data["name"] = user_data.get("login")
                user = User.objects.create(
                    username=user_data.get("login"),
                    name=user_data.get("name"),
                    avatar=user_data.get("avatar_url"),
                    email=user_emails[0]["email"],
                )
                user.set_unusable_password()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("GithubLogIn POST() Error >>>: ", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class KakaoLogIn(APIView):
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                "https://kauth.kakao.com/oauth/token",
                headers={"content Type": "application/x-www-form-urlencoded"},
                data={
                    "grant_type": "authorization_code",
                    "client_id": "f4fdce8bfd733f3368f97c47a87266b6",
                    "redirect_uri": "http://127.0.0.1:3000/api/v2/social/kakao",
                    "code": code,
                },
            )
            access_token = access_token.json().get("access_token")
            user_data = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": f"Bearer {access_token}",
                },
            )
            kakao_account = user_data.json().get("kakao_account")
            profile = kakao_account.get("profile")
            try:
                print(kakao_account.get("email"))
                user = User.objects.get(email=kakao_account.get("email"))
                login(request, user)
                print(1)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User.objects.create(
                    username=user_data.json().get("id"),
                    name=profile.get("nickname"),
                    avatar=profile.get("profile_image_url"),
                    email=kakao_account.get("email"),
                )
                user.set_unusable_password()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("KakaoLogIn POST() Error >>>: ", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
