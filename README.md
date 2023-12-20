![](https://uwe-cyber.github.io/images/uwe_banner.png)

# Future Funfair

This repository holds the code for the **Coding for network security Making Microbits useful** project run by the [University of the West of England (UWE)](https://www.uwe.ac.uk/). 

The project itself usses the [micro:bit radio](https://makecode.microbit.org/reference/radio) functionality to work from insecure to paried and encrypted communication between micro:bits (v2).

### Simple Radio

A simple radio setup that broadcasts messages out - Any device with the same radio config can listen and return messages.

### Paired Radio

A more complex radio setup that uses pairing. Two micro:bits need to pair to be able to communicate with each other. Radio configs are randomly generated and shared during pairing. However messages are still sent in plaintext.

### Paired and Encrypted Radio

Building on the pairing now messages are encrypted and decrypted on send and receive. However this is done using a hardcoded encryption key.
