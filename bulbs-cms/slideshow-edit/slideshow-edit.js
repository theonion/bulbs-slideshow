'use strict';


angular.module('bulbs.slideshow.edit', [
  'bulbs.slideshow.edit.page',
  'cms.image'
])

  .directive('slideshowEdit', [
    function () {
      return {
        restrict: 'E',
        templateUrl: 'bulbs-cms/slideshow-edit/slideshow-edit.html',
        scope: {
          article: '='
        },
        controller: [
          '$scope', '$window', '$timeout', 'CmsImage',
          function($scope, $window, $timeout, CmsImage) {
            $scope.isEditing = false;
            $scope.selectedPage = null;
            $scope.$watch('article', function (newVal, oldVal) {
              if ($scope.selectedPage) {
                $scope.selectedPage = _.find($scope.pages, function (value) {
                  return value.order == $scope.selectedPage.order;
                });
              }
            });
            $scope.selectPage = function (page) {
              $scope.selectedPage = page;
              $scope.isEditing = !!page;
              if ($scope.isEditing) {
                $timeout(function () {
                    CmsImage.picturefill($('.slideshow-page')[0]);
                });
              }
            };
            $scope.onAddPage = function () {
              var page = {
                name: '',
                body: '',
                order: $scope.article.slides.length
              };
              $scope.article.slides.push(page);
              updateOrderIds($scope.article.slides, 'order');
              $scope.selectPage(page);
            };
            $scope.onDeletePage = function (objList, obj) {
              var idx = objList.indexOf(obj);
              if (idx >= 0) {
                objList.splice(idx, 1);
                updateOrderIds(objList, 'order');
                if ($scope.selectedPage && obj.order == $scope.selectedPage.order) {
                    $scope.selectPage(null);
                }
              }
            };
            $scope.onClonePage = function (obj) {
              $scope.onAddPage();
              var selected = $scope.selectedPage;
              angular.copy(obj, selected);
              selected.title = 'Clone ' + selected.title;
            };
            $scope.onDeleteObject = function (objList, obj) {
              var idx = objList.indexOf(obj);
              if (idx >= 0) {
                objList.splice(idx, 1);
                updateOrderIds(objList, 'order');
              }
            };
            $scope.onMoveListObject = function(objList, startIndex, newIndex) {
              if (startIndex >= 0 && newIndex >= 0 && newIndex < objList.length) {
                var obj = objList[startIndex];
                objList.splice(startIndex, 1);
                objList.splice(newIndex, 0, obj);
                updateOrderIds(objList, 'order');
              }
            };
            function updateOrderIds(objList, fieldName) {
              for (var i = 0; i < objList.length; i++) {
                objList[i][fieldName] = i;
              }
            }

            if ($scope.article.slides.length === 0) {
              $scope.onAddPage();
            }

            updateOrderIds($scope.article.slides, 'order');
          }

        ],
      };
  }]);