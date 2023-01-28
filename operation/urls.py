from django.contrib import admin
from django.urls import path,include
from operation import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addrecord,name="addone"),
    path('success/',views.success),
    path('delete/<int:id>/',views.delete, name="deleteone"),
    path('<int:id>',views.editone,name="editone"),
    path('templatetest',views.test),
]
