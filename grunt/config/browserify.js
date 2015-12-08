module.exports = {
  dist: {
    files: {
      './dist/static/js/application.js': ['./superpunch/superpunch/static/es6/application.js'],
    },
    options: {
      transform: ['babelify']
    }
  }
}
