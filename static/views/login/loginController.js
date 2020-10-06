app.controller("loginController", function(
  $scope,
  $location,
  $http,
  $window,
  toastr,
  $localStorage) {
  $scope.userLoginButton = function() {
    $http({
      method: "post",
      url: "api/auth/login/",
      data: {username: $scope.username, password: $scope.password}
    }).then(
      function successCallback(response) {
        $localStorage.token = response.data.key;
        $location.path("app/dashboard");
      },
      function errorCallback(response) {
        var status = response.status;
        if (status === 400) {
          $scope.message = "Username or password is incorrect!";
          toastr.error("Please contact admin or try again later");
        } else if (status >= 500) {
          toastr.error("Someting went wrong, Please contact administrator.");
        }
      }
    );
  };

  // Logout function
  $scope.logout = function() {
    $http({
      method: 'post',
      url: 'api/auth/logout/',
      data: {username: $scope.username, password: $scope.password}
    }).then(function successCallback(response){
      $window.localStorage.removeItem( "jwtToken" );
      $location.path("/");
    })
  };
});
