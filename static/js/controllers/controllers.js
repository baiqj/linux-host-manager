var LoginCtrl = [
'$scope', '$rootScope', '$location', 'Module', 'Message', 'Request',
function($scope, $rootScope, $location, Module, Message, Request){
	var module = 'login';
	Module.init(module, '登录');
	$scope.loginText = '登录';
	$scope.showForgetPwdMsg = false;
	$scope.showLoginForm = true;
	$scope.username = '';
	$scope.password = '';

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

	$scope.login = function(rawpwd) {
		$scope.loginText = '登录中...';
		Request.post('/login', {
			username: $scope.username,
			password: rawpwd ? $scope.password : hex_md5($scope.password)
		}, function(data){
			if (data.code >= 0) {
				$scope.showLoginForm = false;
				var path = $rootScope.loginto ? $rootScope.loginto : '/main';
				var section = $rootScope.loginto_section;
				if (data.code == 0) {
					$location.path(path);
					if (section) $location.search('s', section);
				} else {
					// need to check the password strength
					$scope.pwdStrength = password_strength($scope.password);
					if ($scope.pwdStrength != '高') {
						Message.setError(false);
						Message.setWarning(false);
						$('#main').hide();
						$scope.loginMessage = data.msg;
						$scope.loginWarning = true;
					} else {
						$location.path(path);
						if (section) $location.search('s', section);
					}
				}
			} else {
				$scope.loginText = '登录';
			}
		});
	};

	$scope.getCode = function(){
		
	};
}];