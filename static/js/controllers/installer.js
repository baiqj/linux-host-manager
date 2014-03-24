
/**
 * Created by pengfei on 3/22/14.
 * deprecated, NOT in use!
 * remove later!
 */

var installControllers = angular.module('installControllers', []);

installControllers.controller('InstallCtrl',['$scope','$http',
    function($scope,$http){

        $scope.shell = function(cmd){
            console.log('running shell',cmd);
        }

    }]
);

/*
$scope.listdir = function (currentDir) {
    console.log('[lsitdir]Current DIR is:' + $scope.currentDir);
    $http({method: 'POST',
        url: '/operation/file',
        data: {
            'action': 'listdir',
            'path': currentDir,
            'showhidden': false,
            'remember': false}
    }).
        success(function (data, status, headers, config) {
            console.log('Get the data:' + data);
            if (data.code == 0) {
                $scope.items = data.data;
                console.log("Get /root info success.");
            } else {
                console.log('Get /root info failed.');
            }
        }).
        error(function (data, status, headers, config) {
            console.log('failed get "/root" dir lists!');
        });
}
*/