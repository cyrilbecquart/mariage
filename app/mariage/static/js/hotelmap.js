var map;
function initMap() {
	map = new google.maps.Map(document.getElementById('hotelMap'), {
		center : {
			lat : 47.764488,
			lng : 2.021985
		},
		zoom : 10
	});

	// Add a marker at the center of the map.
	addMarkers(getLocations(), map);
}

// get all hotel locations
function getLocations() {
	var hotelLocations = [];
	for ( i = 1; $('#hotel' + i).length > 0; i++) {
		hotelLocations.push([i.toString(), {
			lat : parseFloat($('#hotel' + i).attr('data-lat')),
			lng : parseFloat($('#hotel' + i).attr('data-lng'))
		}]);
	}
	return hotelLocations;
}

// Adds a marker to the map.
function addMarkers(locations, map) {
	// add marker for party location
	var marker = new google.maps.Marker({
		position : {lat: 47.726278, lng: 1.940727},
		map : map,
		icon : 'static/img/flag-icon.png',
	});
	
	// markers for hotels
	for ( i = 0; i < locations.length; i++) {
		var marker = new google.maps.Marker({
			position : locations[i][1],
			label : locations[i][0],
			map : map
		});
	}
}