# c2srv

This will be an attempt at building a limited function C2 channel.  This is more a learning experiance for me than an attempt to build something truly useful.

### Components
A server side app (<b>c2http.py</b>) that will feed commands to and receive results from a client side app (<b>c2cli.py</b>)

## c2http.py
A simple 'server' that utilizes the http protocol to serve encoded windows commands to the client.
The 'server' will also decode the encoded results.

## c2cli.py
A simple 'client' side app that will make an http connection, through a proxy, out to the the 'server' side app. 
After the connection has been established it will receive commands encoded in the data section of the http packet, that will be decoded and executed .  The results of the command(s) will be encoded and sent back to the 'sever' side.

    
````bash
  Client:                                           Server:
  c2cli.py                                          c2http.py
+-----------------+   HTTP Connection Established  +-----------------+
|                 +-------------------------------->                 |
| +-------------+ |      Encoded CMDs              | +--------+      |
| |Decode CMD   <-|--------------------------------|-|cmd.html|      |
| |Execute CMD  | |      Encoded CMD Output        | +--------+--+   |
| |Encode Output+-|--------------------------------> |Results.txt|   |
| +-------------+ |                                | +-----------+   |
+-----------------+                                +-----------------+
````
    



