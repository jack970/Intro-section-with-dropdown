function toggle() {
	document.querySelector(".menu").classList.toggle("open");
	document
		.querySelector(".background-mobile")
		.classList.toggle("show-background");
	document.querySelector(".openbtn").classList.toggle("change-pos-btn");
	document.querySelector(".close-menu").classList.toggle("show-close-menu");
	document.querySelector(".open-menu").classList.toggle("close");
}
