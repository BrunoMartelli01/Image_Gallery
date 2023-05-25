from django.http import JsonResponse
from .models import Image
from .serializers import ImagesSerializer
from rest_framework.decorators import api_view , permission_classes
import os
from rest_framework.permissions import AllowAny
@api_view(['GET', 'POST'])
def images_list(request):
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImagesSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = request.data
        serializer = ImagesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_image(request, id):
    try:
        image = Image.objects.get(pk=id)
    except Image.DoesNotExist:
        return JsonResponse({'message': 'The image does not exist'}, status=404)
    if len(image.image.path) > 0:
        os.remove(image.image.path)
    image.delete()
    return JsonResponse({'message': 'Image was deleted successfully!'}, status=204)