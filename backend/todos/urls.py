from rest_framework.routers import DefaultRouter

from todos.views import TodoViewSet

app_name = 'todos'

router = DefaultRouter()
router.register(r'', TodoViewSet)

urlpatterns = [] + router.urls
