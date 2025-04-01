from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path("registerUser/", registerUser, name="registerUser"),
    path("getUser/<int:id>/", getUser, name="getUser"),
    path("getUsers/", getUsers, name="getUsers"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("getSnippet/<int:id>/",getSnippet, name="getSnippet"),
    path("getSnippets/", getSnippets, name="getSnippets"),

    path("addSnippet/", addSnippet, name="addSnippet"),

    path("updateSnippet/<int:id>/", updateSnippet, name="updateSnippet"),
    path("deleteSnippet/<int:id>/", deleteSnippet, name="deleteSnippet"),
]
