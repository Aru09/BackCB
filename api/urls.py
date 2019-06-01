from django.urls import path
from api.views import auth, generic
#from api.views import ReviewViewSet
from rest_framework.routers import DefaultRouter

#user_detail = UserViewSet.as_view({'get': 'retrieve'})

router = DefaultRouter()
router.register('', generic.ReviewViewSet, base_name='reviews')
router.register('', generic.CompanyViewSet, base_name='companies')
urlpatterns = router.urls


urlpatterns = [
    path('users/', auth.UserList.as_view()),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('reviews/', generic.ReviewViewSet.as_view({'get':'list',
    'post':'create'})),
    path('companies/', generic.CompanyViewSet.as_view({'get':'list',
    'post':'create'})),

   #path('<int:pk>/', views.DetailTodo.as_view())
    #path('reviews/<int:pk>', generic.ReviewViewSet.as_view({'get':'list'})),

    #path('companies/', FBV.CompanyList.as_view())
]