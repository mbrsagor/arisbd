angular
  .module("User")
  .controller("userController", function(
    $scope,
    toastr,
    UserListResource,
    ActiveprofileResource,
    CreateUserResource) {
    "use strict";

    $scope.pageTitle = "Users";
    $scope.saving = false;
    $scope.user = {};
    
    $scope.addModalbutton = function () {
      $scope.user = null;
    }

    // Display list of user
    UserListResource.query().$promise.then(function(response) {
      $scope.users = response;
    });

    // Create new user
    $scope.addUser = function() {
      $scope.saving = true;
      var resouceMethod = $scope.user.id ? UserListResource.update : CreateUserResource.save;
      resouceMethod($scope.user).$promise
        .then(function () {
          $scope.saving = false;
          toastr.success('Successfully saved the user.');
          $scope.user = null;
        }, function () {
            $scope.saving = false;
            toastr.error('Something went wrong while saving user!');
        });
      $(".modal").modal("hide");
    };

    $scope.updateUser = function (user) {
      $scope.user = user;
    }

    $scope.deleteUser = function (user) {
      swal( {
        title: "Are you sure?",
        text: "user will be deleted permanently.",
        icon: "warning",
        buttons: true,
        dangerMode: true
      }).then(willDelete => {
        if (willDelete) {
          UserListResource.delete({id: user.id}).$promise.then(
            function () {
              toastr.success("User has been deleted.");
            },function () {
              toastr.error("Something went wrong while deleting user!");
            });
        }
      });
    }

    ActiveprofileResource.my_profile().$promise.then(function(response) {
      $scope.profile = response;
    });
  });
