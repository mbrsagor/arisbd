angular.module('arisApp.services')
    .factory('UserListResource', function ($resource) {
        'use strict';

        var users = $resource('api/user/:id', {id: '@id'}, {
            query: {method: 'GET', isArray: true},
            update: {method: 'PUT'},
            delete: {method: 'DELETE'}
        });

        return users;
    })

    .factory('CreateUserResource', function ($resource) {
        'use strict';

        var user = $resource('api/rest-auth/registration/:id', {id: '@id'}, {
            save: {method: 'POST'}
        });

        return user;
    });