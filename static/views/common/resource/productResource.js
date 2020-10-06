angular.module( 'arisApp.services' )
    .factory( 'productResource', function ($resource) {
        'use strict';

        var product = $resource( 'api/product/:id', {id: '@id'}, {
            query: {method: 'GET', isArray: true},
            save: {method: 'POST'},
            update: {method: 'PUT'}
        });

        return product;
    });