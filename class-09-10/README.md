[Class 9](#class9) | [Class 10](#class10)

<a id='class9'></a>

# Class 9: Point Maps

Class contents are in [the 09-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-09-10/09-compiled.zip)

Our tracking URL will be 

* `http://jonathansoma.com/columbia/09-classwork.html`

You'll want to be sure ot use `python -m SimpleHTTPServer` to be able to read your external data.

<a id="review"></a>

## Review

[Just watch this](https://www.jasondavies.com/maps/transition/)

## Homework 9

Use [population.csv](https://github.com/jsoma/storytelling-2015/raw/master/class-09-10/population.csv) and make a map of the world, using:

* Use color for the country or region
* Use circle radius to stand for the population

Focus it on any particular part of the world using `.center()` and `.scale()`, and feel free to play around with the [other options and projections](https://github.com/mbostock/d3/wiki/Geo-Projections). Write a little summary of your "findings."

Turn it in by Thursday 9AM by posting in `#storytelling-hw`.

<a id='class10'></a>

# Class 10: Line/Shape Maps

Class contents are in [the 10-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-09-10/10-compiled.zip)

Our tracking URL will be 

* `http://jonathansoma.com/columbia/10-classwork.html`

Be sure to use `python -m SimpleHTTPServer`!

## Review

* [Shape Maps](http://jonathansoma.com/tutorials/d3/shape-maps/)
* [Color scales](http://jonathansoma.com/tutorials/d3/color-scale-examples/)

<a id='class10-hw'></a>

## Homework 10

For your homework, you are to make **at least two maps**, and give a little caption of what the map is. At least one should have some sort of color scale (although categorical/ordinal is also fine, doesn't have to be linear/quantile/etc).

Post links in `#storytelling-hw` on Slack by 9am Tuesday.

You have a few options with your data sources:

1. **You have some geojson with information attached already:** ...where did you get that?
2. **You have a shapefile that has numerical data attached to it:** see section on converting shapefiles to geojson
3. **You have a shapefile + a csv:** if they have matching columns (e.g. one says VIRGINIA in a column and the other also says VIRGINIA in a column) see section on combining below
4. **You are lost and alone:** see Census info below and just use the county-level map we have

### Data sources

If you have something, **go for it!** Shapefiles are fine, you'll just need to convert them (see below).

[NYC data mine](https://data.cityofnewyork.us/data?browseSearch=&scope=&agency=&cat=&type=maps) data sets are usually garbage, but hey, they exist. Be sure to download the shapefile to convert -DO NOT try to download the JSON, it isn't *GeoJSON*. DC [has one too](http://opendata.dc.gov/), as do most cities. But yeah, generally terrible data.

I personally enjoy the US Census Burea's [American Factfinder](http://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t). To get data to use with our county data set:

1. Visit [http://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t](http://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t)
2. Click `Geographies`
3. Select `...County - 50` from the dropdown
4. Select `All Counties within United States`
5. Click `Add to your selections`
6. Pick a table
7. Click `Modify Table` in the upper left
8. Click the *filter icon* ![http://factfinder.census.gov/common/img/ts_filter.png](http://factfinder.census.gov/common/img/ts_filter.png) and make sure you're a) only getting the estimate, NOT the margin of error, and b) only getting the columns you want. (There are probably *two* filter icons, one for each.)
9. Click or unclick any boxes on the left-hand side to include or not-include the data
10. Click "Transpose Rows/Columns" to make one county = one row, instead of one county = one column
11. Click "Download"
12. Uncheck "Include descriptive data element names"
13. Click DOWNLOAD
14. Oh my god you are finally done

If there's anything in particular you want, feel 

### Convert a Shapefile to GeoJSON

Have a shapefile and want to convert it? You have a few options.

#### Use [ogre.adc4gis.com/](http://ogre.adc4gis.com/) or [www.mapshaper.org/](http://www.mapshaper.org/)

Make sure it's one that's **zipped up**, and has a `.shp` along with a `.prj` (and any other files). If it automatically unzips, be sure to zip it up again. Upload it and it should send you back some nice GeoJSON.

#### Do it yourself with GDAL

Maybe it's too big? That might be problematic when reading it into d3, but if you wanted to do it yourself...

Use [this installer](http://www.kyngchaos.com/software/frameworks#gdal) to install GDAL (GDAL framework link), then open up a new Terminal window, make your way to the directory with the shapefile, and run:

     ogr2ogr -f GeoJSON -t_srs crs:84 outputname.geojson inputname.shp

### Making your own dataset

You could always go to [geojson.io](http://geojson.io) to make your own dataset if you *really* wanted to. It better be awesome, though!

### Combining two datasets

What if you have a shapefile/GeoJSON for the shapes and a CSV for your data? We're going to do it in a *half-good* way.

We're going to use the `queue` library to read in a list of files, and then use JavaScript to combine the csv into your json data.

**MAKE SURE YOU HAVE A COLUMN THAT IS THE SAME BETWEEN THE TWO, NAMES OR ABBREVIATIONS OR CODES OR WHATEVER**. It'll probably be `GEO_ID` and `GEO.id` if you're downloading Census data and using the counties geojson we used in class.

You want to add this function and call `d3.csv` and then `d3.json` once it's pulled in the csv. Then you run `combineData` and it adds the data from the CSV into your geojson's properties.

For a working example and a closer look (with more comments), open [10-homework-compiled.zip](https://github.com/jsoma/storytelling-2015/raw/master/class-09-10/10-homework-compiled.zip).

````html
<script src="https://cdnjs.cloudflare.com/ajax/libs/queue-async/1.0.7/queue.min.js"></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js'></script>  
<script>
  function combineData(geojson_data, csv_data, geojson_key, csv_key) {
    geojson_data['features'].forEach( function(d_json) {
      csv_data.forEach( function(d_csv) {
        if(d_json['properties'][geojson_key] == d_csv[csv_key])
          Object.keys(d_csv).forEach( function(key) { d_json['properties'][key] = d_csv[key]; });
      });
    });
  }

  queue()
    .defer(d3.json, "10-homework-shapes.json")
    .defer(d3.csv, "10-homework-data.csv")
    .await( function(error, data, csv_data) {
      // state_name is the column from the geojson
      // name is the column from the csv
      combineData(data, csv_data, "state_name", "state");

      // Now your 'data' elements have the info from the csv file
      // inside of their properties
      
      console.log("Has the added data now, properties look like:");
      console.log(data['features'][0]);
      
      var svg = d3.select("#chart").append('svg'); // etc etc
  })
</script>
````

And yes, you could combine a **million** datasets and layer them all on top of one another - use some geojson for lines and then a csv for city dots etc etc etc.