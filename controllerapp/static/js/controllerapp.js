var app = angular.module('controllerApp', []);

app.controller('volumeController', ['$scope', '$http', function ($scope, $http) {
    $scope.volumeUp = function () {
        $http.get('/api/volume/up/').then(
            function(response) {
                $scope.notification_text = "Volume: " + response.data.new_volume + "%"
            }
        );
    };
    $scope.volumeDown = function () {
        $http.get('/api/volume/down/').then(
            function(response) {
                $scope.notification_text = "Volume: " + response.data.new_volume + "%"
            }
        );
    };
    $scope.volumeMute = function () {
        $http.get('/api/volume/toggle_mute/').then(
            function(response) {
                if (response.data.muted) {
                    $scope.notification_text = "Muted!";
                } else {
                    $scope.notification_text = "Not Muted";
                }
            }
        );
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
