/**
 * @author Michael Place
 */

function initialize() {
	var mapOptions = {
		center: new google.maps.LatLng(40.75, -111.8833),
		zoom: 10,
		mapTypeId: google.maps.MapTypeId.TERRAIN
	};
	var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
	
	var kmlOptions = {
		clickable: true,
//		map: map,
	}
	
	var kml = new google.maps.KmlLayer('http://mapsirunfarcom.uu5m.stackablehost.com/kml/wasatch2.kml', kmlOptions);
	kml.setMap(map);
}
