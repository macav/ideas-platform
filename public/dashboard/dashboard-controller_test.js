'use strict';

describe('renuo.ideas.dashboard module', function() {

  beforeEach(function(){
    jasmine.addMatchers({
      toEqualData: function(util, customEqualityTesters) {
        return {
          compare: function(actual, expected) {
            return {
              pass: angular.equals(actual, expected)
            };
          }
        };
      }
    });
  });
  beforeEach(module('renuo.ideas.djangoAuth'));
  beforeEach(module('renuo.ideas.dashboard'));

  var ideasData = {
    data: [
      {id: 1, title: 'Idea 1', content: 'Idea 1 Content', upvotes: 3, downvotes: 0},
      {id: 2, title: 'Idea 2', content: 'Idea 2 Content', upvotes: 0, downvotes: 0}
    ]
  };

  describe('Dashboard controller', function(){
    var ctrl, scope, $httpBackend;
    beforeEach(inject(function($controller, $rootScope, _$httpBackend_) {
      scope = $rootScope.$new();
      $httpBackend = _$httpBackend_;
      ctrl = $controller('DashboardCtrl', {$scope: scope, ideas: ideasData});
    }));

    it('should have controller defined', function() {
      expect(ctrl).toBeDefined();
    });

    it('should load ideas', function() {
      expect(ctrl.ideas).toBeDefined();
      expect(ctrl.ideas).toEqualData(ideasData.data);
    });

    it('should properly upvote an idea', function() {
      var idea = ctrl.ideas[0];
      var master = angular.copy(idea);
      $httpBackend.expectPOST('/ideas/1/upvote', {}).respond(200, angular.extend(idea, {upvotes: idea.upvotes+1}));
      ctrl.upvote(idea);
      $httpBackend.flush();
      expect(idea.upvotes).toEqual(master.upvotes+1);
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should properly upvote an idea', function() {
      var idea = ctrl.ideas[0];
      var master = angular.copy(idea);
      $httpBackend.expectPOST('/ideas/1/downvote', {}).respond(200, angular.extend(idea, {upvotes: idea.upvotes-1}));
      ctrl.downvote(idea);
      $httpBackend.flush();
      expect(idea.upvotes).toEqual(master.upvotes-1);
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should not upvote non-existing idea', function() {
      var idea = ctrl.ideas[0];
      var master = angular.copy(idea);
      // let's pretend this doesn't exist
      $httpBackend.expectPOST('/ideas/1/upvote', {}).respond(404);
      ctrl.upvote(idea);
      $httpBackend.flush();
      expect(idea.upvotes).toEqual(master.upvotes);
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should not downvote non-existing idea', function() {
      var idea = ctrl.ideas[0];
      var master = angular.copy(idea);
      // let's pretend this doesn't exist
      $httpBackend.expectPOST('/ideas/1/downvote', {}).respond(404);
      ctrl.downvote(idea);
      $httpBackend.flush();
      expect(idea.upvotes).toEqual(master.upvotes);
      $httpBackend.verifyNoOutstandingRequest();
    });
  });
});
