from rest_framework import viewsets, generics
from courses.models import Category, Course
from courses import serializers, paginations


class CategoryView(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CourseView(viewsets.ViewSet, generics. ListAPIView):
    queryset = Course.objects.prefetch_related('tags').filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginations.CoursePaginator

    def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)

        return queries

