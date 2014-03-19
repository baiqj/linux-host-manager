'use strict';

/* Controllers */

var cloudAppControllers = angular.module('cloudAppControllers', ['ui.bootstrap']);

cloudAppControllers.controller('loginCtrl', ['$scope','$http','$location','Message',
  function($scope, $http,$location,Message) {
  
	/* code section */
	var password_strength_check = function(pwd) {
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
    $scope.password_strength = password_strength_check($scope.password);
    console.log($scope.password_strength);
    $http({method: 'POST',
            url: '/login',
            data:{username:$scope.username, password:hex_md5($scope.password)}
        }).
    success(function(data, status, headers, config){
      if(data.code == 0){
        $scope.loginWarning = !$scope.loginWarning;
        //$location.path('/main');
      } else {
        Message.setError(data.msg);
        console.log(data);
      }
    }).
    error(function(data,status,headers,config){
      console.log('failed get base network datas!');
    });
  }

  $scope.isShowForgetPwd = false;
  }]);

cloudAppControllers.controller('logoutCtrl', ['$rootScope','$scope','$timeout','$http','$location',
  function($rootScope,$scope,$timeout,$http,$location){

    $rootScope.isLogin = false;

  $http({method: 'GET', 
            url: '/xsrf'
        }).
    success(function(data, status, headers, config){
      console.log(data);
      $http({method: 'POST',
                url:   '/logout',
                data: {}
            }).
            success(function(data,status,headers,config){
                console.log('logout success.');
                $location.path('/');
            }).
            error(function(data,status,headers,config){
                  console.log('redict to root path failed');
            });
    }).
    error(function(data,status,headers,config){
      console.log('logout failed when getting /xsrf');
    });

}]);

cloudAppControllers.controller('mainCtrl', ['$rootScope','$scope','$timeout','$http','$location',
  function($rootScope,$scope,$timeout,$http,$location){
	/* custom code section */
  $rootScope.htmlTitle = "首页";

  // get system base information from server
  $scope.sys_info = { os_dist:  '', 
                      run_time: '',
                      cpu_load: '',
                      memory_usage:'',
                      disk_info:[]                  
                    };

  $scope.Ctrl = function(){
    //custome code about your function
    var lastData, currentData;
    var rootUrl = location.pathname.replace(/(\s+)?\/$/, '');
    var rurl = rootUrl + '/query/b*'
    $http({method: 'GET', url: rurl}).
    success(function(data, status, headers, config) {
      console.log(data);
      $scope.sys_info.os_dist = data['server.distribution'];
      $scope.sys_info.run_time = data['server.uptime']['up'];
      $scope.sys_info.cpu_load = Math.round(data['server.cpustat']['total']['used'] / data['server.cpustat']['total']['all'] * 10000) / 100 + '%';;
      $scope.sys_info.memory_usage = data['server.meminfo']['mem_used_rate'];
      $scope.sys_info.disk_info = data['server.diskinfo']['partitions'][0]['partitions'];
    }).
    error(function(data, status, headers, config) {
      console.log('failed get base system information');
      if(status == 403)
        $location.path('/');

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

cloudAppControllers.controller('lamp-installCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  $scope.install_process_value = 30;
  
  }]);

cloudAppControllers.controller('lnmpCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);

cloudAppControllers.controller('lnmp-installCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  $scope.install_process_value = 30;
  
  }]);

cloudAppControllers.controller('backupCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);

cloudAppControllers.controller('startbackupCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";

  $scope.select_all = function(){
    $scope.var1 = true;
    $scope.var2 = true;
    $scope.var3 = true;
    $scope.var4 = true;
    $scope.var5 = true;
  }

  $scope.cancel_all = function(){
    $scope.var1 = false;
    $scope.var2 = false;
    $scope.var3 = false;
    $scope.var4 = false;
    $scope.var5 = false;
  }
  }]);

cloudAppControllers.controller('moveCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  
  }]);

cloudAppControllers.controller('movingCtrl', ['$rootScope','$scope',
  function($rootScope,$scope) {
  /* custom code section */
  $rootScope.htmlTitle = "一键通";
  }]);

cloudAppControllers.controller('optimizeCtrl', ['$rootScope','$scope',
    function($rootScope,$scope) {
        /* custom code section */
        $rootScope.htmlTitle = "一键通";

    }]);

cloudAppControllers.controller('settingCtrl', ['$rootScope','$scope','$http','$location','Message',
    function($rootScope,$scope,$http,$location,Message) {
        /* custom code section */
        $rootScope.isLogin = false;
        $rootScope.htmlTitle = "修改密码";

        $scope.updateAuthInfo = function(){
            console.log('start update password');
            $http({method: 'POST',
                url: '/setting/auth',
                data:{username:$scope.username, password:hex_md5($scope.password),passwordc:hex_md5($scope.password_confirm),passwordcheck: $scope.passwordcheck}
            }).
                success(function(data, status, headers, config){
                    if(data.code == 0){
                        console.log("update password success!!");
                        Message.setError(data.msg);
                        //$location.path('/main');

                    } else {
                        console.log(data);
                    }
                }).
                error(function(data,status,headers,config){
                    console.log('failed get to change password!');
                });
        }

    }]);