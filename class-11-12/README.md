[Class 11](#class11) | [Class 12](#class12)

<a id='class11'></a>

# Class 11: Critique and data munging

Class contents are in [the 11-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-11-12/11-compiled.zip)

Our tracking URL will be 

* `http://jonathansoma.com/columbia/11-classwork.html`

Remember to use `python -m SimpleHTTPServer`!

## Homework Critique

#### [Koreans in NYC + Age in NYC](http://woojink.neocities.org/hw/hw10/10-homework.html)

````javascript
var color_scale = d3.scale.linear().domain([0, max_dp0080011]).range(['#e0ece4','#6e016b']);
````

````javascript
var color_scale2 = d3.scale.linear().domain([min_age, max_age]).range(['#ffffff','#7f0000']);
````

#### [Where are the (Poor) College Graduates?](http://siutanwong.neocities.org/hw10/hw10.html)

````javascript
var color_scale = d3.scale.linear().domain([0, 70.0]).range(['beige', 'red']);
````

````javascript
var color_scale2 = d3.scale.linear().domain([0, 30.0]).range(['beige', 'blue']);
````

#### [NYC Population + Vacant Units](http://jordanrosenblum.neocities.org/HW10/hw10.html)


````javascript
var color_scale1 = d3.scale.linear()
                    .domain([0, max_pop])
                    .range(['beige','red']);
````

````javascript
var color_scale2 = d3.scale.linear()
                            .domain([0, mean_vac, max_vac])
                            .range(['#E0F5FF', '#478FB2', '#142933']);
````

#### [GDP Growth of Mainland China](http://www.newsontheroad.com/data/d3/Storytelling_with_data_Homework10_D3.html)

````javascript
var color_scale=d3.scale.linear().domain([0,0.1,7,11]).range(['grey','red','beige','green']);
````

````javascript
var color_scale = d3.scale.linear().domain([min_index,max_index]).range(['blue','red']);
````

#### [Infant Mortality Rate, 1991 vs 2015](http://arushi.neocities.org/Homework10.html)

````javascript
var color_scale1 = d3.scale.linear()
  .domain([min_pop1, median_pop1, max_pop1])
  .range(['#62DB44', '#113573', '#CF1020']);
````

````javascript
var color_scale = d3.scale.linear()
  .domain([0, median_imr, max_imr])
  .range(['#62DB44', '#113573', '#CF1020']);
````

#### [Bachelors Degrees by Subject](http://melissalhaney.neocities.org/homework10.html)

````javascript
var color_scale = d3.scale.linear()
     .domain([0,15000,30000])
    .range(['beige', '#F29500', '#D40000']);
````

#### [Water supply/demand by county](http://casey-huang.neocities.org/HW10.html)

````javascript
var color_scale1 = d3.scale.quantile()
  .domain(all_withdraw)
  .range(['#eef2f5', '#e4ebf1', '#dee8ef', '#d6e4ed', '#d0e2ed', '#c3daec', '#93d5e2', '#04abd0', '#4477c2']);
````

````javascript
var color_scale2 = d3.scale.quantile()
  .domain(public_supply)
  .range(['#fffbe9', '#fffed9', '#fff9ba', '#fff47c', '#ffdd00', '#ffce00', '#d6b800', '#b49a00', '#897c00']);
````

#### [Housing Choices for Married and Non-Family Households](http://superlativenoun.neocities.org/hw10.html)

````javascript
//  d3.max function is giving back very low value for max_val (9.9)
console.log(max_val);

// hard coding max_val at 68, as per data... 
var color_scale = d3.scale.linear()
    .domain([0, median, 68])
    .range(['#5aaf8c', '#ffffe0', '#d84765']);
````

````javascript
var color_scale = d3.scale.linear()
    .domain([0, median, max_val2])
    .range(['#5aaf8c', '#ffffe0', '#d84765']);
````

#### [Family Income in the US](http://spe.neocities.org/lede_class/hw10/10-homework-income.html)

````javascript
// var color_scale = d3.scale.threshold()
var color_scale = d3.scale.linear()
  // .domain([100, 500, 1000, 2500, 5000, 10000])
  // .range(['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']);

  .domain([ min_income , median_income, max_income])
  // .range(['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']);
  // .range(['#007fff','#72a0e5','#ff8000', '#ff0000']);
  .range(['#1a1aff','#551a8b', 'red']);

  // .range(['#00ff00','green','yellow']);
  // .range(['#1a1aff','#329932', 'yellow']);
````

<a id="review"></a>

## Review

Pull data in and out of a `d3.map()` so you don't have to store it with the JSON

````javascript
var state_data = d3.map();

state_data.get('VA');
// undefined

state_data.set('VA', { 'poverty': 34.5 });
state_data.set('NY', { 'poverty': 11.0 });

var datapoint = state_data.get('VA');
// { 'poverty': 34.5 }

var datapoint = state_data.get('NY');
// { 'poverty': 11 }
````

For example, something like...

````javascript
// Let's say the census data has a "GEO.id" column
// while the geojson has a "County Code" column

queue()
    .defer(d3.json, "us-counties-geojson.json")
    .defer(d3.csv, "ACS_12_3YR_B12002.csv", function(d) {
      // save the data by GEO.id so you can grab it later
      return census.set(d['GEO.id'], d);
    })
    .await(ready);
    // .....

// ....

// Let's say each of `datapoints` has a `County Code`.
function ready(error, county_shapes, census_data) {
  // DON'T merge county_shapes and census data, instead...
  // Let
  var counties = county_shapes['features'];

  // ...
  
  svg.selectAll("path")
      .data(counties)
      .enter()
      .append('path')
      .attr('d', path)
      .style('fill', function(d) {
        // grab the data point where we stored it
        // d has a county code 
        var datapoint = census.get(d['County Code']);
        // and use it like normal
        return color_scale(datapoint['Income']);
      });
}

````


CSV data comes in as *strings*, not as *numbers*.

````javascript
var max = d3.max(counties, function(d) {
  // return parseFloat(d['value']) or parseInt(d['value']);
  return +d['value'];
});
````

[Just watch this](https://www.jasondavies.com/maps/transition/)