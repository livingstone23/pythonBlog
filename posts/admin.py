from django.contrib import admin


from posts.models import  Post

#registramos el modelo al panel administrador
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']


