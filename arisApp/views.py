from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User

from .models import Profile, Product
from .serializers import ProfileSerializer, UserSerializer, ProductSerializer
from .permissions import AuthorAllStaffAllButEditOrReadOnly


class ProfileView(APIView):

    def get(self, request):
        queryset = Profile.objects.get(id=self.request.user.id)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)


class UserProfileView(APIView):

    def get(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProfileDetailsView(APIView):

    def get(self, request, id):
        queryset = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(queryset).data
        return Response(serializer)

    def put(self, request, id):
        queryset = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = get_object_or_404(Profile, id=id)
        queryset.delete()
        return Response(HTTP_400_BAD_REQUEST)


class UserCreateListView(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailsDeleteView(APIView):

    def get(self, request, id):
        queryset = get_object_or_404(User, id=id)
        serializer = UserSerializer(queryset).data
        return Response(serializer)

    def put(self, request, id):
        queryset = get_object_or_404(User, id=id)
        serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = get_object_or_404(User, id=id)
        queryset.delete()
        return Response(HTTP_400_BAD_REQUEST)


class ProductAPIView(APIView):

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProductUpdateDeleteApiView(APIView):

    def get(self, request, id):
        queryset = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(queryset).data
        return Response(serializer)

    def put(self, request, id):
        queryset = get_object_or_404(Product, id=id)
        serialize = ProductSerializer(queryset, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=HTTP_200_OK)
        return Response(serialize.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = get_object_or_404(Product, id=id)
        queryset.delete()
        return Response(HTTP_400_BAD_REQUEST)


class ListOfAgent(APIView):

    def get(self, request):
        queryset = Profile.objects.filter(user_type='agent')
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class ListOfMember(APIView):

    def get(self, request):
        queryset = Profile.objects.filter(user_type='member')
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class IsSuperUser(APIView):

    def get(self, request):
        queryset = User.objects.filter(is_superuser=True)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
