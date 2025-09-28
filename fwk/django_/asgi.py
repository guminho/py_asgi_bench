from django.conf import settings
from django.core.asgi import get_asgi_application

settings.configure(
    SECRET_KEY="nosecret",
    DEBUG=False,
    ROOT_URLCONF="django_.views",
)

app = get_asgi_application()
