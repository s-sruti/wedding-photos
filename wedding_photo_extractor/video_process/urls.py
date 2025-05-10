from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('upload/',views.upload,name='upload'),
    path('process/',views.process,name='process'),
    path('editor/',views.editor,name='editor'),
    path('check_status/',views.check_status),
    path('show_images/',views.show_images),
    path('save_image/',views.save_images),
    path('delete_image/',views.delete_image),
    path('download-zip/', views.zip_directory),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)