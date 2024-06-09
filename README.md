# NotYourAndroid

## FAQ

### What is this Script?

This Script can find MyAndroid Servers that other People are connected to.

### How does it work?

When trying to connect to a Server, MyAndroid first sends a Request to generate a Service Name using a randomly generated Username to `https://www.myandroid.org/community/user.php`. This Request return a Service Name from which you can send a request to `https://www.myandroid.org/runapk/create-myandroid.php` which will give you the Server Username.

MyAndroid has 6 Servers in total. Their Usernames are `guest01` - `guest06` and their Passwords are `server0101` - `server0106`. By repeating the earlier mentioned Request we find out which Servers nobody is connected to. Because we know how many Servers there are, we can simply remove the ones that nobody is connected to and end up with the ones that People are connected to.
