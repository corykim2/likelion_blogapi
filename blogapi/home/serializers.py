from rest_framework import serializers
from .models import Blog

class BlogSerialiser(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']