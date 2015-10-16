[Class 11](#class11) | [Class 12](#class12)

<a id='class11'></a>

# Class 11: Critique and data munging

Class contents are in [the 11-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-11-12/11-compiled.zip)

Our tracking URL will be 

* `http://jonathansoma.com/columbia/11-classwork.html`

Remember to use `python -m SimpleHTTPServer`!

I've broken out the **homework** and **links** into [11-README.md](11-README.md).

## Homework

Make a map! Or a chart. You can just revise what you turned in on Tuesday.

Reading list:

* [WNYC Stop and Frisk Critique](http://spatialityblog.com/2012/07/27/nyc-stop-frisk-cartographic-observations/)
* [Value by alpha maps](http://andywoodruff.com/blog/value-by-alpha-maps/)
* [How the Rainbow Color Map Misleads](https://eagereyes.org/basics/rainbow-color-map)
* [Norminal vs Ordinal vs Quantitative](http://cose.math.bas.bg/Sci_Visualization/compGenVis/chapter2/tsld012.htm)
* [Interactive Population Map](http://www.slate.com/articles/life/culturebox/2014/10/population_map_use_our_interactive_map_to_figure_out_how_many_flyover_states.html)
* [Racial Dot Map](http://demographics.coopercenter.org/DotMap/)
* [This is like three sentences](http://cose.math.bas.bg/Sci_Visualization/compGenVis/chapter2/tsld012.htm)

# Class 12: Using color and interacting across charts

Class contents are in [the 12-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-11-12/12-compiled.zip)

Our tracking URL will be 

* `http://jonathansoma.com/columbia/12-classwork.html`

Remember to use `python -m SimpleHTTPServer`!

## Links

* [Chessboard](https://upload.wikimedia.org/wikipedia/commons/e/ed/Same_color_illusion_proof2.png)
* [Color Brewer](http://colorbrewer2.org)
* [HSV/HSL](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Hsl-hsv_models.svg/800px-Hsl-hsv_models.svg.png)
* [Chromoscope](http://www.chromoscope.net)
* [Mantis Shrimp](https://en.wikipedia.org/wiki/Mantis_shrimp#Eyes)
* [Retinal Variables](http://understandinggraphics.com/wp-content/uploads/2010/01/retinal-variables.png)
* [Color Oracle](http://colororacle.org)
* [GDP Growth in Mainland China](http://www.newsontheroad.com/data/d3/Storytelling_with_data_Homework10_D3.html)
* [Housing Choices](http://superlativenoun.neocities.org/hw10.html)
* [How old is your Neighborhood?](http://woojink.neocities.org/hw/11-homework.html)
* [What did you major in?](http://melissalhaney.neocities.org/homework11.html)
* [Mass shootings](http://spe.neocities.org/lede_class/hw8/hw8-mass-shootings-redesign.html)
* [Commute times](http://journcoder.neocities.org/LFhomework11.html)

<a id="class12-hw"></a>

## Class 12 Homework

For you homework you'll need to create **two maps or charts that use class-based interactivity**. The maps or charts must be **different types**, for example:

* a map and some line charts, or
* a bar graph and a line chart, or
* a map of shapes and a map of points, etc.

When you hover or click something in one visualization, it should change something about the other visualization (this doesn't have to go both ways). You'll want to assign classes to each data point in your visualizations, and then use those classes to manipulate the data.

Additionally, create a writeup that can be used to interact with the map. A simple example would be

**HTML**

````html
There were <a href="#" class="show-shootings-2015">3 shootings in 2015</a>.
````

**Javascript**

````javascript
// Grab all the links on the page that point to 'show-shootings-2015'
d3.selectAll(".show-shootings-2015").on('mouseover', function(d) {
  // Turn 2015's shooting circles red
  d3.selectAll(".shooting-circle.year-2015").style('fill', 'red');
})
````

A simple way to create your two visuals would be to display all of your points on one visual, then have another visual that groups your data (by year, etc). Interacting with the grouped one will then highlight pieces of your complete visualization. See more info about using `d3.nest` for grouped data at [http://learnjsdata.com/group_data.html](http://learnjsdata.com/group_data.html), or in our classwork at [12-classwork-completed.html](12-classwork-completed.html) (the line chart is grouped by years).

**More tips**

You can give elements multiple classes using spaces, e.g. `"animal cat has-claws"`. When using `d3.selectAll` you can grab them using any combination, such as `.animal`, `.cat`, `.has-claws`, `.animal.has-claws`, etc. This enables you to slice your data different ways.