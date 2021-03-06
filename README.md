# real_time_api
An example websocket API built on Python, Tornado and MongoDB

### Motivation
This project is a brief demonstration of a websocket interface to a key/value store based on the following notional business requirements:

Create a service that exposes standard key/value store operations over a websocket interface. 
Requirements and API spec below.

 - Use Python Tornado as the web server framework
 - Use MongoDB for storage
 - Use Motor client for Mongo, it is asynchronous and plays nicely with the Tornado ioloop
 - Take MongoDB connection string as configuration value
 - You can use Mongo on localhost for development or create a free hosted DB at https://mongolab.com/

Real Time API:

`WS /connect`

Used to initiate a websocket connection with the server. Once connected, clients can send messages to the server and receive responses.  Server should send “hello” message as soon as the connection is established

Supported Messages:

`get {key}`

Gets the value of a key from K/V store. If the key does not exist in the K/V store, server returns “null”.

`set {key} {value}`

Sets the value of a key to a give value in the K/V store. Returns ‘ok’ on success and a descriptive error string for any error cases.

Example session:
```bash
12:17:17	command:	/connect ws://localhost:8000/connect
12:17:17	received:	hello
12:17:54	command:	/send get\ foo
12:17:54	sent:	    get foo
12:17:54	received:	null
12:18:07	command:	/send set\ foo\ hello,\ world!
12:18:07	sent:	    set foo hello, world!
12:18:07	received:	ok
12:18:10	command:	/send get\ foo
12:18:10	sent:	    get foo
12:18:10	received:	hello, world!
```

### Operation
1. Install Python 3.4 and the dependencies in the requirements file (`pip install -r requirements.txt`)
2. Install and start an instance of MongoDB locally.  Alternatively, you may use an instance hosted remotely, but you'll need to change the connection URI in the `settings.py` file.
3. `python ./server.py`

### Contributions
Contributions and feedback are always welcome - just send me a pull request.

### License
Use of this software is governed by the MIT license [here](LICENSE).
