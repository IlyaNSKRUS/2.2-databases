from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student


def students_list(request):
    template = 'school/students_list.html'
    students_all = Student.objects.prefetch_related('teachers').all()
    context = {
        'object_list': students_all,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
