from sports.models import Sport
from rest_framework import generics

from .serializers import SportSerializer


class SportRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk' # url(r'?P<pk>\d+')
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    def get_queryset(self):
        return Sport.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Sport.objects.get(pk=pk)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class SportDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SportSerializer
#
#     def get_queryset(self):
#         return Sport.objects.all().filter(user=self.request.user)
