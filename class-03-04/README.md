[Class 3](#class3) | [Class 4](#class4)

<a id='class3'></a>

# Class 3: `.select`, `.enter` and `.append`

Class contents are in [the 03-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-03-04/03-compiled.zip)

Our tracking URLS will be 

* `http://jonathansoma.com/columbia/03-fix-01.html`
* `http://jonathansoma.com/columbia/03-fix-02.html`
* `http://jonathansoma.com/columbia/03-fix-03.html`
* `http://jonathansoma.com/columbia/03-classwork.html`

<a id="review"></a>

### Review

You can see what we did today at [http://jonathansoma.com/columbia/03-classwork.html](http://jonathansoma.com/columbia/03-classwork.html). You might want to check out [this page](http://alignedleft.com/tutorials/d3/the-power-of-data) for a little more about `.enter().append()`.

I also have an [(incomplete) tutorial](http://jonathansoma.com/tutorials/d3/using-select/) that can help with appending `svg`s or using existing ones.

75% of the time, you just do this

**HTML**:

```html
<svg></svg>
```

**JavaScript**:

```js
var chart = d3.select('svg'); // grab the chart off of the page (might want to use a class)

var rectangles = chart.selectAll('rect') // select all rects (even if there arent any)
                    .data(datapoints) // bind it to the data
                    .enter() // grab the data points without a rect
                    .append('rect'); // and give them a rect to call hom
```

Then you go through the whole `.attr` and `.style` business.

<a id="homework-3"></a>

### Homework

Pick **six states** in the USA, and using [http://water.usgs.gov/edu/wetstates.html](http://water.usgs.gov/edu/wetstates.html), make a **list of dictionaries** that includes:
  
  * The name of the state
  * The total square miles of the state
  * The percent of the state covered in water
  * The land area square miles

1. Manually out an `<svg>` element with six `<rect>` elements inside.
2. Visualize the percent of the state covered in water in a horizontal bar graph, and make the bars blue.
3. Manually type out an `<svg>`, but don't put any `<rect>` elements inside. Use a class to grab it.
4. Visualize the total square miles of the state in a **vertical bar graph**.
5. In the second graph, color any states with a square mileage over 50,000 a different color.

Submit to https://neocities.org, upload your files and announce both URLs in #storytelling in Slack. Due Thursday by 9am.

<a id='class4'></a>

# Class 4: Scales and axes

Tracking URLs will be

* `http://jonathansoma.com/columbia/04-classwork-01.html`
* `http://jonathansoma.com/columbia/04-classwork-02.html`

You can download the template for this class in [this zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-03-04/04-compiled.zip).

## Review

You can find the work we did during class at [http://jonathansoma.com/columbia/04-classwork-01.html](http://jonathansoma.com/columbia/04-classwork-01.html).

* [Using scales](http://jonathansoma.com/tutorials/d3/using-scales/)
* [Using axes](http://jonathansoma.com/tutorials/d3/using-axes/), which also has a lot of links down at the bottom

## Homework

Select at least 10 states from [http://wallethub.com/edu/states-most-least-dependent-on-the-federal-government/2700/](http://wallethub.com/edu/states-most-least-dependent-on-the-federal-government/2700/), and create a list of dictionaries that includes all five of the non-rank categories, ie.

    var states = [ 
      { 'name': 'Arkansas', 'return': 0.62, 'fed_funding_pct': 33.07, 'fed_empl': 6.81, 'civ_empl': 3.59 }
    ];

Also include a key called `affiliation`, marking them as either `Democrat`, `Republican` or `Swing`. You can use [this](http://www.gallup.com/poll/160175/blue-states-outnumber-red-states.aspx) as your source for that data.

Create three charts for Tuesday. Use our entire bag of tools - `.enter().append()`, scales, axes, and setting svg `width` and `height` using variables.

1. A horizontal bar chart of `return`, with Democrat-leaning states as blue, Republican-learning states as red, and swing states as some nice shade of purple. Bar length is the return on investment, and include an axis on the bottom. Label should be state name.
2. A bar chart of `fed_funding_pct`, with the percent number just beyond the tip of the bar (the "index labels" [on this image](http://canvasjs.com/wp-content/uploads/2013/02/html5_chart_label.jpg). Color the bar based on a scale. Include an axis.
3. A scatterplot (aka circles)! Make x be `fed_funding_pct`, the y be `fed_empl`, and the radius of the circle reflect `return`. Include a state label somewhere near the circle (exact position is up to you).
4. Make a copy of the scatterplot and add in an X axis and a Y axis.

> **NOTE:** If you haven't had me before or haven't heard me say it in a while, don't wory if you can't complete all of the homework. Sometimes it's aspirational!

You can turn them in all on the same page or across multiple pages. Submit your neocities.org URLs in #storytelling by 11:59pm on Monday.
