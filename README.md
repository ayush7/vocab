# New Language Vocabulary Builder
### An app for storing new words and revising them through flash cards in any language. 

## The use case
I am trying to learn and improve several languages (Japanese and French), and one of the key things required to get better is to expand one's vocabulary. After a point, understanding and remembering grammatical rules is easy but to really be able to express oneself and understand _anything_, one needs to have a sound vocabulary. I usually try to read newspapers, blogs and literature in other languages and almost always come across new words. I've been writing these down but soon realized that this would cause my notebook to explode and there wasn't any real good way to revise these. Hence, the idea for this app.

## Tech Stack and solution
I'll be building this as a webapp which is easily accessible on my phone, and hosting it on my remote gCloud instance. I'll be using mongodb as the database, mostly because I imagine the schema changing from time to time as I come up with new stuff, and I didn't want to be bothered with building a relational schema (overkill for such a simple project). I also will be using Flask as the server since I'm most proficient in python and it's easy for me to whip something up (probably should use this opportunity to practice nodejs but will not). The present system has been hardcoded to use French and Japanese, but you can easily add more languages. 

## Setup

* Create a `.env` local file as a copy of `.env.exmaple`, filling in the given environment variables. Only `INSERT_SECRET` would have to be given a value.
* Run `app.py` after installing the necessary things using `pip install --user flask Flask-PyMongo`
* I deployed it using gunicorn and nginx using the instructions given here

## View demo
The demo of my (evolving) vocabulary database is [here](http://35.233.144.45/). 
