from doctest import Example
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView 
# Create your views here.
from .models import *
from .serializers import ExampleSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from django.views.generic import DetailView, ListView, DeleteView
from django.urls import reverse_lazy
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ExampleAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ExampleApiView(ListCreateAPIView):
    queryset = ExampleModel.objects.filter(is_published=True)
    serializer_class = ExampleSerializer
    pagination_class = ExampleAPIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    # def get(self, request,  *args, **kwargs):
    #     return Response(list(self.queryset.values()))

    # def post(self, request):
    #     try:
    #         for d in request:
    #             post_new = ExampleModel.objects.create(
    #                 title=d['title'],
    #                 content=d['content']
    #             )
    #     except TypeError:
    #         post_new = ExampleModel.objects.create(
    #             title=request.data['title'],
    #             content=request.data['content']
    #         )
    #     return Response({'post': model_to_dict(post_new)})





class IndexView(ListView):
    model = ExampleModel
    template_name = 'index.html'
    context_object_name = 'lst'


class InfoExample(DetailView):
    model = ExampleModel
    template_name = 'detail.html'
    context_object_name = 'dt'

class DeleteView(DestroyAPIView):
    queryset = ExampleModel.objects.all()
    template_name = 'delete.html'
    context_object_name = 'delete_post'
    success_url = reverse_lazy('main')
    

class ExampleUpdateView(ListModelMixin ,UpdateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer

    def get(self, request, pk,   *args, **kwargs):
        lst = ExampleModel.objects.filter(pk=pk)
        return Response({'Update': ExampleSerializer(lst, many=True).data})


class AllExample(RetrieveUpdateDestroyAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer


class GetOnly(ListCreateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer

    def get(self, request, pk,   *args, **kwargs):
        l = ExampleModel.objects.get(pk=pk)
        return Response({'GetOnly': ExampleSerializer(l).data})
