from django.urls import path
from app1 import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin_panel/',views.adminpage,name="admin"),
    path('', views.loginpage,name="login"),
    path('registration/', views.signuppage,name="signup"),
    path('home/', views.homepage,name="home"),
    path('logout/',views.logoutPage,name="logout"),
    path('edit/<int:id>',views.editpage,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('add_user/', views.add_user,name="add_user"),

]