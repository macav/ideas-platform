(function() {
  'use strict';

  function IdeaService($http) {
    var _endpoint = '/ideas/';

    return {
      get: function() {
        return $http.get(_endpoint);
      },
      upvote: function(idea) {
        return $http.post(_endpoint+idea.id+'/upvote', {});
      },
      downvote: function(idea) {
        return $http.post(_endpoint+idea.id+'/downvote', {});
      }
    }
  }
  IdeaService.$inject = ['$http'];

  angular.module('renuo.ideas.dashboard')
  .factory('IdeaService', IdeaService);
})();
