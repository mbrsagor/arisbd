angular.module("arisApp.services", []);
angular.module("arisApp.directives", []);
angular.module("User", []);
angular.module("Base", []);
angular.module("Profile", []);
angular.module("Product", []);
angular.module("addAgentMemberController", []);
angular.module("profileUpdateController", []);

var app = angular.module("arisApp", [
  "arisApp.services",
  "arisApp.directives",
  "Profile",
  "Base",
  "Product",
  'addAgentMemberController',
  'profileUpdateController',
  "User",
  "ui.router",
  "ui.bootstrap",
  "ngResource",
  "ngStorage",
  "toastr"
]);

app.config(["$stateProvider", "$urlRouterProvider", "$locationProvider", "$httpProvider",
  function($stateProvider, $urlRouterProvider, $locationProvider, $httpProvider) {
    "use strict";

    // csrf token
    $httpProvider.defaults.xsrfCookieName = "csrftoken";
    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";

    // html5 mode enable
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });

    $httpProvider.interceptors.push("AuthInterceptor");

    $stateProvider
      .state("login", {
        url: "/",
        templateUrl: "static/views/login/login.html",
        controller: "loginController"
      })
      .state("app", {
        abstract: true,
        url: "/app",
        templateUrl: "static/views/base/base.html",
        controller: "baseController"
      })
      .state("app.dashboard", {
        url: "/dashboard",
        views: {
          "main-pane": {
            templateUrl: "static/views/dashboard/dashboard.html",
            controller: "dashboardController"
          }
        }
      })
      .state("app.user", {
        url: "/user",
        views: {
          "main-pane": {
            templateUrl: "static/views/user/user.html",
            controller: "userController"
          }
        }
      })
      .state("app.product", {
        url: "/product",
        views: {
          "main-pane": {
            templateUrl: "static/views/product/product.html",
            controller: "productController"
          }
        }
      })
      .state("app.addAgentMember", {
        url: "/add_agent_or_member",
        views: {
          "main-pane": {
            templateUrl: "static/views/addAgentMember/addAgentMember.html",
            controller: "addAgentMemberController"
          }
        }
      })
      .state("app.profileUpdate", {
        url: "/profile_update",
        views: {
          "main-pane": {
            templateUrl: "static/views/profile/profileUpdate.html",
            controller: "profileUpdateController"
          }
        }
      })
      .state("app.agent", {
        url: "/agent-list",
        views: {
          "main-pane": {
            templateUrl: "static/views/addAgentMember/agent/agent.html",
            controller: "agentController"
          }
        }
      })
      .state("app.member", {
        url: "/member-list",
        views: {
          "main-pane": {
            templateUrl: "static/views/addAgentMember/member/member.html",
            controller: "memberController"
          }
        }
      })
      .state("app.profile", {
        url: "/profile",
        views: {
          "main-pane": {
            templateUrl: "static/views/profile/profile.html",
            controller: "profileController"
          }
        }
      })
      .state("error", {
        url: "/error",
        templateUrl: "static/views/error/error.html"
      });

    $urlRouterProvider.otherwise("/error");
  }
]);

app.run(function($rootScope, $state, $stateParams) {
  $rootScope.$state = $state;
  $rootScope.$stateParams = $stateParams;
});
