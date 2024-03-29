from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from django.contrib.auth.models import User

from .models import Profile, Product, Category
from .serializers import ProfileSerializer, UserSerializer, ProductSerializer, CategorySerializer
from .permissions import AuthorAllStaffAllButEditOrReadOnly
from utils.custom_responses import prepare_success_response, prepare_error_response, prepare_create_success_response
from utils.category_valiidation import validate_category_data


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


class CategoryAPIView(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.filter(id=pk).first()
        except Category.DoesNotExist:
            return None

    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(prepare_success_response(serializer.data), status=HTTP_200_OK)
        except Exception as e:
            return Response(
                prepare_error_response(str(e)),
                status=HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        validate_error = validate_category_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        validate_error = validate_category_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=HTTP_400_BAD_REQUEST)
        category = Category.objects.get(pk=id).first()
        if category is not None:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=HTTP_400_BAD_REQUEST)
        else:
            return Response(prepare_error_response("No data found for this ID"), status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            category.delete()
            return Response(prepare_success_response("Data deleted successfully"), status=HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=HTTP_400_BAD_REQUEST)


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
