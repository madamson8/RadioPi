# RECEIVER DOCUMENTATION

**All information should be encoded on arrival. The decryption key should only be stored in os memory.

The structure of data being received should be base64 ascii decoded to json like this:

{'o_type': 'type', 'data': 'your data here'}

> Main
> > set_operating_path(reg_path) - Set's operating path for the receiver.
> 
> > get_operating_path() - returns current operating path for the receiver.
> 
> > set_operating_type() - determine the type of data being decoded.
