angular
    .module("addAgentMemberController")
    .controller("addAgentMemberController", function (
        $scope,
        toastr,
        UserListResource,
        ActiveprofileResource,
        profileResource) {

        "use strict";

        $scope.saving = false;
        $scope.pageTitle = "Add new agent or member";
        $scope.profile = {};

        UserListResource.query().$promise.then(function (response) {
            $scope.users = response;
        });

        $scope.addMember = function () {
            $scope.profile = null;
            $scope.saving = true;
            profileResource.save().$promise.then(function () {
                $scope.saving = false;
                toastr.success('Successfully save the client/member.');
            }, function (errorResponse) {
                if (400 <= errorResponse.status && errorResponse.status < 500) {
                    toastr.error(JSON.stringify(errorResponse.data));
                } else {
                    toastr.error('Something went wrong while save client/member.');
                }
            });
        };

        ActiveprofileResource.my_profile().$promise.then(function (response) {
            $scope.profile = response;
        });
    });
