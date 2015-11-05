/**
 * Compile sass files.
 */
'use strict';

module.exports = {
  bulbs_cms_dist_styles_to_tmp_dist: {
    options: {
      sourcemap: 'none'
    },
    files: {
      '.tmp/bulbs-cms-dist/slideshow.css': 'bulbs-cms/slideshow.scss'
    }
  }
};