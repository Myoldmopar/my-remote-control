var app = angular.module('controllerApp', ['cfp.hotkeys']);

app.controller('remoteControlController', ['$scope', '$http', 'hotkeys', function ($scope, $http, hotkeys) {
    "use strict";
    $scope.notification_text = "Remote Control Initialized";
    $scope.errorResponseHandler = function (error_response) {
        $scope.notification_text = "ERROR: " + error_response.data.message;
    };
    $scope.volumeUp = function () {
        $http.get('/api/volume/up/').then(
            function (response) {
                $scope.notification_text = "Volume: " + response.data.volume + "%";
            },
            $scope.errorResponseHandler
        );
    };
    $scope.volumeDown = function () {
        $http.get('/api/volume/down/').then(
            function (response) {
                $scope.notification_text = "Volume: " + response.data.volume + "%";
            },
            $scope.errorResponseHandler
        );
    };
    $scope.volumeMute = function () {
        $http.get('/api/volume/toggle_mute/').then(
            function (response) {
                if (response.data.muted) {
                    $scope.notification_text = "Muted!";
                } else {
                    $scope.notification_text = "Not Muted";
                }
            },
            $scope.errorResponseHandler
        );
    };
    $scope.playPause = function () {
        $http.get('/api/media/play_pause/').then(
            function (response) {
                $scope.notification_text = "Play/Pause Triggered!";
            },
            $scope.errorResponseHandler
        );
    };
    $scope.nextSong = function () {
        $http.get('/api/media/next_song/').then(
            function (response) {
                $scope.notification_text = "Next Song!";
            },
            $scope.errorResponseHandler
        );
    };
    $scope.openPithos = function () {
        $http.get('/api/media/open_pithos/');
    };
    $scope.closePithos = function () {
        $http.get('/api/media/close_pithos/');
    };
    hotkeys.bindTo($scope)
        .add({
            combo: 'j',
            description: 'Volume Down (Think VI)',
            callback: $scope.volumeDown
        })
        .add({
            combo: 'k',
            description: 'Volume Up (Think VI)',
            callback: $scope.volumeUp
        })
        .add({
            combo: 'm',
            description: 'Mute',
            callback: $scope.volumeMute
        })
        .add({
            combo: 'n',
            description: 'Next Song',
            callback: $scope.nextSong
        })
        .add({
            combo: 'p',
            description: 'Play/Pause',
            callback: $scope.playPause
        });

}]);
