from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    AnswerViewSet,
    ArticleViewSet,
    AttemptViewSet,
    CourseViewSet,
    QuestionViewSet,
    TestViewSet,
    TopicViewSet,
    CourseTopicViewAPI,
    TopicArticleViewAPI
)

router = DefaultRouter()
router.register("courses", CourseViewSet)
router.register("topics", TopicViewSet)
router.register("articles", ArticleViewSet)
router.register("tests", TestViewSet)
router.register("questions", QuestionViewSet)
router.register("answers", AnswerViewSet)
router.register("attempts", AttemptViewSet)


urlpatterns = [
    path("", include(router.urls)),
    re_path("course/(?P<id>.+)/topics", CourseTopicViewAPI.as_view(), name="course_topics"),
    re_path("topic/(?P<id>.+)/articles", TopicArticleViewAPI.as_view(), name="topic_article"),]
