'use strict';


angular.module('bulbs.slideshow.edit', [
])
  .directive('slideshowEdit', [
    function () {
      return {
        restrict: 'E',
        templateUrl: 'bulbs/slideshow-edit/slideshow-edit.html',
        scope: {
          article: '='
        }
      };
  }]);