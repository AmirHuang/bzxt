from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .models import exploEvi, exploEviFile, exploEviPeak, exploChEvi
from .serializers import exploEviDetailSerializer, exploEviSerializer, exploEviFileDetailSerializer
from .serializers import exploEviFileSerializer, exploEviPeakSerializer
from .serializers import exploChEviSerializer, devCompEviFileDetailSerializer
from .serializers import devCompEviFileSerializer
from .models import devCompEviFile
from .models import devCompEviPeak, devCompChEvi
from .serializers import devCompEviPeakSerializer, devCompChEviSerializer

from utils.permissions import IsOwnerOrReadOnly


class exploEviViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    list:
        获取
    create:
        添加
    update:
        更新
    delete:
        删除
    """
    queryset = exploEvi.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("caseID", "evidenceID", " picDescrip", "note")
    ordering_fields = ("evidenceID", "inputDate",)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return exploEviDetailSerializer
        return exploEviSerializer


class exploEviFileViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = exploEviFile.objects.all()

    # serializer_class = exploEviFileSerializer
    def get_serializer_class(self):
        if self.action == "retrieve":
            return exploEviFileDetailSerializer
        return exploEviFileSerializer

    def handleFile(self, file):
        pass

    def perform_create(self, serializer):
        file = serializer.save()
        file = self.handleFile(file)
        return file


class exploEviPeakViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = exploEviPeak.objects.all()
    serializer_class = exploEviPeakSerializer


class exploChEviViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = exploChEvi.objects.all()
    serializer_class = exploChEviSerializer


class devCompEviFileViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = devCompEviFile.objects.all()

    # serializer_class = devCompEviFileSerializer
    def get_serializer_class(self):
        if self.action == "retrieve":
            return devCompEviFileDetailSerializer
        return devCompEviFileSerializer

    def handleFile(self, file):
        pass

    def perform_update(self, serializer):
        file = serializer.save()
        file = self.handleFile(file)
        return file

    def perform_create(self, serializer):
        file = serializer.save()
        file = self.handleFile(file)
        return file


class devCompEviPeakViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = devCompEviPeak.objects.all()
    serializer_class = devCompEviPeakSerializer


class devCompChEviViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = devCompChEvi.objects.all()
    serializer_class = devCompChEviSerializer


