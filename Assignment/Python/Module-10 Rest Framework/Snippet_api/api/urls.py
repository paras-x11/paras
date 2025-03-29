from django.urls import path
from api.views import *

urlpatterns = [
    path("getSnippets/",snippets, name="getSnippets"),
    path("addSnippet/", snippets, name="addSnippet"),
    path("updateSnippet/<int:id>/", modifySnippet, name="updateSnippet"),
    path("deleteSnippet/<int:id>/", modifySnippet, name="deleteStudent"),
]
