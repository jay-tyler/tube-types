# Tube Types
Sort of like pipes, except that we declare abstract relations between functions.

## Why? - Design Motivations
Thinking of this as a combination `extract function` and `extract variable` refactor forms.

A few different reasons.

Python is dynamically typed. That's great.
Some data doesn't fit well within a typing system anyways.
For instance, a US based telephone number is a value based paradigm for a `str`
type. You could wrap it in a type or a class, but that might be a bit heavy-handed.

And maybe, you want to accept any kind of phone number, but then be able to query
which kind of phone number it could be, at run time. This is a style of typing
commonly seen in Lisp-derived languages where every type comes with an instantiator,
e.g. `pair` and a type tester, e.g. `pair?`.

Also every time I need to create a regex, it's as though I'm doing it for the very
first time. Wouldn't it make more sense to create a value-testing function that
could be reused in multiple code bases?

## Contrast against other libraries
This library is meant to strongly emphasize extract type refactors and functional
composition.

There are a few different ways to "misuse" this paradigm (IMO):
1. Collapse tube types into overly dense, unreadable functional code
  - TODO: link to `onelinerizer`
2. Port in BASH shell like paradigms to Python

## Examples
See `examples.py` (for now).
