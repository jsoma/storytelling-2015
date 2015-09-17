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


## Homework


## Resources

* [Using scales](http://jonathansoma.com/tutorials/d3/using-scales/)
* [Using axes](http://jonathansoma.com/tutorials/d3/using-axes/), which also has a lot of links down at the bottom