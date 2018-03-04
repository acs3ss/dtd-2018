
window.addEventListener('DOMContentLoaded', function() {
    // your button here
	chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
	console.log(url);
});
    var link = document.getElementById('btnOpenNewTab1');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var newURL = "https://www.washingtonpost.com/regional/";
        chrome.tabs.create({ url: newURL });
    });
	// your button here
    var link = document.getElementById('btnOpenNewTab2');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var newURL = "https://stackoverflow.com/";
        chrome.tabs.create({ url: newURL });
    });
	    var link = document.getElementById('btnOpenNewTab3');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var newURL = "https://www.nytimes.com/";
        chrome.tabs.create({ url: newURL });
    });
	    var link = document.getElementById('btnOpenNewTab4');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var newURL = "https://www.breitbart.com/";
        chrome.tabs.create({ url: newURL });
    });
});

var dial = $(".dial .inner");
	var gauge_value = $(".gauge .value");

		function rotateDial()
		{
			var deg = 0;
			var value = Math.round(Math.random()*100);
			deg = (value * 177.5) / 100;

			gauge_value.html(value + "%");

			dial.css({'transform': 'rotate('+deg+'deg)'});
		    dial.css({'-ms-transform': 'rotate('+deg+'deg)'});
		    dial.css({'-moz-transform': 'rotate('+deg+'deg)'});
		    dial.css({'-o-transform': 'rotate('+deg+'deg)'}); 
		    dial.css({'-webkit-transform': 'rotate('+deg+'deg)'});
		}

		setInterval(rotateDial, 2000);