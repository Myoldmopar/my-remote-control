from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render

from controls.volume import VolumeController
from controls.media import MediaController


def control_page(request):
    return render(request, 'controllerapp/controls.html', {})


class VolumeViewSet(viewsets.GenericViewSet):
    def __init__(self):
        super(VolumeViewSet, self).__init__()
        self.volume = VolumeController()

    @list_route(methods=['GET'])
    def up(self, request):
        response = self.volume.up_increment()
        if response.success:
            return JsonResponse(response.to_dict(), status=status.HTTP_200_OK)
        else:
            return JsonResponse(response.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @list_route(methods=['GET'])
    def down(self, request):
        response = self.volume.down_increment()
        if response.success:
            return JsonResponse(response.to_dict(), status=status.HTTP_200_OK)
        else:
            return JsonResponse(response.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @list_route(methods=['GET'])
    def toggle_mute(self, request):
        response = self.volume.set_mute_status()
        if response.success:
            return JsonResponse(response.to_dict(), status=status.HTTP_200_OK)
        else:
            return JsonResponse(response.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MediaViewSet(viewsets.GenericViewSet):
    def __init__(self):
        super(MediaViewSet, self).__init__()
        self.media = MediaController()

    @list_route(methods=['GET'])
    def play_pause(self, request):
        response = self.media.play_pause()
        if response.success:
            return JsonResponse(response.to_dict(), status=status.HTTP_200_OK)
        else:
            return JsonResponse(response.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @list_route(methods=['GET'])
    def next_song(self, request):
        response = self.media.next_song()
        if response.success:
            return JsonResponse(response.to_dict(), status=status.HTTP_200_OK)
        else:
            return JsonResponse(response.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
