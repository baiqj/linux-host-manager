'use strict';

/* App Module */

var cloudApp = angular.module('cloudApp', [
  'ngRoute',
  'cloudAppControllers',
  'cloudAppDirectives',
  'cloudAppServices',
  'ui.bootstrap',
]);

cloudApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/login', {
        templateUrl: 'partials/login.html',
        controller: 'loginCtrl'
      }). 
      when('/main', {
		    templateUrl: 'partials/main.html',
		    controller: 'mainCtrl'
		  }).
      when('/OneKey', {
        templateUrl: 'partials/OneKey/index.html',
        controller: 'OneKeyCtrl'
      }).
      when('/sites/create', {
		    templateUrl: 'partials/OneKey/create.html',
		    controller:	'siteCreateCtrl'
      }).
      when('/sites/creating', {
        templateUrl: 'partials/OneKey/creating.html',
        controller: 'siteCreatingCtrl'
      }).
      when('/sites/lnmp', {
        templateUrl: 'partials/OneKey/lnmp.html',
        controller: 'lnmpCtrl'
      }).
      when('/sites/onekey/lnmp-start', {
        templateUrl: 'partials/OneKey/lnmp-processing.html',
        controller: 'lnmp-installCtrl'
      }).
      when('/sites/lamp', {
        templateUrl: 'partials/OneKey/lamp.html',
        controller: 'lampCtrl'
      }).
      when('/sites/onekey/lamp-start', {
        templateUrl: 'partials/OneKey/lamp-processing.html',
        controller: 'lamp-installCtrl'
      }).
      when('/sites/backup', {
        templateUrl: 'partials/OneKey/backup.html',
        controller: 'backupCtrl'
      }).
      when('/sites/onekey/backup-start', {
        templateUrl: 'partials/OneKey/start-backup.html',
        controller: 'startbackupCtrl'
      }).
      when('/sites/move', {
        templateUrl: 'partials/OneKey/move.html',
        controller: 'moveCtrl'
      }).
      when('/sites/onekey/start-moving', {
        templateUrl: 'partials/OneKey/moving.html',
        controller: 'movingCtrl'
      }).
      when('/sites/optimize', {
            templateUrl: 'partials/OneKey/optimize.html',
            controller: 'optimizeCtrl'
        }).
      when('/logout', {
       templateUrl: 'partials/login.html',
        controller: 'logoutCtrl'
      }).
      otherwise({
        redirectTo: '/login'
      });
  }]).
run(['$rootScope', '$location', '$timeout',function($rootScope, $location,$timeout) {
  $rootScope.isLogin = false;

  // from server get notice itmes and set variable items;
  $rootScope.items = [ {title:"second item",href:"dddd"},{title:"thire item",href:"22222"},{title:"forth item",href:"ddddd"} ];
  $rootScope.itemIndex = $rootScope.items[0];
  $rootScope.items.splice(0,1);


  $rootScope.$on('$locationChangeSuccess', function () {
      var currentPath = $location.path();

      if(currentPath.indexOf("login") >= 0 ){
          console.log('$locationChangeSuccess changed!', new Date());
          $rootScope.isLogin = false;
        } else {
          $rootScope.isLogin = true;
           console.log("1234567");
        } 
      });

  $rootScope.htmlTitle = "首页";

 /* var testTimeout = function(){
    console.log("test for timeout use.");
  }
          <td>step one</td>

  $timeout(function(){
    testTimeout.call();
  },1);*/

}]);