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

## "Functions" homework - September 21

For this assignment, you will use what you learned about functions and conditional statements to write some code that prints selected sentences from Donna Haraway's essay, "Cyborg Manifesto." Specifically, you will write a function which contains a conditional statement that checks for specific keywords, then prints out the quote associated with that keyword. If everything works correctly, when you call the function with a keyword, like "irony," the function will check the conditions and print out the quote ascribed to that keyword. Submit your file as a python file, with `.py` file extention. For some guidance, you can start by following the steps below.

First, define the function, called `quote_haraway`, with a parameter called `keyword`. I use these specific names but you can use whatever terms you like.

```python
def quote_haraway(keyword):
    [insert some code here] 
```

Second, write a conditional statement that checks for a specific keyword, for example:

```python
def quote_haraway(keyword):
  if keyword == "irony":
    print("Irony is about contradictions that do not resolve into larger wholes, even dialectically, about the tension of holding incompatible things together because both or all are necessary and true.")
```

Third, at least two more conditions, based on keywords of your choosing. 

Fourth, enter some code at the bottom of the script that calls the function. For example: `quote_haraway(irony)`. The final produce should look like this, but expanded to include more conditions:

```python
def quote_haraway(keyword):
  if keyword == "irony":
    print("Irony is about contradictions that do not resolve into larger wholes, even dialectically, about the tension of holding incompatible things together because both or all are necessary and true.")
    [add more conditions]

quote_haraway("irony")
```

BONUS: Expand your function by doing one or both of the following:
- add a loop to one of your conditions, maybe that makes the sentence uppercase or lowercase (with `upper()` or `lower()`)
- create a list of quotes at the top of the function, and use list indexing to pick out the relevant quote for each condition

## “Haunted House” homework - September 28

Expand the haunted house game [in this file]({static}/readings/haunted.py). You might add another door, or create more rooms beyond the existing ones. 

*Bonus: Read up on Python "while loops" and incorporate this loop into your game. This loop will allow you to stay longer in certain rooms, and add more options for responding to the prompt for those rooms.*
<br/><br/>

## "Text Cleaning" homework - October 19

Choose a text that you've read/seen before, maybe from the Project Gutenburg library. 

First, load up your text into a Jupyter notebook or Google Colab notebook. Use NLTK to clean the text by doing the following: remove stopwords, remove punctuation, and stem (and/or lemmatize) the words in the text.
<br/><br/>

## "Exploratory Text Analysis" homework - November 9

Get the text that you cleaned two weeks ago. First, turn the text into an NLTK Text object. Second, run 2 or 3 NLTK methods on the text. Try to use the results of one computation to inspire your next one. For example, you might use one or two of the words that appear when you run the `concordance()` or `generate()` method to explore `similar()`. Then, you might make a `disperson_plot()` of the results.

*Bonus: Write a short paragraph explaining how these results compare to your expectations, based on what you already know about the text. Are you surprised? What else would you want to do with this text using NLTK?*
<br/><br/>