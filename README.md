# portapy

`portapy` is a easy to build version of embedded Python and the following packages for portable use on Windows that comes to around 36MB:

- [aiohttp](http://aiohttp.readthedocs.io/en/stable/)
- [async_timeout](https://github.com/aio-libs/async-timeout)
- [bson](https://github.com/mongodb/mongo-python-driver/tree/master/bson)
- [certifi](https://pypi.python.org/pypi/certifi)
- [chardet](https://pypi.python.org/pypi/chardet/3.0.4)
- [click](http://click.pocoo.org/5/)
- [flask](http://flask.pocoo.org/)
- [idlelib](https://github.com/python/cpython/tree/3.6/Lib/idlelib)
- [idna](https://pypi.python.org/pypi/idna)
- [jinja2](http://jinja.pocoo.org/docs/2.9/)
- [json](https://github.com/python/cpython/tree/3.6/Lib/json)
- [markupsafe](https://pypi.python.org/pypi/MarkupSafe)
- [multidict](https://github.com/aio-libs/multidict)
- [pymongo](https://pypi.python.org/pypi/pymongo)
- [pytz](https://pypi.python.org/pypi/pytz)
- [requests](http://docs.python-requests.org/en/master/)
- [strawpoll.py](https://pypi.python.org/pypi/strawpoll.py/)
- [urllib3](https://github.com/shazow/urllib3)
- [websockets](https://pypi.python.org/pypi/websockets)
- [werkzeug](http://werkzeug.pocoo.org/)
- [yarl](https://github.com/aio-libs/yarl)
- [itsdangerous](https://github.com/pallets/itsdangerous)
- [pluginbase](http://pluginbase.pocoo.org/)
- [six](https://pypi.python.org/pypi/six)

The build is intended to be structured well for a USB drive or a network drive. `portapy` is licensed under the GNUv3.0 license but the respective licence for each package is bundled with it.

## Building

In order to build, run build.py on a version of Python that is 3.0 or above.
