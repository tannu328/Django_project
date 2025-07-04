from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from djangoapi_app.serializer import UserSerializer
from djangoapi_app.views import USerlogin,Usergenericview
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


# router = routers.DefaultRouter()
# router.register(r'users', Usergenericview)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/<int:id>', Usergenericview.as_view()),  
    path('users/', Usergenericview.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', USerlogin.as_view(),name='post')
    

]
