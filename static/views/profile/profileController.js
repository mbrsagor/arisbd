angular
    .module("Profile")
    .controller("profileController", function (
        $scope,
        ActiveprofileResource) {

        "use strict";

        $scope.pageTitle = "My profile";
        ActiveprofileResource.my_profile().$promise.then(function (response) {
            $scope.profile = response;
        });
    });
