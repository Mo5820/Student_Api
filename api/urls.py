from django.urls import path
from . views import(StudentListApiView,StudentDetailApiView,StudentUpdateApiView,StudentDestroyApiView,StudentCreateApiView)

app_name='api'
urlpatterns = [
    path('list/',StudentListApiView.as_view(),name='Studentlistview' ),
    # path('list/<int:pk>/',StudentDetailApiView.as_view(),name='Studentdetailview' ),
    path('list/<str:name>/',StudentDetailApiView.as_view(),name='Studentdetailview'),
    path('list/<str:name>/edit',StudentUpdateApiView.as_view(),name='StudentUpdateApiView'),
    path('list/<str:name>/delete',StudentDestroyApiView.as_view(),name='StudentDestroyApiView'),
    path('list/create',StudentCreateApiView.as_view(),name='StudentCreateApiView'),
]
