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
        self.volume.up_increment()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)

    @list_route(methods=['GET'])
    def down(self, request):
        self.volume.down_increment()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)

    @list_route(methods=['GET'])
    def mute(self, request):
        self.volume.mute()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)


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
