# Code2040Challenge

##Libraries Used
[Requests](http://docs.python-requests.org/en/latest/)

I personally loved working with Requests because it made sending and receiving JSON information simple.

[Dateutil](https://pypi.python.org/pypi/python-dateutil)

Dateutil is a lifesaver because it made dealing with complicated ISO dates uncomplicated. It easily turned the ISO 8601 string to a datetime object and then back again after I added the interval.

##Reflections
I'm really proud about how few lines of code I used to complete the project. I learned about the two amazing libraries mentioned above, Requests and DateUtil.
I have dealt with JSON information before using the jSoup library when I made my DailyQuotes application this summer with Java, but had never dealt with JSON information in Python. 
It was very interesting seeing how the two languages and libraries dealt with JSON. I learned about extended slice
syntax, which prevented me from having to make a for loop, which would clutter the code. I learned about a lot of other Python methods
too, like index and find, that helped me make my code simpler. I plan to use them for future Python projects.
I aimed for readability, accuracy, and commented my code when I needed
to clarify things. This challenge took me about three hours to complete. 

The hardest part was probably Step 4. I tried doing it without using an external library and it proved difficult. When I tried to
convert the string into a datetime object, Python kept complaining that my format was wrong. Knowing that there was an easier way to do this,
I went online and searched for an external library to use. I found DateUtil and it worked like a charm. In about 10 minutes, my code outputted the correct result. I
learned that external libraries are very useful and that the open source community has many libraries that are designed to make life
easier. You just have to be willing to look.
