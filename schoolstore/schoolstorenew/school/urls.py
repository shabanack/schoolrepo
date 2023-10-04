from django.urls import path
from .import views

app_name='school'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),

    #path('login/', views.loginUser, name="login"),
    #path('logout', views.logoutUser, name="logout"),
    #path('register', views.registerPage, name='register'),
    ]