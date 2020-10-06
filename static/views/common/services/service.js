angular.module('arisApp')
    .service('AuthInterceptor', function ($q, $location) {
        'use strict';

        return {
            'responseError': function (response) {
                if (response.status === 401) {
                    $location.path('/');
                }
                return $q.reject(response);
            }
        };
    });
