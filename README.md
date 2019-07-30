# github\_index

A bit of a meta-project on creating a nicer index of my github repositories.
Partially motivated because I'm too greedy to do with only 6 pinned
repositories. It's just about stable enough to function (on my personal
convention for my repositories). It features several sub-utilities I chain
together, including directory-searching and API-json reading. It files my
projects under subcategories, and concatenates together readmes under a category
heading. It was also about familiarising myself with Markdown (generating
headers, normalising header names in links to contents, tables etc). It features
just about the right combination of absolute and relative links that the readme
source is in-place stable. Now featuring disgusting links at the start of each
header to jump back to the table of contents - I'm not a web designer leave me
alone.
## Table of Contents
- [Miscellaneous programming](#toc-miscellaneous-programming)
    - [Postscript](#toc-postscript)
    - [scratch](#toc-scratch)
    - [backtobasics](#toc-backtobasics)
    - [programming\_challenges](#toc-programming\_challenges)
    - [python\_demo](#toc-python\_demo)
    - [microbit](#toc-microbit)
    - [autobiographical\_integers](#toc-autobiographical\_integers)
    - [factors\_multiples](#toc-factors\_multiples)
    - [tile\_encodings](#toc-tile\_encodings)
- [Miscellaneous other](#toc-miscellaneous-other)
    - [dotfiles](#toc-dotfiles)
    - [physics](#toc-physics)
    - [maths](#toc-maths)
- [Assignments](#toc-assignments)
    - [palindromes](#toc-palindromes)
    - [assignment\_guessing](#toc-assignment\_guessing)
    - [anagrams](#toc-anagrams)
    - [encryption](#toc-encryption)
    - [noughtsandcrosses](#toc-noughtsandcrosses)
    - [GUIssing](#toc-guissing)
    - [pesten](#toc-pesten)
- [Miscellaneous Python projects](#toc-miscellaneous-python-projects)
    - [Sudoku](#toc-sudoku)
    - [Calcudoku](#toc-calcudoku)
    - [A453](#toc-a453)
    - [Linked lists](#toc-linked-lists)
    - [Cube](#toc-cube)
    - [Punnet Squares](#toc-punnet-squares)
    - [cookies](#toc-cookies)
    - [Yahtzee](#toc-yahtzee)
    - [queens](#toc-queens)
    - [hangman](#toc-hangman)
    - [points](#toc-points)
    - [DNA](#toc-dna)
    - [cipher\_tools](#toc-cipher\_tools)
    - [sorting](#toc-sorting)
    - [elf\_game](#toc-elf\_game)
    - [double\_pendulum](#toc-double\_pendulum)
    - [flippy\_bot](#toc-flippy\_bot)
    - [fizzbuzz](#toc-fizzbuzz)
    - [1r1l1e](#toc-1r1l1e)
    - [nctfe](#toc-nctfe)
- [java-processing projects](#toc-java-processing-projects)
    - [alphabet](#toc-alphabet)
    - [balls](#toc-balls)
    - [cars](#toc-cars)
    - [circles](#toc-circles)
    - [colourconway](#toc-colourconway)
    - [mazes](#toc-mazes)
    - [pendulums](#toc-pendulums)
    - [pixel\_sorting](#toc-pixel\_sorting)
    - [pythanimated](#toc-pythanimated)
    - [rainbow\_lines](#toc-rainbow\_lines)
    - [regen\_soup](#toc-regen\_soup)
    - [shading](#toc-shading)
    - [snowflakes](#toc-snowflakes)
    - [square\_filling\_circle](#toc-square\_filling\_circle)
    - [UI\_demo](#toc-ui\_demo)
    - [turtles](#toc-turtles)
    - [s\_zoom](#toc-s\_zoom)
    - [sandpiles](#toc-sandpiles)
    - [platformer](#toc-platformer)
    - [snake](#toc-snake)
    - [spaceinvaders](#toc-spaceinvaders)
    - [tetris](#toc-tetris)
    - [sierp\_demo](#toc-sierp\_demo)
    - [chaos\_spreadsheet](#toc-chaos\_spreadsheet)
    - [moire\_draggable](#toc-moire\_draggable)
    - [julia](#toc-julia)
    - [mandelbrot](#toc-mandelbrot)
    - [mandemthot](#toc-mandemthot)
    - [whomping\_fractal](#toc-whomping\_fractal)
    - [koch\_magnet](#toc-koch\_magnet)
- [Python-processing projects](#toc-python-processing-projects)
    - [asteroids](#toc-asteroids)
    - [collatz\_tree](#toc-collatz\_tree)
    - [bounce\_3d](#toc-bounce\_3d)
    - [bubbles](#toc-bubbles)
    - [perl](#toc-perl)
    - [drag\_grav](#toc-drag\_grav)
    - [kaleidoscope](#toc-kaleidoscope)
    - [lightning](#toc-lightning)
    - [bfs\_koch](#toc-bfs\_koch)
    - [stepbysierp](#toc-stepbysierp)
    - [py\_lerpbez](#toc-py\_lerpbez)
    - [road\_screen](#toc-road\_screen)
    - [rubiks\_cube](#toc-rubiks\_cube)
    - [ship\_game](#toc-ship\_game)
    - [wind\_fans](#toc-wind\_fans)
    - [langton](#toc-langton)
    - [squiggles](#toc-squiggles)
    - [tenprint](#toc-tenprint)
    - [mod\_mult](#toc-mod\_mult)
    - [lsystems](#toc-lsystems)
    - [pong](#toc-pong)
    - [radial\_oscillation](#toc-radial\_oscillation)
    - [ascii\_art](#toc-ascii\_art)
    - [hanoi](#toc-hanoi)
    - [mandeldot](#toc-mandeldot)
    - [gcd\_plot](#toc-gcd\_plot)
    - [bifurcation\_logistic\_map](#toc-bifurcation\_logistic\_map)
# [\[toc\]](#table-of-contents) Miscellaneous programming
### [\[toc\]](#table-of-contents) [Postscript](https://github.com/goedel-gang/Postscript)
Some of my Postscript (the printer language) projects - some early, some less so. `zut` means pile of rubbish. There's lots to do with polysymmetry and fractals, and then some other stuff. Postscript is actually a really fun language for static graphics programming - I love its syntax, model of stack frames (you have to manually push a new local namespace dictionary to the stack). It's powerful - featuring programmatic features like for loops, while maintaining good drawing primitives and vector graphics. It's actually pretty good for fractals, but also polysymmetric tilings and more. Here are a couple of my favourites:

A recursive Penrose tiling (which will never form a repeating pattern):

![screenshot](https://github.com/goedel-gang/Postscript/blob/master/svgs/penrose.svg)

A "sierpinski star". Similar to Sierpinski's triangle/gasket, except it must be mutually recursive in hexagon segments and triangle segments.

![screenshot](https://github.com/goedel-gang/Postscript/blob/master/svgs/ster.svg)

The Minkowski sausage fractal. Lesser known but quite pretty fractal, with a very nice fractal looking boundary.

![screenshot](https://github.com/goedel-gang/Postscript/blob/master/svgs/minkowski.svg)

Stars formed by choosing equidistant points around the circumference of a circle and drawing a star by "skipping" over some number of points for each line segment. Uses coprimality to produce a nice looking pattern - ie 9 points with a skip of 3 would just be a triangle so would be boring.

![screenshot](https://github.com/goedel-gang/Postscript/blob/master/svgs/star2.svg)

A few more that I really converted to svg to add here, but realised this readme was getting clunky. I moved them to a directory of SVGs (they should be viewable in browser): [svgs](https://github.com/goedel-gang/Postscript/blob/master/svgs/). There are also `pdf` files, but they don't seem to render very well. They're there because they're a necessary intermediate stage to my SVG generation method - I first use `ps2pdf`, and then `pdf2svg`. It seems to be working quite well so it's good enough for me. I've tested that all of these work with my version of GhostScript - you should also be able to open them in Preview on MacOS or some kind of illustrator/graphics program. These are only a couple of my favourites - the decision making process was like being forced to choose between my own children. I tried to pick some varied projects showing different possible projects in Postscript, although really I like everything that isn't in `zut` that's here.
### [\[toc\]](#table-of-contents) [scratch](https://github.com/goedel-gang/scratch)
Some Scratch projects. Ranges from an implementation of air resistance, gravitational acceleration and an explictly lagged paddle to merge sort, integer base conversion and Sierpinski's triangle. Features the zip archive, and JSON project extracted from the zip archive as a matter of interest.

Here is a base conversion, from ZZ\\36 to hex.

![screenshot](https://github.com/goedel-gang/scratch/blob/master/screenshots/base_conversion.png)

Here it's performed a mergesort on the prime numbers:

![screenshot](https://github.com/goedel-gang/scratch/blob/master/screenshots/mergesort.png)

Here is a static snapshot of pong:

![screenshot](https://github.com/goedel-gang/scratch/blob/master/screenshots/pong.png)

Here is a multicoloured sierpinski's gasket:

![screenshot](https://github.com/goedel-gang/scratch/blob/master/screenshots/sierp.png)
### [\[toc\]](#table-of-contents) [backtobasics](https://github.com/goedel-gang/backtobasics)
Some Python basics should any of my one audience members wish to refer to them. The main goal is to provide lots of accessible examples of basic Python functionality/syntax and make a reasonably usable index of these examples. Features simple examples of code, with mildly explanatory comments. For example, a demonstration of a validation function that takes a parser function as an argument (using while-loops and try-except, docstring omitted):

```Python
def get_type(ty, msg):
     while True:
         try:
             val = ty(input(msg))
         #if a value error is raised, print it and carry on
         except ValueError as ve:
             print(ve)
         else:
             #if it all goes fine return the value (this breaks from the loop and function)
             return val
```

Veel plezier `: )`

Possibly in future featuring other languages.
### [\[toc\]](#table-of-contents) [programming\_challenges](https://github.com/goedel-gang/programming_challenges)
Various programming challenges (for now just populated by my solutions to the BIO 2017).
### [\[toc\]](#table-of-contents) [python\_demo](https://github.com/goedel-gang/python_demo)

Run noughtsandcrosses/play.py to play noughts and crosses against computer.

waves.py slowly produces several different types of wave.

fractals.py for fractals in Turtle using Lindermayer systems - meaning each
fractal is coded in just a couple of lines of definitions.

Fractals.py is a very nicely implemented framework for L-systems, where I have
then proceeded to plug in some L-system definitions for wikipedia. It's been
further tidied up and extended to use the Processing runtime and draw them in
rainbow colours at <https://github.com/goedel-gang/lsystems>.

![screenshot](https://github.com/goedel-gang/python_demo/blob/master/win_screenshot_20190330_121915.png)
![screenshot](https://github.com/goedel-gang/python_demo/blob/master/win_screenshot_20190330_122012.png)
![screenshot](https://github.com/goedel-gang/python_demo/blob/master/win_screenshot_20190330_122102.png)

Perhaps a way to expand this, if you have time, is to allow the user to specify
the number of iterations to perform. You could also look for other fractals to
add.

see <https://github.com/goedel-gang/github_index> for general good times

Good Processing things to show people:

If you don't have Git installed, you'll probably need to download ZIP files and
unzip them, then making sure they're in a directory with the same name as the
`/.*\.py?de/` file, or Processing will refuse to open.

For the second lot, make sure to have installed Python mode (this should not
require admin access).

- <https://github.com/goedel-gang/mandelbrot>
- <https://github.com/goedel-gang/turtles>
- <https://github.com/goedel-gang/pythanimated>
- <https://github.com/goedel-gang/mazes>
- <https://github.com/goedel-gang/pendulums>
- <https://github.com/goedel-gang/colourconway>
- <https://github.com/goedel-gang/circles>

- <https://github.com/goedel-gang/kaleidoscope>
- <https://github.com/goedel-gang/rubiks_cube>
- <https://github.com/goedel-gang/sorting>
- <https://github.com/goedel-gang/bubbles>
- <https://github.com/goedel-gang/ship_game>
- <https://github.com/goedel-gang/lsystems>
- <https://github.com/goedel-gang/pong>
- <https://github.com/goedel-gang/radial_oscillation>

see <https://github.com/goedel-gang/Postscript/blob/master/README.md>
for Postscript fractals and other geometrical patterns.
### [\[toc\]](#table-of-contents) [microbit](https://github.com/goedel-gang/microbit)
Featuring mandelbit, an implementation of a Mandelbrot set renderer on a 5x5
Microbit grid.

![picture](https://github.com/goedel-gang/microbit/blob/master/mandelbrot.jpg)
### [\[toc\]](#table-of-contents) [autobiographical\_integers](https://github.com/goedel-gang/autobiographical_integers)
Programs to search for [autobiographical integers](https://oeis.org/A138480).
### [\[toc\]](#table-of-contents) [factors\_multiples](https://github.com/goedel-gang/factors_multiples)
Aiming to optimise the [NRich problem](https://nrich.maths.org/5468/solution)
for length, by various graphical algorithms.

The first approach was to implement a brute force DFS and leave this to run. I
quickly found that that was intractable, although really I knew that all along -
it was more about having something to implement in code, for the fun of it. I
also spent some time optimising it for speed, by for example pre-computing the
whole graph representing the board and using fast data-structures where possible
(favouring arrays, eg boolean array of visited locations and array of current
path.)

I modified this to instead traverse the board randomly. This quickly got some
better results. I also reimplemented this program in C rather than Python, to
gain about an order of magnitude of speed. I also wrote some utility programs
that try to naïvely or greedily insert remaining tiles between current tiles, or
to highlight the connected subgraphs within remaining tiles. However, with all
of this I was only able to generate a path of length 69.

I then spent a bit of time looking at the properties of my current solutions and
the better published solutions. I saw that they often included long "chains"
of multiples of large numbers, eg multiples of 17. I designed a simple heuristic
to emulate this behaviour, which is that the program tries to maximise the GCD
between adjacent elements. If two candidates have the same GCD, they are
randomly chosen between. Using this in conjunction with the greedy expansion
utility I generated the following sequence:

    >[76]58 29 87 3 69 23 92 46 2 62 31 93 1 35 70 10 40 80 20 100 50 25 75 15 45 90 30 60 12 96 48 24 72 36 18 54 27 81 9 63 21 42 84 28 56 14 98 49 7 91 13 52 26 78 6 66 33 99 11 44 22 88 8 16 32 64 4 76 38 19 95 5 85 17 68 34

![screenshot](https://github.com/goedel-gang/factors_multiples/blob/master/screenshot.png)

There are 10 primes between 50 and 100: 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
Only one of these can be used (via the 1), so this implies a weak upper bound of
91 as a chain length. My attempt is still pretty far from that and my program
isn't particularly sophisticated, and I've not actually had a go at
hand-optimising anything so I reckon it's still possible to get a much better
score.

Non-rigorously, I performed some exhaustive searches of lower board sizes which
might suggest that around 85 is a more reasonable goal:

    In [1]: 23 / 27, 24 / 28, 24 / 29, 26 / 30
    Out[1]:
    (0.8518518518518519,
     0.8571428571428571,
     0.8275862068965517,
     0.8666666666666667)
### [\[toc\]](#table-of-contents) [tile\_encodings](https://github.com/goedel-gang/tile_encoding)
Solving the following problem:

Given a series of N random bits (N could be 4 or 64), toggle exactly one bit
such that you have encoded an integer in {0..N-1}.

Phrased as a magic trick, you arrange for example 64 cards which are black on
one side, and white on the other in a square. You let the target randomly flip
all of the cards, and then select a particular cards (say, by placing some money
under it). You then flip exactly one card. At this point, your accomplice, who
has been out of the room the whole time, comes in and "immediately" determines
which card is the target. This involves no tricks (well, a bit of information
theory).

This repository contains [programs to solve][1] this problem, and a
[document detailing my exact solution][2].

There is also a Processing sketch, but the pretty screenshots of it may contain
spoilers so go [here][3] to see it.

[1]: https://github.com/goedel-gang/tile_encoding/blob/master/src/magic_encode.py
[2]: https://github.com/goedel-gang/tile_encoding/blob/master/SOLUTION.md
[3]: https://github.com/goedel-gang/tile_encoding/blob/master/DOCUMENTATION.md
# [\[toc\]](#table-of-contents) Miscellaneous other
### [\[toc\]](#table-of-contents) [dotfiles](https://github.com/goedel-gang/dotfiles)

These are my dotfiles, maintained in Git using

<https://developer.atlassian.com/blog/2016/02/best-way-to-store-dotfiles-git-bare-repo/>

    alias cfg='/usr/bin/git --git-dir="$HOME/.cfg/" --work-tree=$HOME'
    cfg config --local status.showUntrackedFiles no
    git clone --bare "https://github.com/goedel-gang/dotfiles" "$HOME/.cfg"
    # cfg stash
    cfg checkout
    cfg submodule update --init

Of course they should be considered an entirely volatile, possibly hostile work
in progress.

![screenshot](https://github.com/goedel-gang/dotfiles/blob/master/.github/README_GRUVBOX.png)

How it has looked at some point in the past:

![screenshot](https://github.com/goedel-gang/dotfiles/blob/master/.github/README_SOLARIZED.png)
![screenshot](https://github.com/goedel-gang/dotfiles/blob/master/.github/README_SOLARIZED_OLD.png)
### [\[toc\]](#table-of-contents) [physics](https://github.com/goedel-gang/physics)
All my physics stuff. Currently some experimenting with LaTeX and not much else.
### [\[toc\]](#table-of-contents) [maths](https://github.com/goedel-gang/maths)

A document of some description of sorts, with some maths in. Mostly for fun and
learning LaTeX.

Features some dangerously nice typesetting, and some atrociously bad
typesetting. One day I might understand how to use TiKz, but for now
`chi_t_notes/` is all you're getting.
# [\[toc\]](#table-of-contents) Assignments
### [\[toc\]](#table-of-contents) [palindromes](https://github.com/goedel-gang/palindromes)

Assignment on palindromes in Pascal. The version that I handed in can be found
on the [hand-in tag](https://github.com/goedel-gang/palindromes/tree/hand-in).
### [\[toc\]](#table-of-contents) [assignment\_guessing](https://github.com/goedel-gang/assignment_guessing)

The "guessing game" assignment. The version I handed in can be viewed on the
[hand-in tag](https://github.com/goedel-gang/assignment_guessing/tree/hand-in).
### [\[toc\]](#table-of-contents) [anagrams](https://github.com/goedel-gang/anagrams)

Assignment on anagrams in Pascal. The version that I handed in can be found at
the [hand-in tag](https://github.com/goedel-gang/anagrams/tree/hand-in).
### [\[toc\]](#table-of-contents) [encryption](https://github.com/goedel-gang/encryption)

Assignment on textfiles/encryption. Find what I handed in upon the
[hand-in tag](https://github.com/goedel-gang/encryption/tree/hand-in).
### [\[toc\]](#table-of-contents) [noughtsandcrosses](https://github.com/goedel-gang/noughtsandcrosses)

A CLI noughts and crosses framework in Python. It looks something like this:

	   0  1  2 
	0   |   |   
	 ---+---+---
	1   |   |   
	 ---+---+---
	2   |   |   
	You are playing as noughts
	Enter the position you want to play in > 1 1
	   0  1  2 
	0   |   |   
	 ---+---+---
	1   | O |   
	 ---+---+---
	2   |   |   

Minmax is also implemented - see `writeup`. The version I handed in can be
seen at the
[hand-in tag](https://github.com/goedel-gang/noughtsandcrosses/tree/hand-in).

The serious source code is in `src`. Use `python3 src/play.py -c` to play
against a computer. I also tacked on a ""minimalist"" UI in Processing. The
source code for this is at the top level because of the way Processing like
folders to be. It's generally a little botched because I had to translate things
to Python 2.

![screenshot](https://github.com/goedel-gang/noughtsandcrosses/blob/master/win_screenshot_20180712_110639.png)
### [\[toc\]](#table-of-contents) [GUIssing](https://github.com/goedel-gang/GUIssing)
GUI for the
[assignment\_guessing](https://github.com/goedel-gang/assignment_guessing)
project, developed under duress.

See the version I handed in at the
[hand-in tag](https://github.com/goedel-gang/GUIssing/tree/hand-in)
### [\[toc\]](#table-of-contents) [pesten](https://github.com/goedel-gang/pesten)

Programming assignment on OOP card games, namely "pesten". See the version I
handed in within the
[hand-in tag](https://github.com/goedel-gang/pesten/tree/hand-in).
# [\[toc\]](#table-of-contents) Miscellaneous Python projects
### [\[toc\]](#table-of-contents) [Sudoku](https://github.com/goedel-gang/sudoku)
A (brute-force) sudoku solver in Python. It models a Sudoku as a list (array under the hood) of length 81. It generates a further two-dimensional array (`[81][21]`), which maps cell locations to all other cell locations that that cell can "see". An empty cell takes the conveniently unused value of 0. Input sudoku is read from stdin, and should simply consist of 81 whitespace separated digits. The program comes with an option (`-e`) to print an "empty" sudoku for ease of entering a sudoku. With this as input (`ex.txt`)::

    0 0 0  2 6 0  7 0 1
    6 8 0  0 7 0  0 9 0  
    0 9 0  0 0 4  5 0 0  

    8 2 0  1 0 0  0 4 0  
    0 0 4  6 0 2  9 0 0  
    0 5 0  0 0 3  0 2 8

    0 0 9  3 0 0  0 7 4
    0 4 0  0 5 0  0 3 6
    7 0 3  0 1 8  0 0 0  

Done with this command:

    $ time cat ex.txt | python solve.py 

Produces, in a very respectable time-frame:

    4 3 5  2 6 9  7 8 1  
    6 8 2  5 7 1  4 9 3  
    1 9 7  8 3 4  5 6 2  

    8 2 6  1 9 5  3 4 7  
    3 7 4  6 8 2  9 1 5  
    9 5 1  7 4 3  6 2 8  

    5 1 9  3 2 6  8 7 4  
    2 4 8  9 5 7  1 3 6  
    7 6 3  4 1 8  2 5 9  


    cat ex.txt  0.00s user 0.00s system 0% cpu 0.003 total
    python3 solve.py  0.04s user 0.00s system 90% cpu 0.044 total

Of course, it's a stupid solver so if you give it a problem engineered to work against it the universe will probably collapse before it's finished.
### [\[toc\]](#table-of-contents) [Calcudoku](https://github.com/goedel-gang/Calcudoku)
A simple brute force solver for an 8\*8 'calcudoku'. A `Calcudoku` is given a number of *regions*, with *targets* and *operations*. A region is a set of adjacent cells (although the program could handle non-adjacent cells), where they are given an operation and a target. The Target is an integer which must be reached by combining the integers in the cells using the operation, ie:

    target = 6

operation | explanation
--- | ---
`+` | The numbers should add up to 6.
`-` | The largest number subtract *all* the rest of the numbers should be 6.
`*` | The product of the numbers should be 6.
`/` | The largest number divided by *all* the rest of the numbers should be 6.

These regions are modelled in a pretty nicely structured OO model.

Input works like so: each region is defined and assigned to a character, and then a grid of characters is provided. You can refer to [ex.txt](https://github.com/goedel-gang/Calcudoku/blob/master/ex.txt) for a fully specified input file. Using it as input, with `cat ex.txt | python interf.py`, this output is produced:

    8 5 7 1 4 2 3 6 
    7 3 4 5 6 1 2 8 
    4 7 2 3 8 6 1 5 
    3 1 8 6 2 4 5 7 
    5 8 6 2 7 3 4 1 
    6 2 1 4 5 8 7 3 
    2 6 3 7 1 5 8 4 
    1 4 5 8 3 7 6 2 
### [\[toc\]](#table-of-contents) [A453](https://github.com/goedel-gang/A453)
From my GCSE computing course - see [my full writeup](https://github.com/goedel-gang/A453/blob/master/writeup.pdf) (be warned - it's big. I'd recommend downloading it rather than viewing it inline - I've crashed a couple of browser sessions by trying the latter). It's a **heavily** type-annotated collection of scripts in Python, which perform various forms of naive and less naive compression on text. It initially uses a very naive system of building an index of words and writing "pointers" to words in that index, where the pointers are space-separated base-10 integers in ASCII. This is of course a tremendous waste of a byte - I later go on to use variable-length prefix encodings and raw binary data-files to make some significant gains. It's nowhere near something like LZW compression in terms of speed or compressive factor, but I think that for a Python script given the initial constraints, it's not bad at all. Also features some heavy unit testing, and modularisation, and a pretty decent interface for input/output using argparse. It also features an implementation of LZW in the same framework, used as reference (it's faster and produces more compresssion :( ). This repository features several utilities for abstract dealing with binary misaligned data - they're not particularly optimised, but they're pretty elegant. BinaryWriter and BinaryReader classes are used to buffer byte input and act like iterables.

The most simple compressive algorithm (`readable_compression.py`), given the input:

    ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU BUT WHAT YOU CAN DO FOR YOUR COUNTRY

produces the *readable* output:

    ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU BUT
    0 1 2 3 4 5 6 7 8 9 2 8 5 6 7 3 4

Which it can then correctly decode.

The more advanced `lossless_compression.py` can correctly encode something like this:

      Chor. Two households, both alike in dignity,
        In fair Verona, where we lay our scene,
        From ancient grudge break to new mutiny,
        Where civil blood makes civil hands unclean.
        From forth the fatal loins of these two foes
        A pair of star-cross'd lovers take their life;
        Whose misadventur'd piteous overthrows
        Doth with their death bury their parents' strife.
        The fearful passage of their death-mark'd love,
        And the continuance of their parents' rage,
        Which, but their children's end, naught could remove,
        Is now the two hours' traffic of our stage;
        The which if you with patient ears attend,
        What here shall miss, our toil shall strive to mend.
                                                             [Exit.]

in binary format, and decode it (by this command).

    $ python lossless_compression.py --input ../text/rom_ju_intro.txt  | python lossless_decompression.py

Yes, I have tested my lossless algorithm on the works of Shakespeare. It produces a lossless compressive ratio of about 39% (and a lossy compression ratio of 28%). Its performance and memory usage complexity is poor as it has to read lots into memory to optimise the prefix encoding.

Here are some tests on compressive ratios:

    $ wc -c  ../text/shakespeare.txt 
    5458199 ../text/shakespeare.txt
    $ cat ../text/shakespeare.txt | python lzw_compression.py | wc -c
    1933187
    $ cat ../text/shakespeare.txt | python lossless_compression.py | wc -c 
    2150980
### [\[toc\]](#table-of-contents) [Linked lists](https://github.com/goedel-gang/linked_list)
My Python linked list implementation. This is my expanded implementation from the HackerRank challenged. Note it's kind of half finished and untested so probably broken in all manner of fun ways. It's recursive so won't be able to handle any serious load due to Python's lack of tail call optimisation. It also overloads the `__or__` operator, which put together with recursion produces some slightly Haskell-inspired levels of conciseness:

```Python
def take(head, n):
    if n > 0:
        if head.next:
            return head | head.next.take(n - 1)
        raise IndexError
    return NULL
```

`demo.py` executes several examples (with a nice for loop and a safe application of eval). Here are a couple:

    s1.head_item()                  = 57
    s1.tail()                       = <45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.last()                       = 67
    s1.init()                       = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30>
    s1.drop(11)                     = <8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.take(15)                     = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90>
    s1[14]                          = 90
    s1.setitem(5, -1)               = <57, 45, 55, 58, 78, -1, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.insert_at_tail(-1)           = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67, -1>
    s1.insert_at_head(-1)           = <-1, 57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.insert_at_n(-1, 10)          = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, -1, 59, 8, 58, 79, 90, 33, 39, 70, 30, 67>
    s1.delete_node(18)              = <57, 45, 55, 58, 78, 95, 84, 43, 84, 18, 59, 8, 58, 79, 90, 33, 39, 70, 67>
    s1.reverse()                    = <67, 30, 70, 39, 33, 90, 79, 58, 8, 59, 18, 84, 43, 84, 95, 78, 58, 55, 45, 57>
    s2.merge(s3)                    = <0, 1, 2, 3, 4, 5>

NB it's Python 3.6, as it uses f-strings. Should be easy enough to use .format instead.
### [\[toc\]](#table-of-contents) [Cube](https://github.com/goedel-gang/Cube)
My project expressing a Rubik's cube as a list of integers representing colours, and moves on the cube as permutations on the list. Uses some operator overloading for some pretty expressive syntax to build up the set of moves on the cube. The object model allows chaining and merging of permutations, allowing you to build up to something like this:

```Python
 # turn the front face of the cube
 turn_front = (turn_face(F)
             + circular_chain([(U, [6, 5, 4]),
                               (R, [0, 7, 6]),
                               (D, [2, 1, 0]),
                               (L, [4, 3, 2])]))
```

There are many such samples in `cube.py`. Note that no speed is lost in the abstraction - the abstracted computation is done at the start and then de-abstracted into pure permutations (lists/arrays of integers). `playground.py` allows you to do things like this:

    enter move ([UDFBLR]'?|turn (left|right|up|down)) > U R U' L' U R U' L' U R U' L' U R U' L'
    -------------------------
            R B O                 W = F
            B B B                 Y = B
            R B B                 B = U
                                  G = D
     B O W  G W W  R R W          O = L
     O O O  W W W  R R R          R = R
     O O G  R W O  W R G
     
            Y G G
            G G G
            Y G O
            
            B Y Y
            Y Y Y
            Y Y B

For prettier visualisations, refer to my parallel [Processing project](https://github.com/goedel-gang/rubiks_cube).

This project also explores some more group-theoretical aspects of the cube - eg how many times must a set of moves be repeated to return a cube to its original state. An interesting optimisation in this is finding "sub-cycles" in the permutation formed by the set of moves and determining the LCM of the lengths of these sub-cycles.
### [\[toc\]](#table-of-contents) [Punnet Squares](https://github.com/goedel-gang/Punnet)
Some leftover code for Punnet square generation, from a stackoverflow question. The question was deleted, so I decided to see how illegible I could make my code. Was once intended to become a `code-golf` challenge, but it was too similar to another challenge. It uses some neat generator/unpacking tricks. If tokens are shortened appropriately, you can get this to be pretty short.

`$ python code.py Xx xx`

	 |X |x
	-+---+--
	x|Xx|xx
	-+---+--
	x|Xx|xx
### [\[toc\]](#table-of-contents) [cookies](https://github.com/goedel-gang/cookies)
Some projects on "the cookie game" in Python. Includes an automatic opponent and some testing scripts on higher dimensions of the game. Here is a sample of `opponent.py` dealing out a thrashing (featuring a little more description of what the game is):

`$ python opponent.py -j 4 8`

    Automatically play the cookie game (in 2 dimensions, for now). Prepare not to
    win. The game works like so: There are two jars. Each has some cookies. You win
    if you take the last cookie. You can take some n cookies from any combination
    of jars - but n for each jar. (ie for the two-jar case, you must take either
    the same from both or any number you like from one.

    jars given: (4, 8)
    computer starts
    computer takes 1 cookie from jar { 8 }
    Jars are: 
    Jar 0: 4
    Jar 1: 7
    Enter two jar numbers> 0 1
    Jars are: 
    Jar 0: 4
    Jar 1: 6
    computer takes 1 cookies from both jars
    Jars are: 
    Jar 0: 3
    Jar 1: 5
    Enter two jar numbers> 2 2
    Jars are: 
    Jar 0: 1
    Jar 1: 3
    computer takes 1 cookie from jar { 3 }
    Jars are: 
    Jar 0: 1
    Jar 1: 2
    Enter two jar numbers> 1 0
    Jars are: 
    Jar 0: 0
    Jar 1: 2
    computer takes 2 cookies from jar { 2 }
    computer wins

Also features a miscellaneous utility function that greps for lines containing the letters of a word, in order.
### [\[toc\]](#table-of-contents) [Yahtzee](https://github.com/goedel-gang/yahtzee)
A work in progress - hoping to end up building a kind of nice yahtzee framework and then try to implement some different yahtzee playing algorithms (maybe monte carlo, neural network, etc). Stemming from mid-yahtzee computing banter. It might be interesting to see the distribution of scores achieved by different algorithms, such as a greedy yahtzee-seeking algorithm, or a more measured greedy algorithm searching for intersections between dice and targets (maybe weighting by scores / ease). All sorts of fun opportunities are available - reading random integers from `/dev/urandom`, synchronizing different algorithms into one stream of dice of "game", implementing algorithms as generators that require sent variables, secure extra-algorithm move validation..
### [\[toc\]](#table-of-contents) [queens](https://github.com/goedel-gang/queens)
The n-queens problem in Python. A command-line script to generate all solutions to the problem for an n\*n chessboard (the problem being to fit n queens on this board such that no queen can target another). It uses the relatively naive backtracking technique. It stores queens as a list of length `n`, where each element is the `y`-coordinate of a queen (or `None`) if the queen doesn't exist.

The default case is 8\*8 - so calling with `$ python queens.py` results in something like this:

    Board 0:
    Q _ _ _ _ _ _ _
    _ _ _ _ Q _ _ _
    _ _ _ _ _ _ _ Q
    _ _ _ _ _ Q _ _
    _ _ Q _ _ _ _ _
    _ _ _ _ _ _ Q _
    _ Q _ _ _ _ _ _
    _ _ _ Q _ _ _ _
    Board 1:
    Q _ _ _ _ _ _ _
    _ _ _ _ _ Q _ _
    _ _ _ _ _ _ _ Q
    _ _ Q _ _ _ _ _
    _ _ _ _ _ _ Q _
    _ _ _ Q _ _ _ _
    _ Q _ _ _ _ _ _
    _ _ _ _ Q _ _ _

    ...

    Board 91:
    _ _ _ _ _ _ _ Q
    _ _ _ Q _ _ _ _
    Q _ _ _ _ _ _ _
    _ _ Q _ _ _ _ _
    _ _ _ _ _ Q _ _
    _ Q _ _ _ _ _ _
    _ _ _ _ _ _ Q _
    _ _ _ _ Q _ _ _

It works for any board dimension - eg `$ python -n 13`.

It features a little optimisation - minimising dual computation and reconstruction of objects - `positions` in `_n_queens` is always the same list, and its length is never changed.
### [\[toc\]](#table-of-contents) [hangman](https://github.com/goedel-gang/hangman)
A bit of a legacy project on Hangman. It's an implementation of hangman, where the man being hanged is drawn in Turtle. I have to say I'm actually pretty proud of it. It originally used some slightly messy terminal escape codes to try and hide user input - this has since been replaced with `getpass`. It also features a pretty robust command line interface which happens in parallel with the turtle graphics. Here it is in action (where the invisibly entered word is `"izaak van dongen"`):

	What should the word be? 
	Can you verify?
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ _ _ _ / _ _ _ / _ _ _ _ _ _
	You have 10 remaining guesses
	Guess a letter
	a
	You guessed correctly!
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ a a _ / _ a _ / _ _ _ _ _ _
	You have 10 remaining guesses
	Guess a letter
	v
	You guessed correctly!
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ a a _ / v a _ / _ _ _ _ _ _
	You have 10 remaining guesses
	Guess a letter
	n
	You guessed correctly!
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ a a _ / v a n / _ _ n _ _ n
	You have 10 remaining guesses
	Guess a letter
	x
	That was wrong.
	Incorrect letters you have guessed:
	 x
	This how much you have currently guessed:
	_ _ a a _ / v a n / _ _ n _ _ n
	You have 9 remaining guesses
	Guess a letter
	y
	That was wrong.
	Incorrect letters you have guessed:
	 xy
	This how much you have currently guessed:
	_ _ a a _ / v a n / _ _ n _ _ n
	You have 8 remaining guesses

After several more failures, the screen will turn red and look like this (NB this has been building up in steps like a proper hangman game):

![screenshot](https://github.com/goedel-gang/hangman/blob/master/fail.png)
### [\[toc\]](#table-of-contents) [points](https://github.com/goedel-gang/points)
My first serious, non-trivial, non-tutorial suggested Python project was `points.py`. This repository features several evolutions of the project as I grew more experienced with Python - `IV` is still in development. The gist of the program is to take a set of coordinates, and fit a polynomial in `x` to them *exactly*. This is guaratneed to be possible if no coordinates share an x-coordinate. It is done by substituting each coordinate into the general equation for a polynomial of degree (`num of points - 1`), which results in a solvable system of simultaneous equations, which the program then solves with varying levels of elegance.
### [\[toc\]](#table-of-contents) [DNA](https://github.com/goedel-gang/DNA)
My various projects from my brief work experience at the Wellcome Trust Sanger Institute, where I did a project on error-correction in DNA strings. Features various approaches, including Hadamard codes moved forcibly to base-4, and a base-4 adaptation of the Hamming code, where parity is extended into value-mod-4.

It also has some simple Python CGI scripts implementing some of the found approaches in a very simplistic web interface.

[Here](https://github.com/goedel-gang/DNA/blob/master/presentation.pdf) is the accompanying presentation I made for the end of my stay.

It's somewhere around the middle of my well-populated to-do list to revisit this and clean it up.
### [\[toc\]](#table-of-contents) [cipher\_tools](https://github.com/goedel-gang/cipher_tools)
A collection of programs to aid in cipher-cracking/cryptanalysis. If you use
this and you're not a GW appreciator you're a disappointment and need to
re-evaluate your life (beware as `eval` is unsafe). Please note:

“In submitting an entry solo entrants vouch that it is solely their own work
and teams warrant that it is solely their own collective work.”

Currently features, among other things:

 - Pretty fully fledged textual interface, with exception handling and a
   functional model for commands/functions
 - Frequency analysis (including IOC calculation)
 - Substitution
 - Some facilities for polyalphabetic analysis
 - Analysis of frequently occurring runs of letters
 - Hints for unsubstituted letters
 - Display of expected frequency analysis
 - Substitution table histories
 - Utility to split an unpunctuated text into words, featuring blacklisting,
   whitelisting and space hinting

These are, as it stands, text-based interfaces. Hopefully it should be possible
to paste in input. They rely on an installation of Python 3 (I recommend 3.6).
They might be runnable by clicking the script from a file explorer?

Notice: sometimes I find catastrophic bugs, fix them and don't tell anyone.
This is absolutely my fault and I'll try to stop doing this but in the meantime
please make sure your version is up to date.

You can obtain the scripts by downloading them, pasting them in, or even
cloning them if you're feeling really enthusiastic. (NB the scripts are all in
the `src` directory.)

Here is a quick guide to installation and execution:

 - Install Python 3.6 and, by extension, Idle from
   https://www.python.org/downloads/. This should be pretty well documented
   across the web.
 - Download this repository (click Clone or download, and then "Download ZIP").
   You will probably need to unzip it. Don't make any changes to the files.
 - Navigate to `src/` in the repository in the file explorer of your choice
 - Click/double click on `text_interface.py` to run it.

You probably can run it from IDLE, but I would not recommend, as IDLE does not
provide some of the terminal features used (eg it breaks automatic width
detection)

If you're a command line user, you can safely ignore and just clone and pull,
and run `text_interface` from the CLI.

For more on how `text_interface.py` works, see
[this](https://github.com/goedel-gang/cipher_tools/blob/master/text_interface_doc.md)
MD file.

For documentation on each function, see
[this](https://github.com/goedel-gang/cipher_tools/blob/master/action_doc.md)
MD file.

For fledgling documentation on `splitting_words`, see
[this](https://github.com/goedel-gang/cipher_tools/blob/master/splitting_doc.md)
MD file. This is probably not useful to anyone because (1) it's illegible (2)
it only works from a terminal prompt.

You can also try looking at the source files in `src` - they're now pretty well
documented inline. This will be more technical, terse, and may require some
knowledge of Python but is guaranteed to be up to date.
### [\[toc\]](#table-of-contents) [sorting](https://github.com/goedel-gang/sorting)
My various projects on sorting in Python. The main part is a mix of pure-Python and processing, which is a project in progress, hoping to get some clean, efficient sorting implementations in Python and visualise them (in the classic points fashion, with added rainbows and exponential decay to demonstrate array accesses think kind of like [this](https://www.youtube.com/watch?v=kPRA0W1kECg)) in addition to providing command-line support. `pure` contains pure implementations - in the main directory generator versions are provided (which allow the sort to block itself while keeping state, and allow the generator to provide information about where it's working for rainbow access visualistion). They're also Python 2 as that's my processing installation, so there are some `xrange`s etc.

Here is heapsort, for example:

![screenshot](https://github.com/goedel-gang/sorting/blob/master/screenshots/heap.png)

Here is shellsort (a generalization of insertion sort):

![screenshot](https://github.com/goedel-gang/sorting/blob/master/screenshots/shell.png)

The slightly more esoteric bitonic sort:

![screenshot](https://github.com/goedel-gang/sorting/blob/master/screenshots/bitonic.png)

An appropriately named LSD radix sort:

![screenshot](https://github.com/goedel-gang/sorting/blob/master/screenshots/lsd_radix.png)

Other screenshots can be found in the `screenshots` directory.

So far it also features bubble-sort and bogosort (the former is miniaturised and sped up and still takes forever to complete - the second just takes forever to complete), in addition to some of the other standard ones. I'm only doing algorithms than can be implemented somewhat in place without too much trickery, as this allows the visualisation (merge-sort does make some auxiliary arrays but it still shows the accesses in the merging).

It also features an old, old directory (`school`) from when I was in year 10 and did an investigation into sorting algorithms, which devolved into comparison-less integer sorting. It's a mess. 

[Here](https://youtu.be/BaFKYvCZq1k) is a full video rendering I made of it at one point.
### [\[toc\]](#table-of-contents) [elf\_game](https://github.com/goedel-gang/elf_game)
A framework for simulating the elf game, allowing for testing, analysis and
evaluation of different strategies.  `sim_game.py` is an OOP framework to
perform the simulation. `stats.py` calculates statistics about the distribution
of money earned, and the other files are implementers. 

Also featured are some shell scripts/makefiles to synthesise/present generated
data.

[Here](https://github.com/goedel-gang/elf_game/blob/master/stats.md) is an MD file with a table of statistics about each strategy.

[Here](https://github.com/goedel-gang/elf_game/blob/master/descs.md) is an MD file with scraped descriptions of each approach.

[Here](https://github.com/goedel-gang/elf_game/blob/master/results.md) is an MD file illustrating the usage of the command-line scripts.

[Here](https://github.com/goedel-gang/elf_game/blob/master/spaced_figures.pdf) is a PDF with graphs of the distribution generated by each strategy.
### [\[toc\]](#table-of-contents) [double\_pendulum](https://github.com/goedel-gang/double_pendulum)
An animation of the classic "double pendulum" model that demonstrates chaos.
This was made using matplotlib, and all of the maths and the basis of the
animation was drawn from
[matplotlib example](https://matplotlib.org/examples/animation/double_pendulum_animated.html).
However I then refactored this code so I had a double pendulum class to work
with, and created separate subplots with different starting parameters. I also
made it plot the trail of each bob as the animation progressed. I also added a
tiny tiny command line interface.

Here is an image of the chaotic behaviour it might exhibit - the only
difference in starting conditions was that one pendulum was 10 degrees higher:

![figure of pendulums](https://github.com/goedel-gang/double_pendulum/blob/master/mat_chaotic.png)

See also [this](https://youtu.be/eM7zUfZCPS0) video of it in action.

It now also includes a Processing sketch that uses an iterative model of the
double pendulum. This sketch drew the maths from the
[video](https://www.youtube.com/watch?v=uWzPe_S-RVE)
and [code](https://github.com/CodingTrain/website/blob/master/CodingChallenges/CC_93_DoublePendulum/CC_93_DoublePendulum.pde)
by Daniel Shiffman, although mostly for formulae - the sketch is now in an
entirely different language, for example. It has similarly been modified to
encapsulate each double pendulum in an object, and shows two simultaneously. It
looks like this:

![figure of pendulums](https://github.com/goedel-gang/double_pendulum/blob/master/pde_chaotic.png)

The crucial difference between the two animations is that the first is more
accurate, but the second is iterative so slightly less processing-intensive
near the start and can continue indefinitely.
### [\[toc\]](#table-of-contents) [flippy\_bot](https://github.com/goedel-gang/flippy_bot)
Flippy bit bot. It uses and was developed with the webdriver for Chromium. You
will need to install the correct drivers for your browser if you want to run
this. Change the browser at your own risk - I couldn't get firefox to work.

It's of course also dependent on Selenium.

The constants defined at the start may need to be tweaked to suit your
preference/browser speed.

After a certain time, the bot will hit the limit of possible scores. This is
due to really quite primitive way the game approaches difficulty scaling.

Here are a selection of relevant screenshots of the game's JS code (`game.js`):

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_init.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/cons_init.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_attack.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_cycle.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_timeout.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/config_timeout.png)

Basically, the game initially sets the millisecond interval between enemies to
5000 ms. Whenever an enemy dies this interval is decreased by 30 ms, and
whenever the game refreshed and the "cycle" function is called, the time is
further decreased by 0.2 ms. The cycle function has a constant interval of 10
ms, but also takes some time to run. This means that the upper bound of
achievable score is variable between computers, or even on the same computer
can depend on CPU and memory availability.

On my laptop, this apocalypse happens at around 80 enemies, two and a half
minutes in. This means that my refresh rate would be:

    (5000 - 80 * 30) / 150 / 0.2
    ~ 87 Hz

As a high-uncertainty estimate, this seems reasonable. It also leads to a cycle time of

    1 / 87
    ~ 11-12 ms

Reassuringly, this is more than 10 ms and would put the average execution speed
of a cycle at a couple of ms.

All in all, I consider this to be a satisfactory explanation of why this
happens.

Frustratingly, this result means that the best way to get a high score using
the bot is to play flippy bit on a slower computer.

However, if you as a human start to press as many keys as quickly as possible
as soon as the program crashes, your score actually goes up very fast. This is
because almost everything is on screen at once.

Here is the resulting apocalypse:

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/apocalypse.png)
### [\[toc\]](#table-of-contents) [fizzbuzz](https://github.com/goedel-gang/fizzbuzz)

My crack at an over-engineered fizzbuzz, from about a year ago, as of

    Tue 16 Jul 15:40:02 BST 2019

Supports adding arbitrarily many fizzbuzz "rules" with the `--fb` command line
argument. The classic ruleset would be achieved by

    python fizzbuzz.py --fb 3 fizz --fb 5 buzz
### [\[toc\]](#table-of-contents) [1r1l1e](https://github.com/goedel-gang/1r1l1e)

This is basically a Python script to do run-length encoding (RLE). Seeing as RLE
itself provides such poor compression, I thought I would write the script in as
few bytes as possible in order to save disk space.

You use `python rle.py` to RLE encode stdin, and `python elr.py` to RLE decode
stdin. The use of separate programs avoids branching and parsing of argv in
the scripts, which is a huge savings on bytes. It doesn't understand file
arguments because that would take up too many LoC. Instead, you should just
attach files to stdin and stdout as appropriate.

The encoding it uses is quite simple - it writes alternating counts and bytes,
where each byte of data is preceded by a count indicating how many times it
occurs. The counts are themselves single bytes. If a count is greater than 255,
it simply gets split into multiple count-byte pairs.

It is unaware of Unicode, but not necessarily to its detriment. It just operates
on stdin as a stream of bytes, and correctly restores this stream after
decoding.

There is also a script that generates some realistic real-world data,
accompanied by a makefile that tests the whole things.
### [\[toc\]](#table-of-contents) [nctfe](https://github.com/goedel-gang/nctfe)

This is an implementation of the 2048 game in Python, building up to a Python
`curses` interface. Named `nctfe` in the spirit of `ncdu` and `ncmpc` and so on.

Doesn't do anything so clever as tracking high scores or saving games yet,
regrettably.

![screenshot](https://github.com/goedel-gang/nctfe/blob/master/win_screenshot_20190716_144759.png)

Also features preposterously large boards and autoplay mode so you can make
impressive screenshots like this:

![screenshot](https://github.com/goedel-gang/nctfe/blob/master/win_screenshot_20190716_162511.png)

This mode is best leveraged with PyPy.
# [\[toc\]](#table-of-contents) java-processing projects
### [\[toc\]](#table-of-contents) [alphabet](https://github.com/goedel-gang/alphabet)
Shading the screen using letters of the alphabet in Processing. All printable ascii keys on the keyboard are accessible from the keyboard. Some special keys (space, enter) are used for acceleration. ASCII value scales with the x value. Here are some screenshots:

![screenshot](https://github.com/goedel-gang/alphabet/blob/master/screenshots/alph1.png)

And after a couple of years of typing:

![screenshot](https://github.com/goedel-gang/alphabet/blob/master/screenshots/alph2.png)

[Here](https://youtu.be/K-3I5doHDqs) is a *short* video of it in action.
### [\[toc\]](#table-of-contents) [balls](https://github.com/goedel-gang/balls)
Simple, slightly buggy implementation of balls that can bounce off both each other and walls. It ends up looking pretty dynamic. It uses an equation for circle collision from wikipedia. The problem is that sometimes a ball will clip into another ball and start a weird orbit/mating dance. Especially happens when there's disparity between ball radii. It looks like this:

![screenshot](https://github.com/goedel-gang/balls/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [cars](https://github.com/goedel-gang/cars)
Early experimenting in OOP in java-processing. Animates a bunch of rectangles and their attributes (colour, size, position, rotation etc). It looks like this:

![screenshot](https://github.com/goedel-gang/cars/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [circles](https://github.com/goedel-gang/circles)
Neat little effect in processing an grid of circles, where radius increases the closer to the mouse. Produces quite a simple yet satisfying effect - example:

![screenshot](https://github.com/goedel-gang/circles/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [colourconway](https://github.com/goedel-gang/colourconway)
Conway's game of life, with colourisation related to recent activity. It's pretty but the code is a godawful mess I might try to wade into one day. Here it is in action:

![screenshot](https://github.com/goedel-gang/colourconway/blob/master/screenshot.png)

[Here](https://youtu.be/xvZLSq9onlU) is a video.
### [\[toc\]](#table-of-contents) [mazes](https://github.com/goedel-gang/mazes)
Maze generation algorithms in Processing, by random walking and "knocking down" walls, and backtracking when cornered. All cells are guaranteed to be reachable, so any combination of cells can be taken as start-end (top-left bottom-right, for example). Features solutions and slower, frame-by-frame generation. Here it is in action:

![screenshot](https://github.com/goedel-gang/mazes/blob/master/screenshots/nopath.png)
![screenshot](https://github.com/goedel-gang/mazes/blob/master/screenshots/path.png)
![screenshot](https://github.com/goedel-gang/mazes/blob/master/screenshots/slo.png)

The slow version has [this](https://youtu.be/RDCxf3rzJrw) video.
### [\[toc\]](#table-of-contents) [pendulums](https://github.com/goedel-gang/pendulums)
A little more experimentation with Java OO in processing. Uses the simple model of pendulums to produce a slow interference effect. Here's a static screenshot:

![screenshot](https://github.com/goedel-gang/pendulums/blob/master/screenshot.png)

It doesn't quite deliver the effect of them in motion, but you can see the interference/general idea.
### [\[toc\]](#table-of-contents) [pixel\_sorting](https://github.com/goedel-gang/pixel_sorting)
Sorting rows of pixels in an image by brightness, in Processing. Most of the work was done by Daniel Shiffman.

With this as input:

![input sunflower](https://github.com/goedel-gang/pixel_sorting/blob/master/data/sunflower.jpg)

It can produce this:

![output](https://github.com/goedel-gang/pixel_sorting/blob/master/sorted.jpg)

While it's running, it looks like this:

![screenshot](https://github.com/goedel-gang/pixel_sorting/blob/master/intermediary.png)
### [\[toc\]](#table-of-contents) [pythanimated](https://github.com/goedel-gang/pythanimated)
Relatively simple code to eternally increment animate the angle of a rendered Pythagoras Tree fractal.

![screenshot](https://github.com/goedel-gang/pythanimated/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [rainbow\_lines](https://github.com/goedel-gang/rainbow_lines)
A simpler project, doing some slightly diagonal rainbow shading on a canvas.

Here is a screenshot:

![Screenshot](https://github.com/goedel-gang/rainbow_lines/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [regen\_soup](https://github.com/goedel-gang/regen_soup)
Simple OO to display a kind of weird soup-like substance with some mildly hallucinogenic rainbows. It doesn't use drawing primitives to draw the rainbows as Processing doesn't support any kind of gradient, so it actually directly modifies the pixel array. It looks like this:

![screenshot](https://github.com/goedel-gang/regen_soup/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [shading](https://github.com/goedel-gang/shading)
Processing "rainbow shading" by many random diagonal lines, colour shifting according to x position. It looks like this:

![screenshot](https://github.com/goedel-gang/shading/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [snowflakes](https://github.com/goedel-gang/snowflakes)
From a Christmas CS lesson once upon a time - snowflakes simulated by ascii characters. It looks like this:

![screenshot](https://github.com/goedel-gang/snowflakes/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [square\_filling\_circle](https://github.com/goedel-gang/square_filling_circle)
Squares that fill up the area of a circle, inspired by the classic pi paradox (as the total area of the squares approaches the area of the circle, then surely the perimeter does so too, which would lead to pi=4). It uses a real beauty of an equation worked through by hand to find the intersection of a line with gradient 1 and a circle arc - 

    intercept = 0.5 * (sqrt(-a * a + 2 * a * (b + c - d) - b * b - 2 * b * c + 2 * b * d - c * c + 2 * c * d - d * d + 2 * r * r) + a + b + c - d) - c;

Here is a screenshot of it in action:

![screenshot](https://github.com/goedel-gang/square_filling_circle/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [UI\_demo](https://github.com/goedel-gang/UI_demo)
A simpler implementation/demonstration of my UI elements in Processing, later to be used more in `moire_draggable`. It does a lot of event handling and delegation through static methods to abstract that from the main pde sketch. It uses some vector arithmetic for some of the features. It looks like this:

![screenshot](https://github.com/goedel-gang/UI_demo/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [turtles](https://github.com/goedel-gang/turtles)

Custom turtle implementation in Processing, used to have multiple turtles follow
the same instructions (from keyboard) for symmetric kinda pretty rainbow
patterns. Here is what it looks like:

![screenshot](https://github.com/goedel-gang/turtles/blob/master/win_screenshot_20190624_173407.png)
![screenshot](https://github.com/goedel-gang/turtles/blob/master/win_screenshot_20190624_173340.png)
![screenshot](https://github.com/goedel-gang/turtles/blob/master/win_screenshot_20190624_173315.png)
### [\[toc\]](#table-of-contents) [s\_zoom](https://github.com/goedel-gang/s_zoom)
A kind of inefficient sketch that tries to emulate the effect of infinitely zooming in on the top part of a Sierpinski Triangle. It looks like this:

![screenshot](https://github.com/goedel-gang/s_zoom/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [sandpiles](https://github.com/goedel-gang/sandpiles)
An implementation of Abelian sandpiles that I believe to be currently broken (some points seem to exceed 8) - it's a very pretty fractal though. 

Here it is in an early stage (as it takes a lot of time/power to view later stages):

![screenshot](https://github.com/goedel-gang/sandpiles/blob/master/abelian.png)
### [\[toc\]](#table-of-contents) [platformer](https://github.com/goedel-gang/platformer)
An extremely bare-bones platformer in processing - both in content and implementation. Its collision detection, after much work, seems to be pretty flawless. It should be relatively easy to add more platorms. Here is what it looks like - be warned that I'm a prolific graphic designer:

![screenshot](https://github.com/goedel-gang/platformer/blob/master/screenshot.png)

The upright rectangle is the protagonist, and the sideways rectangles are platforms. If Thomas was alone can do it, so can I.
### [\[toc\]](#table-of-contents) [snake](https://github.com/goedel-gang/snake)
The game Snake in Processing. Not a particularly clear implementation. The snake is rainbow coloured. There is a known bug with the score-text, but I'm not feeling motivated enough to fix it. It also features some very well hidden cheat codes. It looks like this:

![screenshot](https://github.com/goedel-gang/snake/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [spaceinvaders](https://github.com/goedel-gang/spaceinvaders)
Kind of old implementation of Space Invaders I did in processing. It serves as a great showcase of my mastery of graphic design. In fact, I'm starting to worry I've peaked too early in my career:

![screenshot](https://github.com/goedel-gang/spaceinvaders/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [tetris](https://github.com/goedel-gang/tetris)
Old implementation of Tetris in processing. At last, a game with graphics I can understand. The pieces and their rotations are all hardcoded. This suffers from the same bug as my snake game. Here's my attempt at playing it while taking a screenshot:

![screenshot](https://github.com/goedel-gang/tetris/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [sierp\_demo](https://github.com/goedel-gang/sierp_demo)
processing implementation of the "chaos game", with a couple of interactive features. The game works as follows: Take a point in the middle of a triangle. Choose a random corner. Take the point directly in between that corner and your current point. Make this your new point (remember to draw old points). This can produce some interesting results, given automation:

First couple of points:

![screensaver](https://github.com/goedel-gang/sierp_demo/blob/master/screenshots/early_stage.png)

A few more:

![screensaver](https://github.com/goedel-gang/sierp_demo/blob/master/screenshots/later.png)

A **lot** more, and shrunken points:

![screensaver](https://github.com/goedel-gang/sierp_demo/blob/master/screenshots/latest.png)

Fancy that.
### [\[toc\]](#table-of-contents) [chaos\_spreadsheet](https://github.com/goedel-gang/chaos_spreadsheet)
Illustration of the chaotic behaviour of the logistic map function (used for some interactive demoing once upon a time). Acts as a programmatic, slightly enhanced version of just generating the logistic map in a spreadsheet and plotting it. Features animation and some fine control over parameters. It looks like this (but animated):

![screenshot](https://github.com/goedel-gang/chaos_spreadsheet/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [moire\_draggable](https://github.com/goedel-gang/moire_draggable)
A program to interactively explore the moire interference effect on grids, using a (self implemented) visual UI with the mouse, with further features on the keyboard. Also features some serialisation (to preprocessed handwritten postscript) and an experimental Postscript compresser which works by mangling.  Experimenting with some more OOP, and pure Java integration with Processing.  probably not a good idea for people with epilepsy and the like `1234567890-=[back][tab]` to add grids mouse interface for most manipulation.  click and drag on the colourful UIElements to change grid parameters. use the green button to clone a grid, the red to remove.

    r to reset
    p to toggle auto mode
    aq, sw, de for delta manipulation
    space to toggle delta info box
    enter to toggle ui
    click on a draggable element and then use arrow keys for finer manipulation
    use f to serialise
    use i to serialise with image and postscript file - this hasn't been tested much, use at own risk

note that a very large portion of the code for this sketch is .java. This is because this allows me to circumvent all of Processing's preprocessing, and I can use more of Java pure OOP functionality like static fields and methods

It is probably one of the best things I've written. It's very flexible in what you can do, in terms of moving and resizing, overlaying different grids, removing bits of UI, finer precision with keyboard, etc. Most constants are entirely customizable (see the two constants pages). Here I've pulled the full list of all the grids it supports:

      new SquareGrid(), 
      new ConcentricGrid(), 
      new TriangleRadial(), 
      new HexagonalGrid(), 
      new TriangleGrid(), 
      new StarGrid(), 
      new OctGrid(), 
      new SquareStarGrid(), 
      new SquareOffsetGrid(), 
      new CrossGrid(), 
      new CircleGrid(), 
      new CircleStarGrid(), 
      new LineGrid(), 
      new RadialGrid()

Here are some screenshots of what you might begin to do with it, with the "UI" preserved:

![screenshot](https://github.com/goedel-gang/moire_draggable/blob/master/screenshots/hex.png)
![screenshot](https://github.com/goedel-gang/moire_draggable/blob/master/screenshots/radial.png)

Both of these were narrowly obtained before my laptop melted
### [\[toc\]](#table-of-contents) [julia](https://github.com/goedel-gang/julia)
Julia set visualisation next to mandelbrot set, illustrating what a julia set is (kind of) and more so its correspondance with the mandelbrot set.

As a Julia set takes a complex number as input, the mouse coordinates can serve as input. When this is put together with the mandelbrot set, something interesting happens.. You can easily find "interesting" Julia sets - move the mouse along the border of the Mandelbrot set.

Here are just a couple of examples:

![screenshot](https://github.com/goedel-gang/julia/blob/master/screenshots/julia1.png)
![screenshot](https://github.com/goedel-gang/julia/blob/master/screenshots/julia2.png)
![screenshot](https://github.com/goedel-gang/julia/blob/master/screenshots/julia3.png)
![screenshot](https://github.com/goedel-gang/julia/blob/master/screenshots/julia4.png)
### [\[toc\]](#table-of-contents) [mandelbrot](https://github.com/goedel-gang/mandelbrot)
This is a program in java-processing that renders the mandelbrot set. This set is defined as the set of the complex numbers, c such that there is no divergence when 0 is iterated under f(z) = z^2 + c The program works by simply iterating and observing if this number becomes large.  The speed of divergence is then used to give colourings.  The parameters kept track of are - x, y, scale, iteration cap, multibrot value (alternative exponent for z), width and height. See [usage.md](https://github.com/goedel-gang/mandelbrot/blob/master/usage.md) for info about the usage of the sketch.

It supports some mildly sophisticated serialisation - in string format. Any rendering can be described in a couple of terms (x, y, scale, width height, multibrot) which can be quite compactly encoded. This is then stored as the **filename** of any image you save from the sketch. What a stroke of genius, never has a filename been prettier than `-16od5ok4AH4+-NlkJp9kxyI4+w8SYn6PLXC4+Tf+3+uu+Ff.tiff`.

Here are three randomly chosen screenshots from my travels:

![screenshot](https://github.com/goedel-gang/mandelbrot/blob/master/screenshots/mandel1.png)
![screenshot](https://github.com/goedel-gang/mandelbrot/blob/master/screenshots/mandel2.png)
![screenshot](https://github.com/goedel-gang/mandelbrot/blob/master/screenshots/mandel3.png)

[Here](https://drive.google.com/drive/folders/0B3EHq-o9udUMQ2pyZlJKQWZlcDA?usp=sharing) is my full collection of higher quality serialisations for ayone interested.
### [\[toc\]](#table-of-contents) [mandemthot](https://github.com/goedel-gang/mandemthot)
A much faster mandelbrot orbit plotter. This is due to Java/using a compiled
implementation of a language, really. This absolutely destroys the Python
mandeldot. It does about 10k points every frame without too much trouble, if you
ignore the screams coming from your [CG]PU.

It can also overlay orbits, and delete previously stored orbits. It does this by
making a cutesy little stack of PGraphics objects, which is quite cool.

![screenshot](https://github.com/goedel-gang/mandemthot/blob/master/win_screenshot_20190518_164727.png)
![screenshot](https://github.com/goedel-gang/mandemthot/blob/master/win_screenshot_20190518_164743.png)
### [\[toc\]](#table-of-contents) [whomping\_fractal](https://github.com/goedel-gang/whomping_fractal)

This is a tiny little sketch to draw a fractal binary tree, and let you adjust
its parameters by clicking and moving the mouse near either of the first two
branches.

![screenshot](https://github.com/goedel-gang/whomping_fractal/blob/master/screenshots/win_screenshot_20190626_104612.png)
![screenshot](https://github.com/goedel-gang/whomping_fractal/blob/master/screenshots/win_screenshot_20190626_104621.png)
![screenshot](https://github.com/goedel-gang/whomping_fractal/blob/master/screenshots/win_screenshot_20190626_104632.png)
![screenshot](https://github.com/goedel-gang/whomping_fractal/blob/master/screenshots/win_screenshot_20190626_104647.png)
![screenshot](https://github.com/goedel-gang/whomping_fractal/blob/master/screenshots/win_screenshot_20190626_104659.png)
![screenshot](https://github.com/goedel-gang/whomping_fractal/blob/master/screenshots/win_screenshot_20190626_104705.png)
### [\[toc\]](#table-of-contents) [koch\_magnet](https://github.com/goedel-gang/koch_magnet)

Dynamic Koch-snowflake-like-fractal-drawer. You use the mouse to control the
spike's point's coordinates, and the keys 1-9+0 to control the coordinates of
the spike's base, modified with SHIFT if you want to move the left one.

![screenshot](https://github.com/goedel-gang/koch_magnet/blob/master/screenshots/win_screenshot_20190626_172556.png)
![screenshot](https://github.com/goedel-gang/koch_magnet/blob/master/screenshots/win_screenshot_20190626_172603.png)
![screenshot](https://github.com/goedel-gang/koch_magnet/blob/master/screenshots/win_screenshot_20190626_172805.png)
![screenshot](https://github.com/goedel-gang/koch_magnet/blob/master/screenshots/win_screenshot_20190626_172853.png)
# [\[toc\]](#table-of-contents) Python-processing projects
### [\[toc\]](#table-of-contents) [asteroids](https://github.com/goedel-gang/asteroids)
My attempt at Saturn - asteroids orbiting a planet in 3d processing. Again, familiarisation. The asteroids are, of course, rainbow-coloured. It looks like this:

![screenshot](https://github.com/goedel-gang/asteroids/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [collatz\_tree](https://github.com/goedel-gang/collatz_tree)
Inspired by the Collatz conjecture. From the conjecture, one might be able to build a tree with root node 1 where all numbers feed back to 1, and any path down the tree is a Collatz path. Featuring a command-line script to generate (and draw a very pretty unicode picture of) a collatz tree, and a Processing file that draws an even prettier tree, where a `3n + 1` step goes left, and an `n / 2` step goes right, featuring some rainbow HSB colouring. If the Collatz conjecture is disproven, this program might not work.

Here is the Processing sketch in action:

![Screenshot](https://github.com/goedel-gang/collatz_tree/blob/master/screenshot.png)

And this is a sample of `CollatzTree.py`, to a depth of 20 with one extra space between branches (`$ python CollatzTree.py -m 20 -s 2`)

    1
    ├─2
    │ ├─4
    │ │ ├─8
    │ │ │ ├─16
    │ │ │ │ ├─32...
    │ │ │ │ └─5
    │ │ │ │   ├─10
    │ │ │ │   │ ├─20
    │ │ │ │   │ │ ├─40...
    │ │ │ │   │ │ └─┤
    │ │ │ │   │ └─3
    │ │ │ │   │   ├─6
    │ │ │ │   │   │ ├─12
    │ │ │ │   │   │ │ ├─24...
    │ │ │ │   │   │ │ └─┤
    │ │ │ │   │   │ └─┤
    │ │ │ │   │   └─┤
    │ │ │ │   └─┤
    │ │ │ └─┤
    │ │ └─1...
    │ └─
    └─
### [\[toc\]](#table-of-contents) [bounce\_3d](https://github.com/goedel-gang/bounce_3d)
Very simple bouncing balls using Processing's 3d engine. Starting to familiarise with translation and rotation, and how to effectively fit OO in 3-D, and use alpha channels in 3D. It looks like this:

![screenshot](https://github.com/goedel-gang/bounce_3d/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [bubbles](https://github.com/goedel-gang/bubbles)
Neon kinda bubbles that merge into one another. Makes for a kind of intereseting screensaver. There are a number of parameters - they're currently set to a pretty stable state. Decrease loss / increase some defaults for more action.

Here is a screenshot with bubbles in neon mode, with a couple of extra mayhem bubbles added on top of defaults:

![screenshot](https://github.com/goedel-gang/bubbles/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [perl](https://github.com/goedel-gang/perl)
Has nothing to do with Perl. Rather, with George Perlin and Perlin noise. A couple of small pieces of code exploring the applications of Perlin noise in various dimensions. Here are some screenshots:

Dual 1-dimensional Perlin noise to move a point through 2-d space, with time as input (not very inspiring, I know):

![screenshot](https://github.com/goedel-gang/perl/blob/master/screenshots/perl_11.png)

2-dimensional Perlin noise to generate a moving, smooth curve (with added rainbows). Varies with x and time.

![screenshot](https://github.com/goedel-gang/perl/blob/master/screenshots/perl_2.png)

3-dimensional Perlin noise to generate a smooth, moving, heatmap type thing. Varies with x, y, and time

![screenshot](https://github.com/goedel-gang/perl/blob/master/screenshots/perl_3.png)

There is also [a video](https://youtu.be/gF6Wr106b4M) of this one.

Lots of Perlin noise to move a box through 3-D space a la Wingardium Leviosa. Varies a lot.

![screenshot](https://github.com/goedel-gang/perl/blob/master/screenshots/boxperl.png)
### [\[toc\]](#table-of-contents) [drag\_grav](https://github.com/goedel-gang/drag_grav)
Some experimentation with my fun new model of movement. Terminal velocity isn't directly enforced, but a drag coefficient is - acceleration due to gravity is constant, but the velocity decays exponentially, making it naturally reach a limit/peter out.

Here is what it looks like:

![screenshot](https://github.com/goedel-gang/drag_grav/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [kaleidoscope](https://github.com/goedel-gang/kaleidoscope)
Kaleidoscope-inspired pretty processing thing. Shapes are not allowed to collide. Generates sides using arctangent interpolation, and does a nice rolling effect to both save framerate and show off Python generators to all the java-processers.

Here is a screenshot of the rolling setup in progress:

![screenshot](https://github.com/goedel-gang/kaleidoscope/blob/master/partial.png)

And here is a finished kaleidoscope:

![screenshot](https://github.com/goedel-gang/kaleidoscope/blob/master/full.png)

And here is a larger kaleidoscope which is easier to see:

![screenshot](https://github.com/goedel-gang/kaleidoscope/blob/master/big.png)
### [\[toc\]](#table-of-contents) [lightning](https://github.com/goedel-gang/lightning)
Attempt at simulating a lightning-like figure (Lichtenberg figure). Works by keeping a field of potential electrons and randomly expanding into one. More frequently accessed branches thicken. Uses all sorts of haphazard optimisation to make it run, whatsoever. It uses a nice little trick so that a branches prevalence first grows rapidly, then slows - interpolation on the square root. Of course, features rainbow support.

Here is an example of it in action:

![screenshot](https://github.com/goedel-gang/lightning/blob/master/screenshots/lichten.png)

Here is a display of the "electron field":

![screenshot](https://github.com/goedel-gang/lightning/blob/master/screenshots/electrons.png)

[Here](https://www.youtube.com/watch?v=o_IPt9EWTpg) is a short video of it in action.
### [\[toc\]](#table-of-contents) [bfs\_koch](https://github.com/goedel-gang/bfs_koch)
Breadth first Koch snowflake, similar to the sierpinski triangle. It looks like this:

![screenshot](https://github.com/goedel-gang/bfs_koch/blob/master/screenshot.png)

It's a bit off as I've turned off smoothing, but overall I prefer it this way.
### [\[toc\]](#table-of-contents) [stepbysierp](https://github.com/goedel-gang/stepbysierp)
A breadth-first Sierpinski triangle, using generators. It has been optimised a lot so that each stack frame needs only track coordinates, and crucially they share triangle dimension information. Originally, whenever a new depth was reached, the program stuttered as it had to create an exponential number of new generators with new calculations. It looks like this:

![screenshot](https://github.com/goedel-gang/stepbysierp/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [py\_lerpbez](https://github.com/goedel-gang/py_lerpbez)
My first proper Python-processing project. It generates an arbitrary order Bezier Curve, showing some of the behind the scenes too. It's become slowly but steadily more bloated to the point where it can now also draw all subcurves, or draw rainbows.

Here it is in action:

![screenshot](https://github.com/goedel-gang/py_lerpbez/blob/master/screenshots/bez.png)

And with added rainbows:

![screenshot](https://github.com/goedel-gang/py_lerpbez/blob/master/screenshots/rainbow.png)
### [\[toc\]](#table-of-contents) [road\_screen](https://github.com/goedel-gang/road_screen)
My first foray into three-dimensional graphics programming. Done with purely 2-D primitives. Distance/perspective is simulated by interpolating on an arctangent, to confine a potentially infinite range (viewer to horizon) to a bounded range. Don't run it if you love your CPU.

This is what it looks like:

![screenshot](https://github.com/goedel-gang/road_screen/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [rubiks\_cube](https://github.com/goedel-gang/rubiks_cube)
Visual interface to my Rubik's cube model, in python-processing using P3D.

Here are some screenshots:

![Screenshot](https://github.com/goedel-gang/rubiks_cube/blob/master/solved_ss.png "Solved state")
![Screenshot](https://github.com/goedel-gang/rubiks_cube/blob/master/scrambled_ss.png "Scrambled state")
### [\[toc\]](#table-of-contents) [ship\_game](https://github.com/goedel-gang/ship_game)
One of the earlier Python-processing projects. A ship using drag coefficients, and a half-baked autopilot. It has features for random walking using Perlin noise, and for trying to get to a destination (the mouse). Pretty options for exhaust fumes are available. Here is a sample screenshot, using confetti exhaust, with the help of the perlin autopilot:

![screenshot](https://github.com/goedel-gang/ship_game/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [wind\_fans](https://github.com/goedel-gang/wind_fans)
Simulates nutella-style turbines being blown by the mouse. Can be a little intensive. They are all made in beautiful HSB colours. It looks like this (just pretend they're spinning):

![screenshot](https://github.com/goedel-gang/wind_fans/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [langton](https://github.com/goedel-gang/langton)
Langton's ant in Processing, supporting different setups. I'm currently unsure if there's a bug - use at own risk. It wraps around the screen, so highways can collide - it ends up somethign like this:

![screenshot](https://github.com/goedel-gang/langton/blob/master/langton.png)
### [\[toc\]](#table-of-contents) [squiggles](https://github.com/goedel-gang/squiggles)
A squiggle generator in Python processing. Works by generating a square tesselation of "tiles" which each have two quarter circles at opposing corners, with radius half the base of the square, such that an arc ends at each midpoint of a square edge. These tiles are then randomly rotated. It "walks" between two orientations. It looks like this at the start:

![screenshot](https://github.com/goedel-gang/squiggles/blob/master/start.png)

And nearer the middle:

![screenshot](https://github.com/goedel-gang/squiggles/blob/master/mid.png)
### [\[toc\]](#table-of-contents) [tenprint](https://github.com/goedel-gang/tenprint)
"10 print" in Python-processing. Inspired by [Daniel Shiffman's video](https://youtu.be/bEyTZ5ZZxZs). Rather than statically generating random positions and leaving it, each slash has a chance of mutating each frame. The starting state is an aligned grid:

![screenshot](https://github.com/goedel-gang/tenprint/blob/master/screenshots/start.png)

And as the program runs, it deforms into something more like this:

![screenshot](https://github.com/goedel-gang/tenprint/blob/master/screenshots/inprogress.png)

You can see that they don't just snap, but interpolate themselves to where they need to be. The slashes aren't often precisely aligned - this is a natural side effect of allowing them to turn in a continuum rather than flipping between binary states.

This also illustrates the mildly interesting property that this does actually approach a half/half distribution.

Lastly, [here](https://youtu.be/eZNffI1R3xM) is a video of it in action.
### [\[toc\]](#table-of-contents) [mod\_mult](https://github.com/goedel-gang/mod_mult)
Visualisation of a modular multiplication table in processing. Generates slowly. It looks like this:

![screenshot](https://github.com/goedel-gang/mod_mult/blob/master/screenshots/half.png)
![screenshot](https://github.com/goedel-gang/mod_mult/blob/master/screenshots/fin.png)

and in higher resolution:
![screenshot](https://github.com/goedel-gang/mod_mult/blob/master/screenshots/higher.png)
### [\[toc\]](#table-of-contents) [lsystems](https://github.com/goedel-gang/lsystems)

A general approach to L-systems in Python processing, using layered generators,
with a couple implemented. Due to the use of generators they also generate
gradually, giving a nice "drawing" effect, rather than blocking for several
frames. Basically the beauty of it is that having written all the "library"
code, I can define fractals as simply as

```Python
sierpinski = LSystemFractal(
    "Sierpinski's Gasket",
    "F+G+G",
    {"F": "F+G-F-G+F",
     "G": "GG"},
    lambda t, d: standard_rules(t, 120),
    lambda d: 2 ** d,
    9)
```

As you can see, it's currently also very easy to read.

Even though I say so myself, the colouring effects are really cool. Not only are
they all rainbow coloured, but the rainbow is extrapolated from the reproduction
rules of each L-system automatically. Basically, when you're only interested in
symbol count, you can use a linear transition matrix and exponentiation by
squaring to calculate the count of each symbol at the `n`th iteration in
`log(n)` time. This is a totally unnecessary but nevertheless awesome
optimisation to be able to make.

The version used to generate [this video](https://youtu.be/kf3hgNMjzX4) is at
the [video tag](https://github.com/goedel-gang/lsystems/tree/video).

Here are some screenshots:

![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/00_sierpinskis_gasket.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/01_the_dragon_curve.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/02_a_lindenmayer_fern.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/03_the_levy_c_curve.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/04_hilberts_spacefilling_curve.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/05_sierpinskis_gasket_hexagonal_variant.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/06_koch_snowflake.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/07_square_koch_curve.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/08_binary_tree.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/09_fibonacci_word_fractal.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/10_crystal.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/11_peano_curve.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/12_cantor_set.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/13_sierpinski_star.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/14_sierpinskis_carpet.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/15_krishna_anklets.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/16_mango.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/17_board.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/18_square_sierpinski.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/19_penrose_tiling.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/20_hexagonal_gosper.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/21_quadratic_gosper.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/22_bourke_triangle.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/23_bourkes_first_bush.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/24_bourkes_second_bush.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/25_bourkes_third_bush.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/26_saupes_bush.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/27_bourke_stick.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/28_bourke_weed.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/29_koch_island_1.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/30_koch_island_2.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/31_koch_island_3.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/32_minkowski_islandsausage.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/33_pentaplexity.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/34_bourke_rings.png)
![screenshot](https://github.com/goedel-gang/lsystems/blob/master/screenshots/35_bourke_2.png)
### [\[toc\]](#table-of-contents) [pong](https://github.com/goedel-gang/pong)
Pong game inspired by my teacher's warning not to write a Pong game. Has a neon
aesthetic with a sprinkling of Perlin noise and lots of vector calculations.

![screenshot](https://github.com/goedel-gang/pong/blob/master/pong.png)

Handily, you control both paddles so a friend is not required to play. If you
do have a friend, you can quickly swap between who's using the keyboard.
### [\[toc\]](#table-of-contents) [radial\_oscillation](https://github.com/goedel-gang/radial_oscillation)
A processing project on the graphing of polar functions for r in theta and time
by using successively more oscillating points on straight lines, inspired by
[this](https://www.reddit.com/r/oddlysatisfying/comments/82nbra/every_line_is_straight/)
post.

It's currently not very adaptable, the main problem being that it doesn't
necessarily know the period of a given function (eg given r = sin(theta/3 + t),
it has to plot theta from 0 to 6pi). This is also the function it's currently
set up to draw. Here are some screenshots of it as it progresses:

![screenshot](https://github.com/goedel-gang/radial_oscillation/blob/master/screenshots/startradial.png)
![screenshot](https://github.com/goedel-gang/radial_oscillation/blob/master/screenshots/moreradial.png)
![screenshot](https://github.com/goedel-gang/radial_oscillation/blob/master/screenshots/evenmoreradial.png)
![screenshot](https://github.com/goedel-gang/radial_oscillation/blob/master/screenshots/radial_fin.png)

A video of it can be found [here](https://youtu.be/H8MlbKC8moY), and
[here](https://gfycat.com/EllipticalMellowIndianringneckparakeet) is a webm
(GIF). [here](https://gfycat.com/AshamedAcceptableAustralianfurseal) is a gif
of a different function.
### [\[toc\]](#table-of-contents) [ascii\_art](https://github.com/goedel-gang/ascii_art)
Converting images to ASCII using Processing. It's not a very complicated
algorithm but a very satisfying output. All it needs to do is sample brightness
over the appropriate rectangles, although it spends some time on scaling
calculations. Here are a couple of examples:

![screenshot](https://github.com/goedel-gang/ascii_art/blob/master/screenshots/tim_ascii.png)
![screenshot](https://github.com/goedel-gang/ascii_art/blob/master/screenshots/shimmi_ascii.png)
### [\[toc\]](#table-of-contents) [hanoi](https://github.com/goedel-gang/hanoi)
Towers of Hanoi solver - an abstract solution that provides a generator over
swaps and mutates the problem array, and checks for correctness when run in
addition to a Processing sketch that displays the towers.

![screenshot](https://github.com/goedel-gang/hanoi/blob/master/screenshot.png)
### [\[toc\]](#table-of-contents) [mandeldot](https://github.com/goedel-gang/mandeldot)
A mandelbrot orbit plotter.

![screenshot](https://github.com/goedel-gang/mandeldot/blob/master/win_screenshot_20190326_183150.png)
![screenshot](https://github.com/goedel-gang/mandeldot/blob/master/win_screenshot_20190326_182523.png)
![screenshot](https://github.com/goedel-gang/mandeldot/blob/master/win_screenshot_20190326_182803.png)
### [\[toc\]](#table-of-contents) [gcd\_plot](https://github.com/goedel-gang/gcd_plot)

Plotting GCD(x, y) by hue. Despite it being a discrete plot, you get some funky
functions.

![screenshot](https://github.com/goedel-gang/gcd_plot/blob/master/win_screenshot_20190330_125227.png)
![screenshot](https://github.com/goedel-gang/gcd_plot/blob/master/win_screenshot_20190330_125243.png)
### [\[toc\]](#table-of-contents) [bifurcation\_logistic\_map](https://github.com/goedel-gang/bifurcation_logistic_map)

A plotter for the bifurcation diagram of the logistic map. It's fairly dumb, but
it seems to work. Not yet got a very developed UI - the only configurability is
through tweaking global constants.

![screenshot](https://github.com/goedel-gang/bifurcation_logistic_map/blob/master/win_screenshot_20190330_125830.png)
