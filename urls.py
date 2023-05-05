from django.urls import path
from . import views

app_name ='imsyakiyahapp'

urlpatterns = [
#fbvl
path ('', views.readjadwal),
path ('alamat/<int:id>', views.detailjadwal),
path ('buat/', views.createjadwal),
path ('edit/<int:id>',views.updatejadwal),
path ('hapus/<int:id>', views.deletejadwal),
]