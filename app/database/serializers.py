from rest_framework import serializers
from database.models import Movie, Director, Comic_story, Comic_writer, Comic_illustrator, comic_inspirations


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'run_time', 'release_date',
                  'viewer_rating', 'critic_rating', 'director_id', 'comic_stories', 'published')

    # class Meta:
    #     model = Director
    #     fields = ('id', 'first_name', 'last_name')

    # class Meta:
    #     model = Comic_story
    #     fields = ('id', 'title', 'description', 'writer_id', 'illustrator_id')
    
    # class Meta:
    #     model = Comic_writer
    #     fields = ('id', 'first_name', 'last_name')
    
    # class Meta: 
    #     model = Comic_illustrator
    #     fields = ('id', 'first_name', 'last_name')
    
    # class Meta:
    #     model = comic_inspirations
    #     fields = ('id', 'movies_id', 'comic_stories_id')