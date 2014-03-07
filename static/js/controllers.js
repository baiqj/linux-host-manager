'use strict';

/* Controllers */

var cloudAppControllers = angular.module('cloudAppControllers', ['ui.bootstrap']);

cloudAppControllers.controller('loginCtrl', ['$scope',  'Request',
  function($scope, Request) {
  
	/* code section */
	var password_strength = function(pwd) {
    var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
    var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
    var enoughRegex = new RegExp("(?=.{6,}).*", "g");
    if (false == enoughRegex.test(pwd)) {
      return '无安全性可言';
    } else if (strongRegex.test(pwd)) {
      return '高';
    } else if (mediumRegex.test(pwd)) {
      return '一般';
    } else {
      return '低';
    }
  };

  $scope.login = function(){
    var result = password_strength($scope.password);
    console.log(result);
  }


  }]);

cloudAppControllers.controller('mainCtrl', ['$rootScope','$scope','$timeout','$http','$location',
  function($rootScope,$scope,$timeout,$http,$location){
	/* custom code section */
  $rootScope.htmlTitle = "首页";

  // get system base information from server
  $scope.sys_info = { os_dist: 'CentOS 6.5 Final', 
                      run_time: '0天3小时40分34秒',
                      cpu_load: '56%',
                      memory_usage:'43%',
                      nic_info:[
                                {
                                  name:'eth0',
                                  upload_rate:'上行120k/s', 
                                  download_rate:'下行160k/s'
                                },
                                {
                                  name:'eth1',
                                  upload_rate:'上行110k/s', 
                                  download_rate:'下行150k/s'
                                }
                              ],
                      disk_info:[ 
                                  { name:'disk1',avai_space:'100G'},
                                  { name:'disk2',avai_space:'120G'}
                                ],
                    };

  $scope.Ctrl = function(){
    //custome code about your function
    var rootUrl = location.pathname.replace(/(\s+)?\/$/, '');
    var rurl = rootUrl + '/query/b*'
    $http({method: 'GET', url: rurl}).
    success(function(data, status, headers, config) {
      console.log(data);
      $scope.sys_info.os_dist = data['server.distribution'];
      $scope.sys_info.run_time = data['server.uptime']['up'];
      $scope.sys_info.cpu_load = Math.round(data['server.cpustat']['total']['used'] / data['server.cpustat']['total']['all'] * 10000) / 100 + '%';;
      $scope.sys_info.memory_usage = data['server.meminfo']['mem_used_rate'];
    }).
    error(function(data, status, headers, config) {
      console.log('failed get base system information');
    });
    // end your function codes
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