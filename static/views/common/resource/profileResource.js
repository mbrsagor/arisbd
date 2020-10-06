angular.module('arisApp.services')
    .factory('profileResource', function ($resource) {
        'use strict';

        var profile = $resource( 'api/profile/:id', {id: '@id'}, {
            update: {method: 'PUT', params: {id: '@id'}},
            query: {method: 'GET', isArray: true},
            post: {method: 'POST'}
        });

        return profile;
    })
    
    .factory('ActiveprofileResource', function ($resource) {
        'use strict';

        var active_profile = $resource( 'api/active-profile/:id', {id: '@id'}, {
            my_profile: {method: 'GET', params: {id: '@id'}}
        });

        return active_profile;
    });
