angular.module('Profile')
  .controller('dashboardController', function (
    $scope,
    profileResource,
    productResource,
    $http) {

    $scope.pageTitle = "Welcome to ArisBD";
    $scope.pageSubTitle = "Online MNL sytem web application";

    profileResource.query().$promise
      .then(function (response) {
        $scope.profile = response;
      });
    
    productResource.query().$promise
      .then(function (response) {
        $scope.products = response;
      });
      
    $http.get('/api/user')
      .then(function (response) {
        $scope.users = response.data;
      });
      
    $http.get('/api/list_of_agent')
      .then(function (response) {
        $scope.agent = response.data;
      });
      
    $http.get('/api/list_of_member')
      .then(function (response) {
        $scope.member = response.data;
      });
});
