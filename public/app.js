(function() {
  'use strict';

  angular.module('renuo.ideas', [
    'ngRoute',
    'renuo.ideas.dashboard'
  ]).
  config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider) {
    $routeProvider.otherwise({redirectTo: '/'});
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);
})();
