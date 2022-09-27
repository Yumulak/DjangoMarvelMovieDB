from django.urls import path
from database import views as database_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', database_views.index.as_view(), name='home'),
    path('api/database/', database_views.movie_list),
    path('api/database/<int:pk>/', database_views.movie_detail),
    path('api/database/published/', database_views.movie_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
