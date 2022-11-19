from .models import Blog
from .serializers import BlogSerialiser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Blog.objects.all()
    serializer_class = BlogSerialiser

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)