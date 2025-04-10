from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://fictional-barnacle-jp7pp64v4wcjq5p-8000.app.github.dev"
    })