[Class 5](#class5) | [Class 6](#class6)

<a id='class5'></a>

# Class 5: Clicking and hovering with `.on`

Class contents are in [the 05-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-05-06/05-compiled.zip)

Our tracking URLS will be 

* `http://jonathansoma.com/columbia/05-classwork.html`

<a id="review"></a>

### Review

* [Hover notes](http://jonathansoma.com/tutorials/d3/hover-notes/)
* [Clicking and hovering](http://jonathansoma.com/tutorials/d3/clicking-and-hovering/)

<a id="homework-5"></a>

### Class 5 Homework

This homework is a breather to help you relax, focus on what you know, and possibly flex your wings a bit.

Make two charts of any type, using data of your choosing (at least 10 data points apiece). I like to use Wikipedia's [Lists of Lists of Lists](https://en.wikipedia.org/wiki/List_of_lists_of_lists) and [Lists of Lists](https://en.wikipedia.org/wiki/Category:Lists_of_lists) to find fun data sets.

Only requirements are:

* Use `d3.scale` on both
* Make an infobox for *at least* one of them
* Use click and/or hover events to provide some sort of interactivity
* *Try* to make it look at least a *little* nice

Submit your neocities.org URLs in #storytelling by 9:00am on Thursday.

<a id='class6'></a>

# Class 6: Doing margins right, external data dources and (maybe!) sorting and filtering

Class contents are in [the 06-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-05-06/06-compiled.zip)

Our tracking URLS will be 

* `http://jonathansoma.com/columbia/06-classwork-margins.html`
* `http://jonathansoma.com/columbia/06-classwork-external.html`

### Review

Tutorials you might might find helpful are:

* [Positioning axes](http://jonathansoma.com/tutorials/d3/positioning-axes/)
* [Sorting](http://jonathansoma.com/tutorials/d3/sorting/)
* [Scales](http://jonathansoma.com/tutorials/d3/using-scales/) (scroll down to 'ordinal scales', which I'll be posting by Friday PM)
* [Ordinal Scales 1](https://github.com/mbostock/d3/wiki/Ordinal-Scales), [Ordinal Scales 2](http://jaketrent.com/post/use-d3-rangebands/)

You can also use Google to find some!

#### Using an update function

It works like this:

```javascript
// create the svg to draw in
// draw add axes
// append axes

function update(data) {
  // update x scale's domain
  // select x axis using class, use .call to update x axis
  
  // update y scale's domain
  // select y axis using class, use .call to update y axis
  
  // select all of the shapes and bind the data
  // use a key function if you want, .data(datapoints, function() { return d['whatever' ] })
  
  // .enter and .append for the new ones + set default values
  
  // update their width or r or color or whatever
  // throw in transition() if you want
}
var xscale = 
```

[more](https://medium.com/@c_behrens/enter-update-exit-6cafc6014c36), [more](http://bl.ocks.org/mbostock/3808218)

#### Ordinal scales and range bands

The one thing we didn't talk but totally used was *ordinal scales* and *range bands*. Ordinal scales take a list of categories instead of a list of numbers, but still give out numeric output.

```javascript
// create a scale that takes Cats, Dogs, Birds or Turtles as input
// and gives numbers between 0 and 100 as output
var scale = d3.scale.ordinal().domain(["Cats", "Dogs", "Birds", "Turtles"]).rangeBands([0, 100])

// Where is Cats? It has 0-24.
scale("Cats");
// Output: 0

// Where is Dogs? It has 25-49
scale("Dogs");
// Output: 25

// Birds is 50-74
scale("Birds");
// Output: 50

// Turtles is 75-100
scale("Turtles");
// Output: 75

// get the width of every band
scale.rangeBand()
// 25
```

If it helps, think of it as the same as if we had a linear scale that went from 0-3, with cats=0, dogs=1, birds=2, turtles=3.

### Class 6 Homework

Make three charts using data of your choice. They can even be all of the same data, and/or you can re-use data we've had previously. Feel free to share data sets in Slack.

1. **Chart One:** A chart with axes that uses a `g` with margins to fit in the svg. If you use circles, grow the `r` to the right size over 500 milliseconds upon loading of the page. If using rectangles, grow the `width` over the same timeframe instead. Make color mean something - either make your data fall into categories or use a color scale.
2. **Chart Two:** A scatterplot with two axes that uses a `g` with margins to fit in the svg. As you hover over a data point, the point must light up and an infobox must be appear and be filled in. Create an update function where, if I run it with shuffled data(`d3.shuffle(datapoints)`) will change the `x` and `y` of the circles, causing them to swoop around the page.
3. **Chart Three:** A vertical bar chart with axes that uses a `g` with margins to fit in the svg. This chart must use an `d3.scale.ordinal()` scale for its x-axis, as well as have an `update(data)` function as used today in class. Add a piece of text (`<p>` or `<button>` or whatever you want) that, when you click it, runs `update(d3.shufle(datapoints));`
4. If you're feeling triple-exceptional, add a note at the top of each vertical bar noting the amount the bar represents. As the bars change, have this number change with it.

Add a one- or two-sentence caption to each chart explaining your 'findings,' or what the chart displays

If you're doing this all on one page, you'll want to call your data sets and update functions different things, or else they'll cause problems.