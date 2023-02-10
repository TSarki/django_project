from django.urls import path
import debug_toolbar

from school.views import students_list
from django.urls import path, include

urlpatterns = [
    path('', students_list, name='students'),
    path('__debug__/', include(debug_toolbar.urls)),
]
