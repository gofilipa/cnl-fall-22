Title: Homework
Date: 2022-08-28 21:00
Modified: 2022-08-28 21:00
Category: Homework
Tags: 
Slug: homework
Authors: Filipa Calado
Summary: Homework prompts and challenges

# Reading Responses

On weeks that you have a Reading Response due, you will submit a short reading response (approximately 300 words, or 1 full page) due on Tuesday night at midnight, the evening before class.

For this assignment, choose one moment from the reading that struck you in some way. What did you find compelling about this moment? How might it relate to our class readings or discussions? How does it deepen your thinking about coding or language?

The reading response is meant to get you to think deeply about the readings and prepare you for class discussion. They will be graded as Pass, Fail, or Zero.

# Coding Homework

On weeks where you do not have a Reading Response, you will have coding homework. These are short coding challenges based on the previous class instruction. You will not be graded on how well you code, but on your engagement and attempt at the challenge. That being said, these assignments will also offer opportunities for you to customize, extend, or go further with your solutions, which is entirely up to you.

If you run up against obstacles, remember that errors are our friends. They often offer us clues for debugging. In the case that you are really stuck, do not be discouraged, but think of it as an opportunity to bring up for class discussion. To reiterate, you will be graded on making the attempt, not on being "correct."
<br/><br/>

## “Errors” homework - September 14
As you experiment on the Python interpreter, create four errors: two syntax errors and two traceback errors. For each error, explain the error in your own words. Then, debug the error, providing a corrected expression. When trying to understand the error, remember to pay special attention to the caret and error message.

Be sure to define the specialized terms or language (like `EOL` or `literal`) in your explanation. See below for example responses, and check [this page for a refresher on errors in Python](https://curriculum.dhinstitutes.org/workshops/python/lessons/?page=5). 

Copy and paste your code into a Word document, where you will type your explanations and solutions (the formatting when you copy/paste may be a bit wonky, but don't worry about it). 

### Error #1
```console
>>> %greeting = "Hello World"
  File "<stdin>", line 1
    %greeting = "Hello World"
    ^
SyntaxError: invalid syntax
```
Explanation: The syntax error occured because the expression begins with a special character. Python only allows variables to begin with letters, not special characters or numbers.

Solution:
```console
greeting = "Hello World"
```

### Error #2
```console
>>> greeting = "hello" + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Explanation: Different data types like a string and an integer cannot be added (or "concatenated") together. Python can only add two of the same data type.

Solution:
```console
>>> greeting = "hello" + " goodbye"
hello goodbye
```


<br/><br/>

## “Loops” homework - September 21

Here’s a list of numbers:

```
prime_numbers = [2, 3, 5, 7, 11]
```

Write some code to print out the square of each of these numbers. Remember that the square of a number is that number times itself.

Next, look up a new concept—"f-string" (a formatting technique for strings)—on Google and use it to write a loop that gives the following output:

```
The square of 2 is 4.
The square of 3 is 9.
The square of 5 is 25.
The square of 7 is 49.
The square of 11 is 121.
```
<br/><br/>

## “Haunted House” homework - September 28

Expand the haunted house game [in this file]({static}/readings/haunted.py). You might add another door, or create more rooms beyond the existing ones. 

*Bonus: Read up on Python "while loops" and incorporate this loop into your game. This loop will allow you to stay longer in certain rooms, and add more options for responding to the prompt for those rooms.*
<br/><br/>

## "Frequency Distribution" homework - October 19

Choose a text from the Project Gutenburg library that you've read before. 

First, clean the text, removing stopwords, punctuation, and stemming (and/or lemmatizing) the remaining words. Second, turn the text into an NLTK Text object. Finally, run two or three NLTK methods on the text.

*Bonus: Write a short paragraph explaining how these results compare to your expectation from reading the book. Are you surprised? What else would you want to do with this text using NLTK?*
<br/><br/>

## “Lexicon and Parser” homework - November 2

TBD