var map;
function initHotelMap() {
	map = new google.maps.Map(document.getElementById('hotelMap'), {
		center : {
			lat : 47.764488,
			lng : 2.021985
		},
		zoom : 10
	});

	addLocationsMarkers(map);
	addHotelMarkers(getLocations(), map);
}

function initLocationsMap() {
	map = new google.maps.Map(document.getElementById('locationsMap'), {
		center : {
			lat : 47.764488,
			lng : 2.021985
		},
		zoom : 10
	});

	addLocationsMarkers(map);
	addHotelMarkers(getLocations(), map);
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

// Adds markers for Locations, with nice icons
function addLocationsMarkers(map) {
	// add marker for 
	// party location
	var marker = new google.maps.Marker({
		position : {lat: 47.726278, lng: 1.940727},
		map : map,
		icon : 'static/img/castle-icon-blue.png',
	});
	// church location
	var marker = new google.maps.Marker({
		position : {lat: 47.699065, lng: 2.021684},
		map : map,
		icon : 'static/img/church-icon-green.png',
	});
	// brunch location
	var marker = new google.maps.Marker({
		position : {lat: 47.761590, lng: 2.271166},
		map : map,
		icon : 'static/img/home-icon-red.png',
	});
}

// add markers for hotels
function addHotelMarkers(locations, map) {

	for ( i = 0; i < locations.length; i++) {
		var marker = new google.maps.Marker({
			position : locations[i][1],
			label : locations[i][0],
			map : map
		});
	}
}