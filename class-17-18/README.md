# Class 17: Election Day!

Nothing to go here.

# Class 18: QGIS background, Responsive D3

Class contents are in [the 18-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-17-18/18-compiled.zip)

**Tracking URLs** are

* http://jonathansoma.com/columbia/18-classwork-iframe.html
* http://jonathansoma.com/columbia/18-classwork-content.html

Remember to use `python -m SimpleHTTPServer`!

**Other Links**

* [Missed Connections](http://www.iliablinderman.com/connections/)
* [Layer attribution](http://maps.stamen.com/#howto)
* [http://directory.spatineo.com/](http://directory.spatineo.com/) for WMS layers
* [PLUTO data](http://www.nyc.gov/html/dcp/html/bytes/dwn_pluto_mappluto.shtml)
* [CartoDB](http://cartodb.com) and [MapBox](http://mapbox.com)
* [Natural Earth](http://www.naturalearthdata.com/downloads/10m-raster-data/10m-natural-earth-1/)
* [USGS](http://www.usgs.gov/faq/categories/9797/3571)
* Basemaps: [CartoDB](https://cartodb.com/basemaps), [Stamen](http://maps.stamen.com/#toner/12/37.7707/-122.3781)


## Review

#### HTML/JS

Want to scale your viz to be any size? Basic `viewBox` is `0 0 width height`, `preserveAspectRatio` works fine as `xMidYMid meet`. Remember, no height/width!

````html
<svg preserveAspectRatio="xMidYMid meet" viewBox="0 0 900 400">
````

Basic iframe is

````html
<iframe src="example.html" width="400" height="400"></iframe>
````

Responsive iframe is

`````html
<!-- padding-bottom is height / width - this would be 400x900 -->
<div style="position: relative; height: 0; overflow: hidden; padding-bottom: 45%;">
  <iframe class="frame" style=" position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src=""></iframe>
</div>
`````

### Plugins

[OpenStreetMap](https://www.openstreetmap.org/), TileLayersPlugin, Open Layers