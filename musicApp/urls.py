from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import SongsAPIView, SongsDetails

app_name = "musicApp"

# urlpatterns = [
#     path('', views.SongsDetails, name='index'),
# ]

urlpatterns = [
    path('songs/', SongsAPIView.as_view()),
    path('songs/<int:pk>', SongsDetails.as_view()),
   
]


# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]