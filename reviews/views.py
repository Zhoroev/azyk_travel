from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from tours.models import Tour
from rest_framework.response import Response


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            tour_id = self.kwargs.get('tour_id')
            tour = Tour.objects.get(id=tour_id)
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user, tour=tour)
                return Response(serializer.data)
        return Response('Зарегистрируйтесь чтобы оставить отзыв')

    def update(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(ReviewViewSet, self).update(request, *args, **kwargs)
        return Response("Отказ")

    def partial_update(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(ReviewViewSet, self).partial_update(request, *args, **kwargs)
        return Response("Отказ")

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(ReviewViewSet, self).destroy(request, *args, **kwargs)
        return Response("Отказ")
    # TODO иначе нужно вызвать ошибку