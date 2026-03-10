from django.http import HttpResponse

def health_check(request):
    return HttpResponse("Hugging Face Space is Online! Diagnostics OK.", content_type="text/plain")
