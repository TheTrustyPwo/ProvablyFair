# ProvablyFair
A Provably Fair number generator

##What is this?
This is a really simple but useful random number generator. It uses cryptographic ways
to generate and ensure that the server cannot generate a number that is in their favour.

##How does it work?
The number is generated with 3 parameters - the server seed, client seed and the nonce.
Out of these, we will only show the user the SHA256 hash of the server seed used. The client
is able to modify the client seed to their own liking. The nonce can be used in different ways: It
could be the user has rolled (This ensures a nonce can never be used twice on one client), or it could
just be a timestamp. It ensures an extra layer of security to the system. The nonce, will of course
be shown to the client as well, leaving only the server seed unknown to the client until after the
number has been generated. After the number has been generated and all parameters used to generate number
has been shown to the client, the client can then verify the number by using the following algorithms.

##How do we generate the number?
Assuming we are generating a number between 1 and  100, we would use the following way:
```
Two strings are created:
STRING1 = "[MODIFIER]:[SERVER SEED]:[MODIFIER]"
STRING2 = "[MODIFIER]:[CLIENT SEED]:[MODIFIER]"
Then HMAC-SHA512 is used to hash STRING1 with STRING2 as the secret key, giving us a 128 character hex string.
The first 8 characters of the hex string are taken and converted to a decimal. 
This decimal is then divided by 42949672.95 and rounded off to the nearest whole number.
This whole number is used as the secret, with the maximum possible value being 100
```

##Applications
This system is mainly used in the digital world, such as online gambling, giveaways, contests,
fraud prevention and manipulation with predictable transactions on exchanges