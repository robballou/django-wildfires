#!/bin/bash

# pull incidents
echo '[ ] Download the incidents data'
wget http://activefiremaps.fs.fed.us/data/kml/conus_lg_incidents.kmz
echo '[ ] Unzip data'
unzip conus_lg_incidents.kmz
echo '[ ] Update the data in the app'
python manage.py parseincidents conus_lg_incidents.kml
export DATE=`date +"%Y%m%d"`
echo '[ ] Archiving data as: incident$DATE.kml'
mv conus_lg_incidents.kml incidents$DATE.kml

# pull the perimeters
echo '[ ] Getting perimeters'
wget http://rmgsc.cr.usgs.gov/outgoing/GeoMAC/current_year_fire_data/KMLS/ActiveFirePerimeters.kml
mv ActiveFirePerimeters.kml ActiveFirePerimeters.kmz
echo '[ ] Unzipping perimeters'
unzip ActiveFirePerimeters.kmz
togeojson ActiveFirePerimeters.kml > static/fire_perimeters.json
rm ActiveFirePerimeters.kml