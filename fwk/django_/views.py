from common import NUM_ROUTE, build_html, build_json
from django.http import HttpResponse, JsonResponse
from django.urls import path

urlpatterns = []


# Add routes to load routing system
# ----------------------------
async def req_ok(request):
    return HttpResponse("ok", content_type="text/plain")


for n in range(NUM_ROUTE):
    urlpatterns.append(path(f"route-{n}", req_ok))


async def html(request, count):
    """Return HTML content."""
    content = await build_html(count)
    return HttpResponse(content)


async def api(request, user, record):
    """Return JSON content."""
    content = await build_json(user, record)
    return JsonResponse(content)


urlpatterns.append(path("html/<int:count>", html))
urlpatterns.append(path("api/users/<int:user>/records/<int:record>", api))
