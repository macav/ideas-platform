(function() {
  'use strict';

  function DashboardCtrl(ideas, IdeaService, DjangoAuthUser) {
    this.ideas = ideas.data;
    this.user = DjangoAuthUser;
    this.upvote = function(idea) {
      IdeaService.upvote(idea).then(function(response) {
        angular.extend(idea, response.data);
      });
    }
    this.downvote = function(idea) {
      IdeaService.downvote(idea).then(function(response) {
        angular.extend(idea, response.data);
      });
    }
  }
  DashboardCtrl.$inject = ['ideas', 'IdeaService', 'DjangoAuthUser'];
  DashboardCtrl.resolve = {
    ideas: ['IdeaService', function(IdeaService) {
      return IdeaService.get();
    }]
  };

  function DashboardConfig($routeProvider) {
    $routeProvider.when('/', {
      templateUrl: 'static/dashboard/dashboard.html',
      controller: 'DashboardCtrl',
      controllerAs: 'ctrl',
      resolve: DashboardCtrl.resolve
    });
  }
  DashboardConfig.$inject = ['$routeProvider'];

  angular.module('renuo.ideas.dashboard')
  .config(DashboardConfig)
  .controller('DashboardCtrl', DashboardCtrl);
})();
