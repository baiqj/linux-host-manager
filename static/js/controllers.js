'use strict';

/* Controllers */

var cloudAppControllers = angular.module('cloudAppControllers', ['ui.bootstrap']);

cloudAppControllers.controller('loginCtrl', ['$scope',  'Request',
  function($scope, Request) {
  
	/* code section */
	 //$scope.bookname = 'bookname-value';
  }]);

cloudAppControllers.controller('mainCtrl', ['$rootScope','$scope',
  function($rootScope,$scope){
	/* custom code section */
  $rootScope.htmlTitle = "首页";
  }]);

cloudAppControllers.controller('OneKeyCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);

cloudAppControllers.controller('siteCreateCtrl', ['$rootScope','$scope','$location',
  function($rootScope,$scope,$location) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";

  $scope.phpversion = 0;
  $scope.mysqlversion = 0;
  $scope.apacheversion = 0;
  $scope.charsetOpt = "utf-8";

  $scope.submit = function(){
    $scope.isClick = !$scope.isClick;
    $location.path('/sites/creating')
  }
  }]);

cloudAppControllers.controller('siteCreatingCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);

cloudAppControllers.controller('lampCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);

cloudAppControllers.controller('lampCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);