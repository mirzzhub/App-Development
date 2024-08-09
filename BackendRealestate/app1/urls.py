from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RentalViewSet, UserViewSet, AdminsViewSet, ContactViewSet, IssuesViewSet

router = DefaultRouter()
router.register(r'rentals', RentalViewSet)
router.register(r'users', UserViewSet)
router.register(r'admins', AdminsViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'issues', IssuesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
