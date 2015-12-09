module.exports = {
  sass: {
    files: './superpunch/superpunch/static/scss/**/*.scss',
    tasks: ['compass'],
  },

  es6: {
    files: './superpunch/superpunch/static/es6/**/*.js',
    tasks: ['browserify'],
  },
}
