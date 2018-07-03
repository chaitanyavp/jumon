var app = angular.module('myApp', []);
  app.controller('myCtrl', function($scope) {
      $scope.cardname = "John Doe";
	  // setup some JSON to use
  //var bad = document.getElementById('textbox_id').value;
  var cars = {};
  cars.name = $scope.cardname;
  /*window.onload = function() {
  	// setup the button click
  	document.getElementById("theButton").onclick = function() {
  		doWork()
  	};
  }*/
  function doWork() {
  	// ajax the JSON to the server
  	$.post("receiver" + "?name=" + $scope.cardname, $scope.cardname, function(request){
  		document.getElementById("bad").innerHTML=request;
  		console.log(request)
  	});
  	// stop link reloading the page
   event.preventDefault();
  }
});