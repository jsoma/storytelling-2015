[Quick link to class 20](#class20)

# Class 19: Web Applications, Part 1


## Before-Class Prep

Class contents are in [the 19-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-19-20/19-compiled.zip)

You might have these packages already, but let's give it a shot:

````bash
pip install csvkit
pip install peewee
pip install flask
````

**Tracking URLs** are

* http://jonathansoma.com/columbia/app.py
* http://jonathansoma.com/columbia/models.py

## Review

### Links

* [My web applications tutorials](http://jonathansoma.com/tutorials/webapps/)
* [Peewee quickstart](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html#quickstart)
* [Peewee query operators](http://docs.peewee-orm.com/en/latest/peewee/querying.html#query-operators)
* [Flask homepage](http://flask.pocoo.org/)

### Code

Running a Flask app
    
````bash
python app.py
````

Using CSVKit to create a SQLite database

````bash
csvsql --db sqlite:///[filename].db --insert --table [tablename] [filename].csv
````

Connecting to a databse from peewee

````python
from peewee import *

db = SqliteDatabase('[filename].db')
````

Sample model for peewee

````python
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # previously defined (see above)
````

Sample route for Flask

````python
    @app.route('/path/to/cat')
    def index():
        return render_template('cat_picture.html')
````

## Class 19 Homework

### Part one: Peeking at others' work

Find one visualization you like, attempt to figure out how it was done. Answer the following questions:

1. Explain why you like the visualization. What did they do right? Anything that could have been done differently?
2. Examine the source for the basics of how it was created. D3? CartoDB?
3. Any special libraries (e.g. tooltip, queue)? Look for `script` tags, and then google their filenames.
4. Any techniques you find familiar or unfamiliar? Do you think you could reproduce this visualization with a little bit of work?

Display the visualization in an iframe on a Neocities page and add your summary above it. It might *already* be in an iframe - use the web inspector to select it, then glance up the tree. You might see an `<iframe>` tag that you can steal the URL from (and if it exists, that's where you should be using view source anyway).

### Part two: Not-final project

You're going to have a **project** to turn in next Tuesday, working in groups of up to 3 people (although you can also do this solo). Figure out who you're working with, if anyone, and track down a few data sets that might interest you.

Projects need to have around 1000 words, with 3 visuals, 2 data sources, and you must **call or email a source**, even if it's just for a quote. Calling someone early on to get their input about finding a dataset or what to look for inside of one they're familiar with is probably a good idea.

I'd also like a **methods and experiences** section that explains how you did what you did - did everything go wrong? Is your data garbage, and your source a maniac, and all the libraries you worked with haven't been updated since 1998? Explain it all!

If your project is something huge, and you think you aren't going to be done by Tuesday: **you're going to be done by Tuesday anyway!** Turn your partial research into a project, and then you can re-use the data for a second, more in-depth project the next week.

This *seems* really formal but it's honestly the same thing we've been doing for the past million weeks. This time you just get to work in groups and I'm looking for something a little more polished.

<div id="class20">&nbsp;</div>

# Class 20: Web Applications with Flask, Part II

We're using the same code as last time, I've packaged it up in [the 20-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-19-20/20-compiled.zip)

### Review

You can find the completed work from class in [the 20-nyc-schools-partial.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-19-20/20-nyc-schools-partial.zip)

**Database Concepts:** Foreign keys, primary keys, one-to-many, one-to-one, many-to-many, aggregate functions

**Aggregating**

`fn.___` uses [aggregate functions](https://www.sqlite.org/lang_aggfunc.html) in the `____`, so it's specific to what kind of database you're using. SQLite doesn't support too many.

````python
# Max of total_students column
School.select().aggregate(fn.Max(School.total_students))
````

````python
# Lowest total students in all of Brooklyn
School.select().where(School.boro == "Brooklyn").aggregate(fn.Min(School.total_students))
````

````python
# Average total students for Manhattan
School.select().where(School.boro == "Manhattan").aggregate(fn.Avg(School.total_students))
````

````python
# How many schools in Queens?
School.select().where(School.boro == "Queens").count()
````

Now let's kick it up a notch and add in [SQL joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)

````python
# Compare schools in different boroughs
School.select().join(Score).where(School.boro == "Manhattan").aggregate(fn.Avg(Score.critical_reading_mean))
School.select().join(Score).where(School.boro == "Brooklyn").aggregate(fn.Avg(Score.critical_reading_mean))
````

````python
# Compare schools of similar size in the same borough
current_school = School.get(School.dbn == "13K419")
similar_avg = School.select().join(Score).where(
    (School.boro == current_school.boro) & 
    (School.total_students > current_school.total_students * 0.8) & 
    (School.total_students > current_school.total_students * 1.2)
  ).aggregate(fn.Avg(Score.critical_reading_mean))
print "Current school: {}, Average: {}".format(current_school.scores[0].critical_reading_mean, similar_avg)
````