var app = angular.module('controllerApp', []);

app.controller('volumeController', ['$scope', '$http', function ($scope, $http) {
        $scope.volumeUp = function () {
            $http.get('/api/volume/up/');
        };
        $scope.volumeDown = function () {
            $http.get('/api/volume/down/');
        };
        $scope.volumeMute = function () {
            $http.get('/api/volume/toggle_mute/');
        };
    }]);

app.controller('mediaController', ['$scope', '$http', function ($scope, $http) {
        $scope.playPause = function () {
            $http.get('/api/media/play_pause/');
        };
        $scope.nextSong = function () {
            $http.get('/api/media/next_song/');
        };
        $scope.openPithos = function () {
            $http.get('/api/media/open_pithos/');
        };
        $scope.closePithos = function () {
            $http.get('/api/media/close_pithos/');
        };
    }]);
