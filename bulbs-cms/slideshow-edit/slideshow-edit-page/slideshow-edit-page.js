'use strict';

angular.module('bulbs.slideshow.edit.page', [])

  .directive('slideshowEditPage', function () {
    return {
      restrict: 'E',
      templateUrl: 'bulbs-cms/slideshow-edit/slideshow-edit-page/slideshow-edit-page.html',
      scope: {
        'page': '='
      }
    };
  });