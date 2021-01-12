from rest_framework import routers
from autheticate import views
router=routers.DefaultRouter()
router.register('society-admin',views.RegisterViewSet,basename='register')
router.register('login',views.LoginViewSet,basename='login')
router.register('change',views.ChangePassword,basename='change')
router.register('socialmedialogin',views.SocielMedia,basename='socialmedialogin')
urlpatterns=router.urls