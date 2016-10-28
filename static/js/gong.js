'use strict';

if (!waitlist) {
	var waitlist = {};
}

waitlist.gong = (function() {

	const displayMessage = waitlist.base.displayMessage;
	const addListener = waitlist.sse.addEventListener;
	const storage = sessionStorage;
	var gongbutton;
	var sound;

	function playGong() {
		if (gongbutton.checked) {
			sound.currentTime = 0;
			sound.play();
		}
	}

	function gongClicked() {
		if (gongbutton.checked) {
			sound.removeAttribute("hidden");
			storage["gong"] = "open";
		} else {
			sound.setAttribute("hidden", "");
			sound.pause();
			storage.removeItem("gong");
		}
	}

	function disableGong() {
		gongbutton.checked = false;
		gongClicked();
		document.getElementById("gong").remove();
	}

	function gongSetup() {
		// Setup SSE invite-send event
		addListener("invite-send", playGong);
		gongbutton.addEventListener("click", gongClicked);
		sound.volume = 0.5;
		// Checks storage for gong info if not found alert to please enable notification
		if (storage.getItem("gong")) {
			gongbutton.checked = true;
			gongClicked();
		} else {
			displayMessage("To get informed when you are invited please enable browser notifications in the top right.", "info");
		}
	}

	function init() {
		gongbutton = document.getElementById("gongbutton");
		sound = document.getElementById("sound");
		if (gongbutton) {
			if (window.EventSource) {
				gongSetup();
			} else {
				disableGong();
			}
		}
	}

	$(document).ready(init);
	return {
	disableGong: disableGong
	};
})();