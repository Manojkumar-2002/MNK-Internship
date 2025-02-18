from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey(Blogs, related_name="comments", on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)  
    text = models.TextField()


    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"
