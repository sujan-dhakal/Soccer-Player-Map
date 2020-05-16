function format(str) {
    var a = str.split(' ')
                .map(w => w[0].toUpperCase() + w.substr(1).toLowerCase())
                .join(' ')
    return a;
} // Make title case: WAKE fORest -> Wake Forest

var map = L.map('map', {
    center: [37.0, -95.0],
    minZoom: 2,
    maxZoom: 15,
    zoom: 2
});

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a', 'b', 'c']
}).addTo(map);

var markerClusters = L.markerClusterGroup();

for (var i = 0; i < hs_json.length; ++i) {
    var player = players_json[i];

    var school = hs_json.filter((hs) => {
        return hs.id == player.High_School_id;
    })[0];

    var college = college_json.filter((college) => {
        return college.id == player.College_id;
    })[0];

    var popup = player.first_name + ' ' +
        player.last_name +
        '<br/> High School: ' + format(school.Name) +
        '<br/> Hometown: ' + format(player.Hometown) +
        '<br/> College: ' + format(college.Name);

    var m = L.marker([school.location_lat, school.location_long])
        .bindPopup(popup);

    markerClusters.addLayer(m);
}

map.addLayer(markerClusters);