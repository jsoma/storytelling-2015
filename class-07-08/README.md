[Class 7](#class7) | [Class 8](#class8)

<a id='class7'></a>

# Class 7: Chart Types and a Handful of Extras

Class contents are in [the 07-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-07-08/07-compiled.zip)

Our tracking URLS will be 

* `http://jonathansoma.com/columbia/07-classwork-filtering.html`
* `http://jonathansoma.com/columbia/07-classwork-sorting.html`

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