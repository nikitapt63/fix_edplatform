from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions

from .models import Answer, Article, Attempt, Course, Question, Test, Topic
from .serializers import (
    AnswerSerializer,
    ArticleSerializer,
    AttemptSerializer,
    CourseSerializer,
    QuestionSerializer,
    TestSerializer,
    TopicSerializer,
)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AttemptViewSet(ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer


class CourseTopicViewAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def get_queryset(self):
        course = self.kwargs["id"]
        return Topic.objects.filter(course_id=course)


class TopicArticleViewAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        topic= self.kwargs["id"]
        return Article.objects.filter(topic_id=topic)