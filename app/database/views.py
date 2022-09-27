from django.shortcuts import render

# Create your views here.


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from database.models import Movie, Director, Comic_story, Comic_writer, Comic_illustrator, comic_inspirations
from database.serializers import DatabaseSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Movie.objects.all()
    return render(request, "database/index.html", {'database': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'database/index.html'

    def get(self, request):
        queryset = Movie.objects.all()
        return Response({'database': queryset})


class list_all_movies(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'database/movie_list.html'

    def get(self, request):
        queryset = Movie.objects.all()
        return Response({'database': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            movies = movies.filter(title__icontains=title)

        movies_serializer = DatabaseSerializer(movies, many=True)
        return JsonResponse(movies_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = DatabaseSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Movie.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Movies were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse({'message': 'The movie does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        movie_serializer = DatabaseSerializer(movie)
        return JsonResponse(movie_serializer.data)

    elif request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie_serializer = DatabaseSerializer(movie, data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data)
        return JsonResponse(movie_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return JsonResponse({'message': 'Movie was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_list_published(request):
    movies = Movie.objects.filter(published=True)

    if request.method == 'GET':
        movie_serializer = DatabaseSerializer(movies, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
