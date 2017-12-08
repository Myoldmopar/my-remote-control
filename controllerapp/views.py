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
        if response['success']:
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @list_route(methods=['GET'])
    def down(self, request):
        response = self.volume.down_increment()
        if response['success']:
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @list_route(methods=['GET'])
    def toggle_mute(self, request):
        response = self.volume.toggle_mute()
        if response['success']:
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MediaViewSet(viewsets.GenericViewSet):

    def __init__(self):
        super(MediaViewSet, self).__init__()
        self.media = MediaController()

    @list_route(methods=['GET'])
    def play_pause(self, request):
        self.media.play_pause()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)

    @list_route(methods=['GET'])
    def next_song(self, request):
        self.media.next_song()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)

    @list_route(methods=['GET'])
    def open_pithos(self, request):
        self.media.open_pithos()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)

    @list_route(methods=['GET'])
    def close_pithos(self, request):
        self.media.close_pithos()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)
