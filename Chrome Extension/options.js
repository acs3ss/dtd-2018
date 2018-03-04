window.addEventListener('DOMContentLoaded', function() {
    // your button here
    var link = document.getElementById('btnOpenNewTab');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var newURL = "http://stackoverflow.com/";
        chrome.tabs.create({ url: newURL });
    });
	// your button here
    var link = document.getElementById('btnOpenNewTab2');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var newURL = "https://www.nytimes.com/";
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