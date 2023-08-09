Vue.component('carousel', {
  template: `
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="imagenes/bailarina1.jpg" alt="Image 1" class="carousel-image">
        </div>
        <div class="carousel-item">
          <img src="imagenes/bailarina2.jpg" alt="Image 2" class="carousel-image">
        </div>
        <div class="carousel-item">
          <img src="imagenes/bailarina3.jpg" alt="Image 3" class="carousel-image">
        </div>
      </div>
      <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  `
});

new Vue({
  el: '#app'
});
