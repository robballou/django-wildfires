var map = L.map('map').setView([map_center[0], map_center[1]], 5);

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
   attribution: '',
    maxZoom: 18
}).addTo(map);

var incident_markers = {},
  percent_regex = /^(\d+)%/;
for (var i = 0; i < incidents.length; i++) {
  var marker = L.circleMarker([incidents[i].lat, incidents[i].lon]).addTo(map),
    percent_contained = incidents[i].percent_contained,
    color = '';

  if (percent_regex.test(percent_contained)) {
    match = percent_contained.match(percent_regex);
    percent_contained = parseInt(match[1], 10);
    if (percent_contained === 0) {
      color = '#FF3300';
    }
    else if (percent_contained > 0 && percent_contained < 50) {
      color ='#999900';
    }
    else if (percent_contained >= 50 && percent_contained < 70) {
      color ='#3399FF';
    }
    else if (percent_contained >= 70) {
      color ='#66CC00';
    }
    marker.setStyle({'color': color });
  }

  marker.setRadius(5);
  marker.bindPopup('<b>' + incidents[i].name + '</b><br />' + incidents[i].description);
  incident_markers[incidents[i].name] = marker;
}

$(document).ready(function() {
  $('body').on('click', 'a.incident', function(event) {
    event.preventDefault();
    var this_name = $(this).text();
    $.each(incident_markers, function(key, incident) {
      if (key == this_name) {
        incident.openPopup();
      }
    });
  });

  console.log(perimeters);
  for (var feature in perimeters.features) {
    if (perimeters.features.hasOwnProperty(feature)) {
      var this_feature = perimeters.features[feature];
      if (this_feature.geometry.type !== 'Point') {
        var geo_feature = L.geoJson(this_feature, {style: {'color': '#ff0000', 'weight': 1}}).addTo(map);
        geo_feature.bindPopup('<b>' + this_feature.properties.name + '</b>');
      }
    }
  }
});