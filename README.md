# geolocation_PME
Use folium maps to compare two lat/long locations and choose one. 

Runs within a Jupyter Notebook. Won't run as straight Python.

Goal is to compare one or two lat/long locations on a map,
select one to "keep", or choose "none" or "decide later".

Context is specimen locations in PME's mineral collection. 
Locations for most sepcimens in Cabinets 1-21 were defined by 
worklearn students between 2017 and 2024. For specimens without this
location information, address, province, country, etc. were compiled
and passed to GeoAppify to "guess" a lat long. This works only about half
the time so review of results is necessary. 

This tool is meant to make this task efficient when reviewing +/- 10,000 specimens. 
