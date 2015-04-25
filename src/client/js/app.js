var blox = require("./blox/blox");

window.addEventListener('load', onload);

function onload() {

  var container = document.getElementById('container');
  var canvas = document.createElement('canvas');
  var gl = canvas.getContext('webgl');
  container.appendChild(canvas);

  if (gl) {
    var world = blox.create(gl);
    render();
  }

  function render() {
    requestAnimationFrame(render);
    var displayWidth  = window.innerWidth;
    var displayHeight = window.innerHeight;

    if ((canvas.width != displayWidth) ||
        (canvas.height != displayHeight)) {

      canvas.width  = displayWidth;
      canvas.height = displayHeight;

      world.aspectRatio(canvas.width / canvas.height);
      gl.viewport(0, 0, canvas.width, canvas.height);
    }
    world.render();
  };
};
