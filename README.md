Stocker
=========

Stocker is a simple stock portfolio app written in Python.
Some of it's roadmap features include

  ~~- Historic Graphic for Stocks~~
  ~~- MongoEngine integration and utilization~~
  ~~- CandleStick Charts~~
  - DataTables in Profile
  - Portfolio Tracking
  - Stock recommendations based on current stock
  - BackTesting
  - Alerts

PreReqs
---

You should run this in an environment that has MongoDB installed and running.

On MacOS, if you have brew installed, you can run the following:
```sh
$ brew install mongodb
$ brew services start mongo
```

Installation
--------------

```sh
git clone https://github.com/ryanhartje/stocker.git
```

From here, run app.py and you can interact with this on port 5001:
```sh
$ cd stocker;
$ python app.py
* Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
* Restarting with stat
```

Now visit http://localhost:5001/


In Progress
----

Update should update your local mongoDB collection. It does not yet parse all
of the data it should.


```sh
$ python update.py -d
```

Version
-----------

0.1.1

Tech
-----------

Stocker uses a number of open source projects to work properly:

* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [Flask] - evented I/O for the backend
* [jQuery] - javascript library
* [MongoDB]

Resources
--------------

Highcharts Fiddle: http://jsfiddle.net/gh/get/jquery/1.9.1/highslide-software/highcharts.com/tree/master/samples/highcharts/demo/line-basic/

License
----

MIT

[Twitter Bootstrap]:http://twitter.github.com/bootstrap/
[jQuery]:http://jquery.com
[Flask]:http://flask.pocoo.org/

Change Log
-------

0.1.1 - [3/12/2017] - Updated package imports, updated update script for testability, and PEP8. Added debug mode.
0.1.0 - [7/20/2015] - Added Historic Data fetching from Yahoo. Also added historic highchart close graph on the view/<stock> page. Updated versioning to SemVer.
0.1 - Basic WUI with add and view
