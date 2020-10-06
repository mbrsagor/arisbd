angular
    .module("Base")
    .controller("baseController", function (
        $scope,
        profileResource,
        UserListResource,
        ActiveprofileResource) {
        "use strict";

        $scope.pageTitle = "Base";

        profileResource.query().$promise.then(function (response) {
            $scope.users = response;
        });

        UserListResource.query().$promise.then(function (response) {
            $scope.auth_user = response;
        });

        ActiveprofileResource.my_profile().$promise.then(function (response) {
            $scope.profile = response;
        });
    });
