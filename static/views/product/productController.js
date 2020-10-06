angular
    .module("Product")
    .controller("productController", function (
        $scope,
        productResource,
        ActiveprofileResource,
        toastr) {

        "use strict";

        $scope.pageTitle = "Product";
        $scope.item = {};
        $scope.saving = false;

        productResource.query().$promise.then(function (response) {
            $scope.products = response;
        });

        $scope.addModalbutton = function () {
            // This function basically use for `update` modal box clear data when user `add new item`
            $scope.item = null;
        };

        $scope.addProduct = function () {
            $scope.saving = true;
            var resourceMethod = $scope.item.id ? productResource.update : productResource.save;
            resourceMethod($scope.item).$promise
                .then(function () {
                    $scope.saving = false;
                    console.log($scope.item);
                    toastr.success('Successfully saved the item.');
                    $scope.item = null;
                }, function () {
                    $scope.saving = false;
                    toastr.error('Something went wrong while saving item!');
                });
            $(".modal").modal("hide");
        };

        $scope.UpdateProduct = function (product) {
            $scope.item = product;
        };

        $scope.deleteProduct = function (product) {
            swal({
                title: "Are you sure?",
                text: "Product will be deleted permanently.",
                icon: "warning",
                buttons: true,
                dangerMode: true
            }).then(willDelete => {
                if (willDelete) {
                    productResource.delete({id: product.id}).$promise.then(
                        function () {
                            toastr.success("Product has been deleted.");
                        },
                        function () {
                            toastr.error("Something went wrong while deleting product!");
                        }
                    );
                }
            });
        };

        ActiveprofileResource.my_profile().$promise.then(function (response) {
            $scope.profile = response;
        });
    });
