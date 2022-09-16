from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))



class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # preptime = models.ForeignKey(
    #     Preptime,
    #     on_delete=models.CASCADE,
    #     related_name="recipe_posts"
    # )
    # mealtime = models.ForeignKey(
    #     Mealtime,
    #     on_delete=models.CASCADE,
    #     related_name="recipe_posts"
    # )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="recipe_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    serving_size = models.CharField(max_length=30, default=0)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, 
        related_name='recipe_likes', 
        blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"