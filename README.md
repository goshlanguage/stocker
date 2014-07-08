Stocker
=========

Stocker is a simple stock portfolio app written in Python.
Some of it's roadmap features include

  - Historic Graphic for Stocks
  - Portfolio Tracking with TradeKing API
  - Stock recommendations based on current stock

Version
----

.01

Tech
-----------

Dillinger uses a number of open source projects to work properly:

* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [Flask] - evented I/O for the backend
* [jQuery] - duh 

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

