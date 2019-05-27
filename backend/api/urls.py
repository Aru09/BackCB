from django.urls import path
from api.views import auth, generic


urlpatterns = [
    path('users/', auth.UserList.as_view()),
    path('login/', auth.login),
    path('logout/', auth.logout),
    #path('reviews', FBV.ReviewList.as_view() ),
    #path('companies/', FBV.CompanyList.as_view())
]