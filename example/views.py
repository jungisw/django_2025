from http.client import responses
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from rest_framework import status

from example.serializers import PostSerializer

@api_view(['GET','POST'])
def blogAPI(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        postSerializer = PostSerializer(posts, many=True)
        return Response(postSerializer.data, status=status.HTTP_200_OK)
    else:
        postSerializer = PostSerializer(data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data, status=status.HTTP_201_CREATED)

    return Response(postSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['GET','DELETE','PUT'])
def postAPI(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        postSerializer = PostSerializer(post)
        return Response(postSerializer.data,
                        status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response('delete completed', status=status.HTTP_204_NO_CONTENT)
    else:
        #post = Post.objects.get(pk=pk)
        post = get_object_or_404(Post,pk=pk)
        postSerializer = PostSerializer(post,data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data,
                            status=status.HTTP_200_OK)
    return Response(postSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


def example(request):
    return render(request,
                  'example/example.html')
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")