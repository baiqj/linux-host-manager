'use strict';

/* Controllers */

var cloudAppControllers = angular.module('cloudAppControllers', ['ui.bootstrap']);

cloudAppControllers.controller('loginCtrl', ['$scope',  'Request',
  function($scope, Request) {
  
	/* code section */
	 //$scope.bookname = 'bookname-value';
  }]);

cloudAppControllers.controller('mainCtrl', ['$rootScope','$scope','$timeout',
  function($rootScope,$scope,$timeout){
	/* custom code section */
  $rootScope.htmlTitle = "首页";

  // get system base information from server
  $scope.sys_info = {os: 'RedHat', currenttime: 1,run_time: 0,sys_Load: '56%', CPU:'core i5',Memory:'4096M',IP:'211.45.233.14'};

  $scope.Ctrl = function(){
    //custome code about your function
    var myDate = new Date();
    $scope.sys_info.currenttime=myDate.toLocaleTimeString();
    // end your function codes

    var countUp = function() {
      // custom code about your function
        var myDate = new Date();
        $scope.sys_info.currenttime=myDate.toLocaleTimeString();
      // end your function code
        $timeout(countUp, 1000);
    }

    $timeout(countUp, 1000);
    }
    $scope.Ctrl();

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

  //from server get the version information and set the variable in the below
  $scope.http_versions  = ['1.2.3','3.4.5','5.1.6'];
  $scope.mysql_versions = ['1.2.3','3.4.5','5.1.6'];
  $scope.php_versions   = ['1.2.3','3.4.5','5.1.6'];

  $scope.http_version = 0;
  $scope.mysql_version = 0;
  $scope.php_version = 0;
  $scope.charsetOpt = "utf-8";

  $scope.submit = function(){
    console.log('domain=' + $scope.domainName 
      + '\nphpversion=' + $scope.php_version  
      + '\nhttpversion=' + $scope.http_version
      + '\nmysqlversion=' + $scope.mysql_version);
    // send install infomation to server
    // -----------send a request to server and your code here!!!-------------
    // then redict to 'creating page'
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

cloudAppControllers.controller('lnmpCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);