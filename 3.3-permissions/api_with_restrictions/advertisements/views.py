from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter

from .permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters
from .serializers import AdvertisementSerializer
from .models import Advertisement

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
    
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(),IsOwnerOrReadOnly()]
        return []
