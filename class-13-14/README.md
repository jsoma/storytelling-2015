# Class 13/14: Nonexisting values, time and updating

Class contents are in [the 13-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-13-14/13-compiled.zip)

Our tracking URL will be 

* `http://jonathansoma.com/columbia/13-classwork.html`

Remember to use `python -m SimpleHTTPServer`!

## Review

**Long vs. Wide data**

Takes a look at [high-tech-exports-wide.csv](high-tech-exports-wide.csv) and [high-tech-exports-long.csv](high-tech-exports-long.csv). Wide has one row per country, with every column being a year. Long has one row per country-year pair. You can convert between the two easily with pandas, check out [this notebook](convert-wide-to-long.ipynb).

You can also check out [this tutorial I wrote](http://jonathansoma.com/tutorials/d3/wide-vs-long-data/) that shows you how to convert between the two (kind of!) in D3/JavaScript.

**`setTimeout`, `setInterval` and `d3.timer`**

`setTimeout` executes a function after a certain amount of time.

````javascript
// run a function after 250ms
setTimeout( function() {
  console.log("I was just run")
}, 250)
````

`setInterval` runs a function after a certain amount of time, again and again and again.

````javascript
// run a function after 250ms
setInterval( function() {
  console.log("I am run every 250ms")
}, 250)
````

`d3.timer` runs a function after a certain amount of time, again and again and again. But two important improvements over `setInterval`: 1) if the last iteration hasn't finished yet, it won't run, and 2) it will stop repeating if you return true.

````javascript
// run a function after 250ms
var count = 0;
setInterval( function() {
  count++;
  console.log("I am run every 250ms");
  if(count >= 5) {
    // stop running after 5 iterations
    return true;
  }
}, 250)
````

**Missing data**

Instead of testing if something is `None` or `nil` or `null`, you check if its *type is *the string `"undefined"`*. Stupidly complicated, right? Looks like this:

````javascript
if(typeof datapoint === 'undefined') {
  return '#666666';
}
````

Why doesn't it need parens? [Because they said so](http://stackoverflow.com/questions/15843805/why-does-typeof-not-need-parentheses).

<a id="homework"></a>

## Homework

Let's take some data and watch it change over time! Your assignment is to create **two visualizations** (two charts or one map and one chart). One shows a looping animation of your data over time, and the other is *not* animated and presents the same data differently.

For example, the map we made in class + a line chart of all of the countries' high-tech exports over time.

You will **absolutely need to convert your data to long format.** Don't even *try* to do it with wide format data. You will not succeed, mainly because you'll need to `d3.nest` your data to make the line chart. You might want to [refresh your knowledge of `d3.nest`](https://github.com/jsoma/storytelling-2015/tree/master/class-07-08).

My data came from [the World Bank](http://data.worldbank.org/), and yours can too!

## Links

* [Reddit's /r/DataIsBeautiful](https://www.reddit.com/r/dataisbeautiful)
* [Traffic Accidents in Cambridge, MA from 2010 to 2013](http://siutanwong.neocities.org/hw12/hw12.html)
* [Economics of Canadian provinces, 2009-2013](http://woojink.neocities.org/hw/hw12/12-homework.html)
* [NYC traffic deaths in 2014](http://jordanrosenblum.neocities.org/HW12/hw12.html)
* [My Spending Habit](http://tonypaek.neocities.org/hw12/hw12.html)
* [Unemployment Population](http://arushi.neocities.org/Homework12.html)
* [Most Common Contributing Factors in Fatal NYC Car Crashes](http://superlativenoun.neocities.org/hw12.html)
* [Major Tranfers in England Premier League (Summer 2015)](http://newsontheroad.neocities.org/lede_storytelling_with_data/Storytelling_with_data_Homework12_D3.html)
