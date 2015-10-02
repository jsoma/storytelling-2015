[Class 7](#class7) | [Class 8](#class8)

<a id='class7'></a>

# Class 7: Chart Types and a Handful of Extras

Class contents are in [the 07-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-07-08/07-compiled.zip)

Our tracking URLs will be 

* `http://jonathansoma.com/columbia/07-classwork-filtering.html`
* `http://jonathansoma.com/columbia/07-classwork-sorting.html`

Our magic phrases will be:

* How much do we need to know? Do we need numbers?
* Compared to *what?*

<a id="review"></a>

### Review


**Reading from a CSV**

````javascript
    d3.csv("filename.csv", function(error, data) {
      console.log(data);
    })
````

**Running a server**

    python -m SimpleHTTPServer

**Sorting**
    
````javascript
    list = [ {'age': 5, 'name': 'Annie'}, {'age': 9, 'name': 'Peter'}, {'age': 42, 'name': 'Deborah'}, {'age': 22, 'name': 'Eve'}];
    list.sort( function(a, b) { 
      return a['age'] > b['age']; 
    })
````
    
**Filtering**

`.indexOf` returns a -1 when the argument passed does not exist in the list.

````js
d3.selectAll('circle')
  .filter( function(d) {
    return ['USA', 'India', 'China'].indexOf(d['Country']) != -1;
  })
````
**Buttons**

    <button id="my-button">This is a button</button>

### Homework

1. Read the first 4 chapters of Edward Tufte's **The Visual Display of Quantitative Information**.
2. Make a graphic *to be critiqued in class.* It can be D3, it can be drawn on a piece of paper, it can be made in [Tableau](http://jordanrosenblum.neocities.org/HW6/hw6.html), it can come from Excel, it can be from [DataWrapper](https://datawrapper.de): just *some sort of data visualization*. You can use data we've worked with already, or anything else you'd like. Include a short caption.
3. Turn in by 9am Thursday by posting to `#storytelling-hw` on Slack.

<a id="class8"></a>

# Class 8: Lines Galore

Class contents are in [the 08-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-07-08/08-compiled.zip)

Our tracking URL will be 

* `http://jonathansoma.com/columbia/08-classwork.html`

## Review

* http://www.w3schools.com/svg/svg_path.asp
* https://www.dashingd3js.com/svg-paths-and-d3js
* https://www.dashingd3js.com/d3js-scales (scroll down to `Color`)
* http://bl.ocks.org/mbostock/3883245
* http://bl.ocks.org/natemiller/20f9bd99d1795e3a0b1c

Also be sure to check out [08-single-line-complete.html](08-single-line-complete.html) and [08-multiple-lines-complete.html](08-multiple-lines-complete.html) and [http://jonathansoma.com/columbia/08-classwork.html](http://jonathansoma.com/columbia/08-classwork.html).

## Homework

**PART ONE: BRAINS**

Figure out something you want to do a project on (and find the dataset). If you don't have anything you want to do a project on, that's fine, too, I'll just assign a data set.

I'll be posting a Google Forms link in Slack for you to complete this part. Due by 9am Tuesday.

**PART TWO: BRAWN**

We want to make a chart [just like this one from the New York Times](http://www.nytimes.com/interactive/2009/11/06/business/economy/unemployment-lines.html), with the following bits and pieces

* Time series of at least 5 lines (but hopefully a lot more). No limit on number of x-axis points, you could even make a [slopegraph](http://charliepark.org/slopegraphs/)
* All lines are some light color at the beginning
* Hovering over a line makes it become highlighted and a little thicker (stroke=color, stroke-width=thickness)
* When you hover or click (up to you), a filled-in infobox appears telling you what country (or whatever) it is
* Paragraph to serve either as informative caption or list some findings/leads
* **Bonus:** Circles that also react to hovering and clicking, if you can figure out a way to make them look nice
* **Bonus:** You'll have problems with paths and circles being behind other paths/circles. Google around to see if you can find an answer to this problem.

Use whatever data you want, although a good time series might be hard to find. I tried it out using some data from [http://www.economicswebinstitute.org/ecdata.htm](http://www.economicswebinstitute.org/ecdata.htm) and it seemed to work well, they have a fair amount that's relatively clean. You'll want to make sure it's in this format:

|name|year|value|
|---|---|---|
|A|1970|10|
|A|1990|4|
|B|1970|5|
|B|1990|10|

**BE SURE TO READ ALL OF MY NOTES AND TIPS BELOW, THERE ARE MANY USEFUL INSTRUCTIONS**

**Due by 9am Tuesday**, post link in #storytelling-hw.

### HOMEWORK TIP: Using external data

We don't want to type all of this data into some `var datapoints =` line, we just want to use the csv that we downloaded or expored from Excel! It's no big deal - I have a [writeup here](http://jonathansoma.com/tutorials/d3/using-external-data/) but the text below might be enough for you.

Let's say previously we wrote code like this:

```javascript
var datapoints = [ {...} ];
var svg = d3.select("#chart").append("svg").attr("height", 400).attr("width", 400);
// blah blah
var circles = svg.selectAll("circles").data(datapoints).enter().append('circles')
// blah blah
````

Now we just need to do **two things**.

First, we wrap it all in a method called `d3.csv`

````javascript
d3.csv("data.csv", function(error, datapoints) {
  console.log(datapoints);
  var svg = d3.select("#chart").append("svg").attr("height", 400).attr("width", 400);
  // blah blah
  var circles = svg.selectAll("circles").data(datapoints).enter().append('circles')
  // blah blah
})
````

But we'll get an error if we try to open our web page the way we always do. The second change is we need to **run a little server on our computer**.

Make your way to the directory that the `.html` and `.csv` are in and run

    python -m SimpleHTTPServer

You'll need a notice that says

    Serving HTTP on 0.0.0.0 port 8000 ...

Visit [http://localhost:8000/](http://localhost:8000), open up your html file from there, and you'll be good to go!

### HOMEWORK TIP: How to fix up your data set

There are lots of great data sources on [http://www.economicswebinstitute.org/ecdata.htm](http://www.economicswebinstitute.org/ecdata.htm), *but* you'll need to edit them a little bit.

**First!!!**

Cut and paste the "important" part of the data into a new Excel sheet, and make sure all of your columns have names (and the year names are actually years, not '2008-2012' or '2005 estimate').

**Second!!!**

Make sure every year is a row. How? Like this:

I originally tested this out with a dataset about [remittances](https://en.wikipedia.org/wiki/Remittance), but the data looked something like this:

|Country|1970|1980|1990|2000|
|---|---|---|---|---|
|Albania|3|4|5|23|
|Greece|53|2|..|33|

Unfortunately, that isn't going to work for us! Instead of having years as columns, we need *one year/country pair on every row*.

Luckily, it's easy with pandas! You use the `pd.melt` method to convert all of those rows into columns.

````python
import pandas as pd
df = pd.read_csv("remittances.csv")
melted = pd.melt(df, id_vars=['Country'], var_name='year', value_name='remittances')
melted.to_csv("melted.csv", index=False)
melted.head()
````

|Country|year|remittances|
|---|---|---|
|Albania|1970|3|
|Albania|1980|4|
|Albania|1990|5|
|Albania|2000|23|
|Greece|1970|53|
|Greece|1980|2|
|Greece|1990|..|
|Greece|2000|33|

If you don't want to do that yourself, you can use my [melted-remittances.csv](melted-remittances.csv) file.

**THIRD!!**

Two things you'll need to do when reading in your data: get rid of rows without data and convert the year and amount to numbers.

To get rid of any rows that don't have data in them (`N/A`, `..`, etc), you just *filter* out the bad ones using `.filter`. For example, mine had a lot of `..` instead of actual values.

````javascript
datapoints = datapoints.filter( function(d) {
  // if remittances is not '..', we'll keep it
  return d['remittances'] != '..'
});
````

Then you need to convert all of the amounts and years to numbers (for some reason they default to strings). You can do that by adding a `+` in front of them.

````javascript
datapoints.forEach( function(d){
  d['year'] = +d['year'];
  d['remittances'] = +d['remittances']; 
});
````

So in the end your code will look like this:

````javascript
d3.csv("filename.csv", function(error, datapoints) {
  // Filter out bad data
  datapoints = datapoints.filter( function(d) {
    // if remittances is not '..', we'll keep it
    return d['remittances'] != '..'
  });
  
  // Convert everything to numbers
  datapoints.forEach( function(d){
    d['year'] = +d['year'];
    d['remittances'] = +d['remittances']; 
  });
  
  var svg = //....etc etc
});

Just be sure you're filtering before you're converting to numbers!

**FOURTH!!**

For god knows what reason d3 automatically reads in all of your data as strings. We fix it like this.

````javascript
d3.csv("melted.csv", function(error, datapoints) {
  datapoints = datapoints.filter( function(d) {
    // if remittances is not '..', we'll keep it
    return d['remittances'] != '..'
  });

  // Use '+' to make JavaScript convert the year 
  // and remittances columns into numbers
});
````
