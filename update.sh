#!/bin/bash

# pull incidents
echo '[ ] Download the incidents data'
wget http://activefiremaps.fs.fed.us/data/kml/conus_lg_incidents.kmz
echo '[ ] Unzip data'
unzip conus_lg_incidents.kmz
echo '[ ] Update the data in the app'
python2.7 manage.py parseincidents conus_lg_incidents.kml
export DATE=`date +"%Y%m%d"`
echo '[ ] Archiving data as: incident$DATE.kml'
mv conus_lg_incidents.kml incidents$DATE.kml

# pull the perimeters
echo '[ ] Getting perimeters'
wget http://rmgsc.cr.usgs.gov/outgoing/GeoMAC/current_year_fire_data/KMLS/ActiveFirePerimeters.kml
mv ActiveFirePerimeters.kml ActiveFirePerimeters.kmz
echo '[ ] Unzipping perimeters'
unzip ActiveFirePerimeters.kmz
echo '[ ] Converting perimeter data'
togeojson ActiveFirePerimeters.kml > static/fire_perimeters_all.json

echo '[ ] Creating minified version'
echo -n 'var perimeters=' > static/fire_perimeters.json.tmp
cat static/fire_perimeters_all.json >> static/fire_perimeters.json.tmp
node_modules/uglify-js/bin/uglifyjs static/fire_perimeters.json.tmp >> static/fire_perimeters.min.json.tmp

echo '[ ] Emptying old data'
rm static/fire_perimeters_all.json
rm static/fire_perimeters.min.json
rm ActiveFirePerimeters.kml

echo '[ ] Replacing existing data'
mv static/fire_perimeters.min.json.tmp static/fire_perimeters.min.json