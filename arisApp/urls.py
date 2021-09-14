from django.urls import pathfrom .views import (    UserProfileView, ProfileDetailsView, UserCreateListView,    ProductAPIView, ProductUpdateDeleteApiView, UserDetailsDeleteView,    ListOfAgent, ListOfMember, ProfileView, IsSuperUser, CategoryAPIView)urlpatterns = [    path('active-profile', ProfileView.as_view()),    path('profile', UserProfileView.as_view()),    path('profile/<int:id>', ProfileDetailsView.as_view()),    path('user', UserCreateListView.as_view()),    path('user/<int:id>', UserDetailsDeleteView.as_view()),    path('product', ProductAPIView.as_view()),    path('product/<int:id>', ProductUpdateDeleteApiView.as_view()),    path('category/', CategoryAPIView.as_view()),    path('create-category/', CategoryAPIView.as_view()),    path('category-update/<int:id>', CategoryAPIView.as_view()),    path('category-delete/<int:id>', CategoryAPIView.as_view()),    path('list_of_agent', ListOfAgent.as_view()),    path('list_of_member', ListOfMember.as_view()),    path('is_superuser', IsSuperUser.as_view()),]