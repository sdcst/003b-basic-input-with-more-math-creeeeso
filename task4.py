#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""

import math

a = input("Enter a person's name: ")
b = input("Enter an adjective: ")
c = input("Enter a food: ")
d = input("Enter another adjective: ")
e = input("Enter a noun: ")
f = input("Enter the name of a place: ")
g = input("Enter a verb: ")
h = input("Enter an adverb: ")
i = input("Enter another food: ")
j = input("Enter a thing: ")


print(f"Today we picked apple from {a}'s Orchard. I had no idea there were so many different varieties of apples. I ate {b} apples straight off the tree that tasted like {c}. Then there was a {d} apple that looked like a {e}. When our bag was full, we went on a free hay ride to {f} and back. It ended at a hay pile where we got to {g} {h}. I can hardly wait to get home and cook with the apples. We are going to make apple {i} and {j} pies!.")