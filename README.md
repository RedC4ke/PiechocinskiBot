# PiechocinskiBot
A simple Markov's chain bot to generate fake Janusz Piechocinski sentences with the use of Markovify and spaCy Python libraries. 

Implementation:
https://facebook.com/piechocinskibot

Usage:

1.1 Put your text into "src/sources.txt" file.

1.2 If you want the app to post regular messages to your Facebook page, you'll need to put environmental variables such as Graph API secret token and Graph API User Token.
 
2. Run the ModelFactory script. 

3. Run the app.


If you want to just preview the sentences, you can use the demo script.
Docker deploy script should work for everyone, but you may want to change deployment script, as it is designed to use remote Azure container from my local machine. 
