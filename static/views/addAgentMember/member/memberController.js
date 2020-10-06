angular.module('Profile')
    .controller('memberController', function (
        $scope,
        $http,
        toastr,
        ActiveprofileResource,
        profileResource) {

        $scope.pageTitle = "Member";

        $http.get('/api/list_of_member')
            .then(function (response) {
                $scope.members = response.data;
            });

        $scope.deleteMember = function (member) {
            swal({
                title: "Are you sure?",
                text: "Member will be deleted permanently.",
                icon: "warning",
                buttons: true,
                dangerMode: true
            }).then(willDelete => {
                if (willDelete) {
                    profileResource.delete({id: member.id}).$promise.then(
                        function () {
                            toastr.success("Member has been deleted.");
                        },
                        function () {
                            toastr.error("Something went wrong while deleting member!");
                        }
                    );
                }
            });
        };

        ActiveprofileResource.my_profile().$promise.then(function (response) {
            $scope.profile = response;
        });
    });