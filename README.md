Stocker
=========

Stocker is a simple stock portfolio app written in Python.
Some of it's roadmap features include

  ~~- Historic Graphic for Stocks~~
  ~~- MongoEngine integration and utilization~~
  - CandleStick Charts
  - DataTables in Profile
  - Portfolio Tracking
  - Stock recommendations based on current stock
  - BackTesting
  - Alerts

Version
-----------

0.1.0

Tech
-----------

Stocker uses a number of open source projects to work properly:

* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [Flask] - evented I/O for the backend
* [jQuery] - duh 
* [MongoDB]

Resources
--------------

Highcharts Fiddle: http://jsfiddle.net/gh/get/jquery/1.9.1/highslide-software/highcharts.com/tree/master/samples/highcharts/demo/line-basic/

Installation
--------------

```sh
git clone https://github.com/ryanhartje/stocker.git
```

##### Be sure to configure update.py in your crons or other scheduler 

I have my cron set to run update every 5 minutes:

```sh
*/5 * * * * /usr/bin/python /path/to/update.py > /var/log/stocker.log 2> /var/log/stocker-error.log
```


License
----

MIT

[Twitter Bootstrap]:http://twitter.github.com/bootstrap/
[jQuery]:http://jquery.com
[Flask]:http://flask.pocoo.org/

Change Log
-------
0.1.0 - [7/20/2015] - Added Historic Data fetching from Yahoo. Also added historic highchart close graph on the view/<stock> page. Updated versioning to SemVer.
0.1 - Basic WUI with add and view

