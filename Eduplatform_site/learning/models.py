from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from account.models import Teacher
from account.mixins import DateTimeMixinModel


__all__ = {'Course', 'Topic'}


class Course(models.Model, DateTimeMixinModel):
    course_name = models.CharField(max_length=50)
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")

    def __str__(self):
        return f'{self.course_name}'


class Topic(models.Model, DateTimeMixinModel):
    topic_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    numbering = models.IntegerField(validators=[MinValueValidator(0,'Min number value!')])

    class Meta:
        verbose_name = _("course_topic")
        verbose_name_plural = _("course_topics")
        ordering = ['numbering',]

    def __str__(self):
        return f'{self.id}, {self.topic_name}, course - {self.course}'
