from django.urls import path
from django.conf import settings
from voiture import views
from django.conf.urls.static import static


urlpatterns = [
    path('all/', views.liste_voitures, name='liste_voitures'),
   path('ajouter/', views.ajouter_voiture, name='ajouter'),
    # Ajoutez d'autres modèles d'URL si nécessaire
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
