(function() {
  'use strict';

  angular.module('renuo.ideas', [
    'ngRoute',
    'renuo.ideas.dashboard'
  ]).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.otherwise({redirectTo: '/'});
  }]);
})();
