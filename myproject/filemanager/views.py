from django.http import JsonResponse
from .models import File

def upload_file(request):
    if request.method == 'POST':
        title = request.POST['title']
        # Handle file upload here
        File.objects.create(title=title)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
