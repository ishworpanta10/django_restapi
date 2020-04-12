from django.http import JsonResponse
from django.shortcuts import render

# from third party imports
from rest_framework import mixins

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

from rest_framework import generics


# only get
class PostView(
        mixins.ListModelMixin,
        # mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


# only post
class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# same as listview and post create
class Post(generic.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# get post both
# only get


class PostViewCreate(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class test_view(APIView):

#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         # post = qs.first()
#         # serializer = PostSerializer(post)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save
#             return Response(serializer.data)
#         return Response(serializer.errors)
