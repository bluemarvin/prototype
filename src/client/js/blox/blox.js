var glmat = require('gl-matrix');
var shaders = require('./shaders');

exports.create = function(gl) {
  return new blox(gl);
};

function blox(gl) {
  this.gl = gl;
  this.proj = glmat.mat4.create();
};

var proto = blox.prototype;

proto.aspectRatio = function (ratio) {
  glmat.mat4.perspective(this.proj, 3.15 / 2, ratio, 1, 1000);
};

proto.render = function () {
  
};

