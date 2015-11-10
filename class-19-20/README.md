# Class 19: Web Applications, Part 1

Class contents are in [the 18-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-19-20/19-compiled.zip)

## Before-Class Prep

You might have these packages already, but let's give it a shot:

````bash
pip install csvkit
pip install peewee
pip install flask
````

Also, download [19-compiled.zip file](https://github.com/jsoma/storytelling-2015/raw/master/class-19-20/19-compiled.zip).

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
    
    python app.py

Using CSVKit to create a SQLite database

    csvsql --db sqlite:///[filename].db --insert --table [tablename] [filename].csv

Connecting to a databse from peewee

    from peewee import *

    db = SqliteDatabase('[filename].db')

Sample model for peewee

    class Person(Model):
        name = CharField()
        birthday = DateField()
        is_relative = BooleanField()

        class Meta:
            database = db # previously defined (see above)

Sample route for Flask

    @app.route('/path/to/cat')
    def index():
        return render_template('cat_picture.html')

## Homework

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