from django.http import JsonResponse
from .models import Image
from .serializers import ImagesSerializer
from rest_framework.decorators import api_view , permission_classes
import os
from rest_framework.permissions import IsAuthenticated
import base64
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def images_list(request):
    if request.method == 'GET':
        images = Image.objects.filter(user=request.user)
        serializer = ImagesSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_img(request):
    if request.method == 'POST':
        data = request.data
        data = data.copy()
        data.__setitem__('user', request.user.id)
        serializer = ImagesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_img(request, id):
    if request.method == 'GET':
        try:
            image = Image.objects.get(pk=id, user=request.user.id)
        except Image.DoesNotExist:
            return JsonResponse({'message': 'The image does not exist'}, status=404)
        serializer = ImagesSerializer(image)
        with open(image.image.path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            encoded_string = encoded_string.decode('utf-8')
            serializerData = serializer.data
            serializerData["image"] = encoded_string
        return JsonResponse(serializerData, safe=False)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_img(request, id):
    try:
        image = Image.objects.get(pk=id, user=request.user.id)
    except Image.DoesNotExist:
        return JsonResponse({'message': 'The image does not exist'}, status=404)
    if len(image.image.path) > 0:
        os.remove(image.image.path)
    image.delete()
    return JsonResponse({'message': 'Image was deleted successfully!'}, status=204)