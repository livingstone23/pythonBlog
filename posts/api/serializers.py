from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_at']

        ''' 
        #Permite definir todo, pero si el modelo cambia o no queremos presentar todo deberemmos realizar ajuste.
        fields = ['title', 'description', 'created_at']
        '''