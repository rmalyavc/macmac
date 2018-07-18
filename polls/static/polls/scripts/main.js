// Add .class in viewport
function ready(){
	const bp = 1024;
  const ww = window.innerWidth;
  let slider = document.getElementById('slides').getElementsByClassName('item');

  if (ww < bp) {
  	for (let i = 0; i < slider.length; i++) {
  		let result = slider[i];
  		let cl = result.getAttribute('class');
  		result.setAttribute('class', cl + ' ' + 'slide');//rewrite with ES6
  		console.log(result);
  	}
  }
}
document.addEventListener("DOMContentLoaded", ready());


// Slideshow
var slideIndex = 0;
var slideIndex2 = 0;

function plusSlides(n, cont) {
	var len = document.getElementById(cont).getElementsByClassName('slide').length;
	if (cont === 'slideshow') {
		slideIndex += n;
		if (slideIndex >= len)
			slideIndex = 0;
		else if (slideIndex < 0)
			slideIndex = len - 1;
	  showSlides(cont);
	  slideIndex++;
	}
	else {
		slideIndex2 += n;
		if (slideIndex2 >= len)
			slideIndex2 = 0;
		else if (slideIndex2 < 0)
			slideIndex2 = len - 1;
		showSlides(cont);
		slideIndex2++;
	}
}

function showSlides(cont) {
	var count = slideIndex;
	if (cont === 'slides')
		count = slideIndex2;

	var slides = document.getElementById(cont).getElementsByClassName('slide');
	for (var i = 0; i < slides.length; i++) {
		if (count !== i)
			slides[i].style.display = 'none';
		else
			slides[i].style.display = 'block';
	}
}

setInterval(function() {
	var len = document.getElementById('slideshow').getElementsByClassName('slide').length;
	if (slideIndex >= len)
		slideIndex = 0;
	showSlides('slideshow');
	slideIndex++;
}, 4000);

setInterval(function() {
	var len = document.getElementById('slides').getElementsByClassName('slide').length;
	if (slideIndex2 >= len)
		slideIndex2 = 0;
	showSlides('slides');
	slideIndex2++;
}, 4000);