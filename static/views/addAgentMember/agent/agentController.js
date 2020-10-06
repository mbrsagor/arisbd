angular.module('Profile')
    .controller('agentController', function (
        $scope,
        $http,
        toastr,
        ActiveprofileResource,
        profileResource) {

        $scope.pageTitle = "Agent";

        $http.get('/api/list_of_agent')
            .then(function (response) {
                $scope.agent = response.data;
            });

        $scope.deleteAgent = function (_agent) {
            swal({
                title: "Are you sure?",
                text: "Agent will be deleted permanently.",
                icon: "warning",
                buttons: true,
                dangerMode: true
            }).then(willDelete => {
                if (willDelete) {
                    profileResource.delete({id: _agent.id}).$promise.then(
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
