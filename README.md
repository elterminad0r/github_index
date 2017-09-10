# github\_inventory
A bit of a meta-project on creating a nicer index of my github repositories. Partially motivated because I'm too greedy to do with only 6 pinned repositories. It's just about stable enough to function. It features several sub-utilities I chain together, including directory-searching and API-json reading. It files my projects under subcategories, and concatenates together readmes under a category heading.
## Table of Contents
1. [My Postscript Repository](#my-postscript-repository)
    1. [Postscript](#postscript)
1. [Miscellaneous Python projects](#miscellaneous-python-projects)
    1. [Sudoku](#sudoku)
    1. [Calcudoku](#calcudoku)
    1. [A453](#a453)
    1. [Linked lists](#linked-lists)
    1. [Cube](#cube)
    1. [urn the front face of the cube](#urn-the-front-face-of-the-cube)
    1. [Punnet Squares](#punnet-squares)
    1. [cookies](#cookies)
    1. [Yahtzee](#yahtzee)
    1. [queens](#queens)
    1. [hangman](#hangman)
1. [rc](#rc)
    1. [rc](#rc)
1. [My Python basics repo](#my-python-basics-repo)
    1. [backtobasics](#backtobasics)
1. [java-processing projects](#java-processing-projects)
    1. [alphabet](#alphabet)
    1. [balls](#balls)
    1. [cars](#cars)
    1. [circles](#circles)
    1. [colourconway](#colourconway)
    1. [mazes](#mazes)
    1. [pendulums](#pendulums)
    1. [pixel\_sorting](#pixel\_sorting)
    1. [pythanimated](#pythanimated)
    1. [rainbow\_lines](#rainbow\_lines)
    1. [regen\_soup](#regen\_soup)
    1. [shading](#shading)
    1. [snowflakes](#snowflakes)
    1. [square\_filling\_circle](#square\_filling\_circle)
    1. [UI\_demo](#ui\_demo)
    1. [turtles](#turtles)
    1. [s\_zoom](#s\_zoom)
1. [Implementations of games in Processing](#implementations-of-games-in-processing)
    1. [platformer](#platformer)
    1. [snake](#snake)
    1. [spaceinvaders](#spaceinvaders)
    1. [tetris](#tetris)
1. [projects on "chaos" demonstrations](#projects-on-"chaos"-demonstrations)
    1. [sierp\_demo](#sierp\_demo)
    1. [chaos\_spreadsheet](#chaos\_spreadsheet)
1. [massive project on moire effect](#massive-project-on-moire-effect)
    1. [moire\_draggable](#moire\_draggable)
1. [Mandelbrot and julia sets](#mandelbrot-and-julia-sets)
    1. [julia](#julia)
    1. [mandelbrot](#mandelbrot)
1. [Python-processing projects](#python-processing-projects)
    1. [asteroids](#asteroids)
    1. [collatz\_tree](#collatz\_tree)
    1. [bounce\_3d](#bounce\_3d)
    1. [bubbles](#bubbles)
    1. [perl](#perl)
    1. [drag\_grav](#drag\_grav)
    1. [kaleidoscope](#kaleidoscope)
    1. [lightning](#lightning)
    1. [bfs\_koch](#bfs\_koch)
    1. [stepbysierp](#stepbysierp)
    1. [py\_lerpbez](#py\_lerpbez)
    1. [road\_screen](#road\_screen)
    1. [rubiks\_cube](#rubiks\_cube)
    1. [ship\_game](#ship\_game)
    1. [wind\_fans](#wind\_fans)
## My Postscript Repository
### [Postscript](https://github.com/elterminad0r/Postscript)
Some of my Postscript (the printer language) projects - some early, some less so. `zut` means pile of rubbish. There's lots to do with polysymmetry and fractals, and then some other stuff. Postscript is actually a really fun language for static graphics programming - I love its syntax, model of stack frames (you have to manually push a new local namespace dictionary to the stack). It's powerful - featuring programmatic features like for loops, while maintaining good drawing primitives and vector graphics. It's actually pretty good for fractals, but also polysymmetric tilings and more. Here are a couple of my favourites:

![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/penrose.svg)
![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/ster.svg)
![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/minkowski.svg)
![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/star2.svg)


A few more that I really wanted to add here, but have moved to a directory of SVGs (they should be viewable in browser): [svgs](https://github.com/elterminad0r/Postscript/blob/master/svgs/). There are also `pdf` files, but they don't seem to render very well. They're there because they're a necessary intermediate stage to my SVG generation method - I first use `ps2pdf`, and then `pdf2svg`. It seems to be working quite well so it's good enough for me. I've tested that all of these work with my version of GhostScript - you should also be able to open them in Preview on MacOS or some kind of illustrator/graphics program.
## Miscellaneous Python projects
### [Sudoku](https://github.com/elterminad0r/sudoku)
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
### [Calcudoku](https://github.com/elterminad0r/Calcudoku)
A simple brute force solver for an 8\*8 'calcudoku'. A `Calcudoku` is given a number of *regions*, with *targets* and *operations*. A region is a set of adjacent cells (although the program could handle non-adjacent cells), where they are given an operation and a target. The Target is an integer which must be reached by combining the integers in the cells using the operation, ie:

    target = 6

operation | explanation
--- | ---
`+` | The numbers should add up to 6.
`-` | The largest number subtract *all* the rest of the numbers should be 6.
`*` | The product of the numbers should be 6.
`/` | The largest number divided by *all* the rest of the numbers should be 6.

These regions are modelled in a pretty nicely structured OO model.

Input works like so: each region is defined and assigned to a character, and then a grid of characters is provided. You can refer to [ex.txt](https://github.com/elterminad0r/Calcudoku/blob/master/ex.txt) for a fully specified input file. Using it as input, with `cat ex.txt | python interf.py`, this output is produced:

    8 5 7 1 4 2 3 6 
    7 3 4 5 6 1 2 8 
    4 7 2 3 8 6 1 5 
    3 1 8 6 2 4 5 7 
    5 8 6 2 7 3 4 1 
    6 2 1 4 5 8 7 3 
    2 6 3 7 1 5 8 4 
    1 4 5 8 3 7 6 2 
### [A453](https://github.com/elterminad0r/A453)
From my GCSE computing course - see [my full writeup](https://github.com/elterminad0r/A453/blob/master/writeup.pdf) (be warned - it's big. I'd recommend downloading it rather than viewing it inline - I've crashed a couple of browser sessions by trying the latter). It's a **heavily** type-annotated collection of scripts in Python, which perform various forms of naive and less naive compression on text. It initially uses a very naive system of building an index of words and writing "pointers" to words in that index, where the pointers are space-separated base-10 integers in ASCII. This is of course a tremendous waste of a byte - I later go on to use variable-length prefix encodings and raw binary data-files to make some significant gains. It's nowhere near something like LZW compression in terms of speed or compressive factor, but I think that for a Python script given the initial constraints, it's not bad at all. Also features some heavy unit testing, and modularisation, and a pretty decent interface for input/output using argparse.

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
### [Linked lists](https://github.com/elterminad0r/linked_list)
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
### [Cube](https://github.com/elterminad0r/Cube)
My project expressing a Rubik's cube as a list of integers representing colours, and moves on the cube as permutations on the list. Uses some operator overloading for some pretty expressive syntax to build up the set of moves on the cube. The object model allows chaining and merging of permutations, allowing you to build up to something like this:

```Python
### [urn the front face of the cube](https://github.com/elterminad0r/Cube)
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

For prettier visualisations, refer to my parallel [Processing project](https://github.com/elterminad0r/rubiks_cube).

This project also explores some more group-theoretical aspects of the cube - eg how many times must a set of moves be repeated to return a cube to its original state. An interesting optimisation in this is finding "sub-cycles" in the permutation formed by the set of moves and determining the LCM of the lengths of these sub-cycles.
### [Punnet Squares](https://github.com/elterminad0r/Punnet)
Some leftover code for Punnet square generation, from a stackoverflow question. The question was deleted, so I decided to see how illegible I could make my code. Was once intended to become a `code-golf` challenge, but it was too similar to another challenge. It uses some neat generator/unpacking tricks. If tokens are shortened appropriately, you can get this to be pretty short.

`$ python code.py Xx xx`

	 |X |x
	-+---+--
	x|Xx|xx
	-+---+--
	x|Xx|xx
### [cookies](https://github.com/elterminad0r/cookies)
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
### [Yahtzee](https://github.com/elterminad0r/yahtzee)
A work in progress - hoping to end up building a kind of nice yahtzee framework and then try to implement some different yahtzee playing algorithms (maybe monte carlo, neural network, etc). Stemming from mid-yahtzee computing banter. It might be interesting to see the distribution of scores achieved by different algorithms, such as a greedy yahtzee-seeking algorithm, or a more measured greedy algorithm searching for intersections between dice and targets (maybe weighting by scores / ease). All sorts of fun opportunities are available - reading random integers from `/dev/urandom`, synchronizing different algorithms into one stream of dice of "game", implementing algorithms as generators that require sent variables, secure extra-algorithm move validation..
### [queens](https://github.com/elterminad0r/queens)
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
### [hangman](https://github.com/elterminad0r/hangman)
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

![screenshot](https://github.com/elterminad0r/hangman/blob/master/fail.png)
## rc
### [rc](https://github.com/elterminad0r/rc)
A collection of copies of my rc files for easier access. They're not particularly pretty - I haven't put much effort into them. Generally, I'm satisfied to use what works. I'm happy enough to introduce obscure aliases I'll forget though. `vimrc` contains a number of things specific to my terminal.

I use `izaak-zshrc` for my `rc` file for `zsh`, as to allow `oh-my-zsh`'s default file to be preserved/keep my file safe. It contains a preposterous volume of aliases, beware.

I have two email accounts set up with `mutt`, with obscured passwords. `gmail` is aliases to load my `gmail` credentials, etc. I've emulated `muttrc` syntax with a `sh` shebang.
## My Python basics repo
### [backtobasics](https://github.com/elterminad0r/backtobasics)
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
## java-processing projects
### [alphabet](https://github.com/elterminad0r/alphabet)
Shading the screen using letters of the alphabet in Processing. All printable ascii keys on the keyboard are accessible from the keyboard. Some special keys (space, enter) are used for acceleration. ASCII value scales with the x value. Here are some screenshots:

![screenshot](https://github.com/elterminad0r/alphabet/blob/master/screenshots/alph1.png)

And after a couple of years of typing:

![screenshot](https://github.com/elterminad0r/alphabet/blob/master/screenshots/alph2.png)
### [balls](https://github.com/elterminad0r/balls)
Simple, slightly buggy implementation of balls that can bounce off both each other and walls. It ends up looking pretty dynamic. It uses an equation for circle collision from wikipedia. The problem is that sometimes a ball will clip into another ball and start a weird orbit/mating dance. Especially happens when there's disparity between ball radii. It looks like this:

![screenshot](https://github.com/elterminad0r/balls/blob/master/screenshot.png)
### [cars](https://github.com/elterminad0r/cars)
Early experimenting in OOP in java-processing. Animates a bunch of rectangles and their attributes (colour, size, position, rotation etc). It looks like this:

![screenshot](https://github.com/elterminad0r/cars/blob/master/screenshot.png)
### [circles](https://github.com/elterminad0r/circles)
Neat little effect in processing an grid of circles, where radius increases the closer to the mouse. Produces quite a simple yet satisfying effect - example:

![screenshot](https://github.com/elterminad0r/circles/blob/master/screenshot.png)
### [colourconway](https://github.com/elterminad0r/colourconway)
Conway's game of life, with colourisation related to recent activity. It's pretty but the code is a godawful mess I might try to wade into one day. Here it is in action:

![screenshot](https://github.com/elterminad0r/colourconway/blob/master/screenshot.png)
### [mazes](https://github.com/elterminad0r/mazes)
Maze generation algorithms in Processing, by random walking and "knocking down" walls, and backtracking when cornered. All cells are guaranteed to be reachable, so any combination of cells can be taken as start-end (top-left bottom-right, for example). Features solutions and slower, frame-by-frame generation. Here it is in action:

![screenshot](https://github.com/elterminad0r/mazes/blob/master/screenshots/nopath.png)
![screenshot](https://github.com/elterminad0r/mazes/blob/master/screenshots/path.png)
![screenshot](https://github.com/elterminad0r/mazes/blob/master/screenshots/slo.png)
### [pendulums](https://github.com/elterminad0r/pendulums)
A little more experimentation with Java OO in processing. Uses the simple model of pendulums to produce a slow interference effect. Here's a static screenshot:

![screenshot](https://github.com/elterminad0r/pendulums/blob/master/screenshot.png)

It doesn't quite deliver the effect of them in motion, but you can see the interference/general idea.
### [pixel\_sorting](https://github.com/elterminad0r/pixel_sorting)
Sorting rows of pixels in an image by brightness, in Processing. Most of the work was done by Daniel Shiffman.

With this as input:

![input sunflower](https://github.com/elterminad0r/pixel_sorting/blob/master/data/sunflower.jpg)

It can produce this:

![output](https://github.com/elterminad0r/pixel_sorting/blob/master/sorted.jpg)

While it's running, it looks like this:

![screenshot](https://github.com/elterminad0r/pixel_sorting/blob/master/intermediary.png)
### [pythanimated](https://github.com/elterminad0r/pythanimated)
Relatively simple code to eternally increment animate the angle of a rendered Pythagoras Tree fractal.

![screenshot](https://github.com/elterminad0r/pythanimated/blob/master/screenshot.png)
### [rainbow\_lines](https://github.com/elterminad0r/rainbow_lines)
A simpler project, doing some slightly diagonal rainbow shading on a canvas.

Here is a screenshot:

![Screenshot](https://github.com/elterminad0r/rainbow_lines/blob/master/screenshot.png)
### [regen\_soup](https://github.com/elterminad0r/regen_soup)
Simple OO to display a kind of weird soup-like substance with some mildly hallucinogenic rainbows. It doesn't use drawing primitives to draw the rainbows as Processing doesn't support any kind of gradient, so it actually directly modifies the pixel array. It looks like this:

![screenshot](https://github.com/elterminad0r/regen_soup/blob/master/screenshot.png)
### [shading](https://github.com/elterminad0r/shading)
Processing "rainbow shading" by many random diagonal lines, colour shifting according to x position. It looks like this:

![screenshot](https://github.com/elterminad0r/shading/blob/master/screenshot.png)
### [snowflakes](https://github.com/elterminad0r/snowflakes)
From a Christmas CS lesson once upon a time - snowflakes simulated by ascii characters. It looks like this:

![screenshot](https://github.com/elterminad0r/snowflakes/blob/master/screenshot.png)
### [square\_filling\_circle](https://github.com/elterminad0r/square_filling_circle)
Squares that fill up the area of a circle, inspired by the classic pi paradox (as the total area of the squares approaches the area of the circle, then surely the perimeter does so too, which would lead to pi=4). It uses a real beauty of an equation worked through by hand to find the intersection of a line with gradient 1 and a circle arc - 

    intercept = 0.5 * (sqrt(-a * a + 2 * a * (b + c - d) - b * b - 2 * b * c + 2 * b * d - c * c + 2 * c * d - d * d + 2 * r * r) + a + b + c - d) - c;

Here is a screenshot of it in action:

![screenshot](https://github.com/elterminad0r/square_filling_circle/blob/master/screenshot.png)
### [UI\_demo](https://github.com/elterminad0r/UI_demo)
A simpler implementation/demonstration of my UI elements in Processing, later to be used more in `moire_draggable`. It does a lot of event handling and delegation through static methods to abstract that from the main pde sketch. It uses some vector arithmetic for some of the features. It looks like this:

![screenshot](https://github.com/elterminad0r/UI_demo/blob/master/screenshot.png)
### [turtles](https://github.com/elterminad0r/turtles)
Custom turtle implementation in Processing, used to have multiple turtles follow the same instructions (from keyboard) for symmetric kinda pretty rainbow patterns. Here is what it looks like:

![screenshot](https://github.com/elterminad0r/turtles/blob/master/screenshot.png)
### [s\_zoom](https://github.com/elterminad0r/s_zoom)
A kind of inefficient sketch that tries to emulate the effect of infinitely zooming in on the top part of a Sierpinski Triangle. It looks like this:

![screenshot](https://github.com/elterminad0r/s_zoom/blob/master/screenshot.png)
## Implementations of games in Processing
### [platformer](https://github.com/elterminad0r/platformer)
An extremely bare-bones platformer in processing - both in content and implementation. Its collision detection, after much work, seems to be pretty flawless. It should be relatively easy to add more platorms. Here is what it looks like - be warned that I'm a prolific graphic designer:

![screenshot](https://github.com/elterminad0r/platformer/blob/master/screenshot.png)

The upright rectangle is the protagonist, and the sideways rectangles are platforms. If Thomas was alone can do it, so can I.
### [snake](https://github.com/elterminad0r/snake)
The game Snake in Processing. Not a particularly clear implementation. The snake is rainbow coloured. There is a known bug with the score-text, but I'm not feeling motivated enough to fix it. It also features some very well hidden cheat codes. It looks like this:

![screenshot](https://github.com/elterminad0r/snake/blob/master/screenshot.png)
### [spaceinvaders](https://github.com/elterminad0r/spaceinvaders)
Kind of old implementation of Space Invaders I did in processing. It serves as a great showcase of my mastery of graphic design. In fact, I'm starting to worry I've peaked too early in my career:

![screenshot](https://github.com/elterminad0r/spaceinvaders/blob/master/screenshot.png)
### [tetris](https://github.com/elterminad0r/tetris)
Old implementation of Tetris in processing. At last, a game with graphics I can understand. The pieces and their rotations are all hardcoded. This suffers from the same bug as my snake game. Here's my attempt at playing it while taking a screenshot:

![screenshot](https://github.com/elterminad0r/tetris/blob/master/screenshot.png)
## projects on "chaos" demonstrations
### [sierp\_demo](https://github.com/elterminad0r/sierp_demo)
processing implementation of the "chaos game", with a couple of interactive features. The game works as follows: Take a point in the middle of a triangle. Choose a random corner. Take the point directly in between that corner and your current point. Make this your new point (remember to draw old points). This can produce some interesting results, given automation:

First couple of points:

![screensaver](https://github.com/elterminad0r/sierp_demo/blob/master/screenshots/early_stage.png)

A few more:

![screensaver](https://github.com/elterminad0r/sierp_demo/blob/master/screenshots/later.png)

A **lot** more, and shrunken points:

![screensaver](https://github.com/elterminad0r/sierp_demo/blob/master/screenshots/latest.png)

Fancy that.
### [chaos\_spreadsheet](https://github.com/elterminad0r/chaos_spreadsheet)
Illustration of the chaotic behaviour of the logistic map function (used for some interactive demoing once upon a time). Acts as a programmatic, slightly enhanced version of just generating the logistic map in a spreadsheet and plotting it. Features animation and some fine control over parameters. It looks like this (but animated):

![screenshot](https://github.com/elterminad0r/chaos_spreadsheet/blob/master/screenshot.png)
## massive project on moire effect
### [moire\_draggable](https://github.com/elterminad0r/moire_draggable)
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

![screenshot](https://github.com/elterminad0r/moire_draggable/blob/master/screenshots/hex.png)
![screenshot](https://github.com/elterminad0r/moire_draggable/blob/master/screenshots/radial.png)

Both of these were narrowly obtained before my laptop melted
## Mandelbrot and julia sets
### [julia](https://github.com/elterminad0r/julia)
Julia set visualisation next to mandelbrot set, illustrating what a julia set is (kind of) and more so its correspondance with the mandelbrot set.

As a Julia set takes a complex number as input, the mouse coordinates can serve as input. When this is put together with the mandelbrot set, something interesting happens.. You can easily find "interesting" Julia sets - move the mouse along the border of the Mandelbrot set.

Here are just a couple of examples:

![screenshot](https://github.com/elterminad0r/julia/blob/master/screenshots/julia1.png)
![screenshot](https://github.com/elterminad0r/julia/blob/master/screenshots/julia2.png)
![screenshot](https://github.com/elterminad0r/julia/blob/master/screenshots/julia3.png)
![screenshot](https://github.com/elterminad0r/julia/blob/master/screenshots/julia4.png)
### [mandelbrot](https://github.com/elterminad0r/mandelbrot)
This is a program in java-processing that renders the mandelbrot set. This set is defined as the set of the complex numbers, c such that there is no divergence when 0 is iterated under f(z) = z^2 + c The program works by simply iterating and observing if this number becomes large.  The speed of divergence is then used to give colourings.  The parameters kept track of are - x, y, scale, iteration cap, multibrot value (alternative exponent for z), width and height. See [usage.md](https://github.com/elterminad0r/mandelbrot/blob/master/usage.md) for info about the usage of the sketch.

It supports some mildly sophisticated serialisation - in string format. Any rendering can be described in a couple of terms (x, y, scale, width height, multibrot) which can be quite compactly encoded. This is then stored as the **filename** of any image you save from the sketch. What a stroke of genius, never has a filename been prettier than `-16od5ok4AH4+-NlkJp9kxyI4+w8SYn6PLXC4+Tf+3+uu+Ff.tiff`.

Here are three randomly chosen screenshots from my travels:

![screenshot](https://github.com/elterminad0r/mandelbrot/blob/master/screenshots/mandel1.png)
![screenshot](https://github.com/elterminad0r/mandelbrot/blob/master/screenshots/mandel2.png)
![screenshot](https://github.com/elterminad0r/mandelbrot/blob/master/screenshots/mandel3.png)

[Here](https://drive.google.com/drive/folders/0B3EHq-o9udUMQ2pyZlJKQWZlcDA?usp=sharing) is my full collection of higher quality serialisations for ayone interested.
## Python-processing projects
### [asteroids](https://github.com/elterminad0r/asteroids)
My attempt at Saturn - asteroids orbiting a planet in 3d processing. Again, familiarisation. The asteroids are, of course, rainbow-coloured. It looks like this:

![screenshot](https://github.com/elterminad0r/asteroids/blob/master/screenshot.png)
### [collatz\_tree](https://github.com/elterminad0r/collatz_tree)
Inspired by the Collatz conjecture. From the conjecture, one might be able to build a tree with root node 1 where all numbers feed back to 1, and any path down the tree is a Collatz path. Featuring a command-line script to generate (and draw a very pretty unicode picture of) a collatz tree, and a Processing file that draws an even prettier tree, where a `3n + 1` step goes left, and an `n / 2` step goes right, featuring some rainbow HSB colouring. If the Collatz conjecture is disproven, this program might not work.

Here is the Processing sketch in action:

![Screenshot](https://github.com/elterminad0r/collatz_tree/blob/master/screenshot.png)

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
### [bounce\_3d](https://github.com/elterminad0r/bounce_3d)
Very simple bouncing balls using Processing's 3d engine. Starting to familiarise with translation and rotation, and how to effectively fit OO in 3-D, and use alpha channels in 3D. It looks like this:

![screenshot](https://github.com/elterminad0r/bounce_3d/blob/master/screenshot.png)
### [bubbles](https://github.com/elterminad0r/bubbles)
Neon kinda bubbles that merge into one another. Makes for a kind of intereseting screensaver. There are a number of parameters - they're currently set to a pretty stable state. Decrease loss / increase some defaults for more action.

Here is a screenshot with bubbles in neon mode, with a couple of extra mayhem bubbles added on top of defaults:

![screenshot](https://github.com/elterminad0r/bubbles/blob/master/screenshot.png)
### [perl](https://github.com/elterminad0r/perl)
Has nothing to do with Perl. Rather, with George Perlin and Perlin noise. A couple of small pieces of code exploring the applications of Perlin noise in various dimensions. Here are some screenshots:

Dual 1-dimensional Perlin noise to move a point through 2-d space, with time as input (not very inspiring, I know):

![screenshot](https://github.com/elterminad0r/perl/blob/master/screenshots/perl_11.png)

2-dimensional Perlin noise to generate a moving, smooth curve (with added rainbows). Varies with x and time.

![screenshot](https://github.com/elterminad0r/perl/blob/master/screenshots/perl_2.png)

3-dimensional Perlin noise to generate a smooth, moving, heatmap type thing. Varies with x, y, and time

![screenshot](https://github.com/elterminad0r/perl/blob/master/screenshots/perl_3.png)

Lots of Perlin noise to move a box through 3-D space a la Wingardium Leviosa. Varies a lot.

![screenshot](https://github.com/elterminad0r/perl/blob/master/screenshots/boxperl.png)
### [drag\_grav](https://github.com/elterminad0r/drag_grav)
Some experimentation with my fun new model of movement. Terminal velocity isn't directly enforced, but a drag coefficient is - acceleration due to gravity is constant, but the velocity decays exponentially, making it naturally reach a limit/peter out.

Here is what it looks like:

![screenshot](https://github.com/elterminad0r/drag_grav/blob/master/screenshot.png)
### [kaleidoscope](https://github.com/elterminad0r/kaleidoscope)
Kaleidoscope-inspired pretty processing thing. Shapes are not allowed to collide. Generates sides using arctangent interpolation, and does a nice rolling effect to both save framerate and show off Python generators to all the java-processers.

Here is a screenshot of the rolling setup in progress:

![screenshot](https://github.com/elterminad0r/kaleidoscope/blob/master/partial.png)

And here is a finished kaleidoscope:

![screenshot](https://github.com/elterminad0r/kaleidoscope/blob/master/full.png)

And here is a larger kaleidoscope which is easier to see:

![screenshot](https://github.com/elterminad0r/kaleidoscope/blob/master/big.png)
### [lightning](https://github.com/elterminad0r/lightning)
Attempt at simulating a lightning-like figure (Lichtenberg figure). Works by keeping a field of potential electrons and randomly expanding into one. More frequently accessed branches thicken. Uses all sorts of haphazard optimisation to make it run, whatsoever. It uses a nice little trick so that a branches prevalence first grows rapidly, then slows - interpolation on the square root. Of course, features rainbow support.

Here is an example of it in action:

![screenshot](https://github.com/elterminad0r/lightning/blob/master/screenshots/lichten.png)

Here is a display of the "electron field":

![screenshot](https://github.com/elterminad0r/lightning/blob/master/screenshots/electrons.png)
### [bfs\_koch](https://github.com/elterminad0r/bfs_koch)
Breadth first Koch snowflake, similar to the sierpinski triangle. It looks like this:

![screenshot](https://github.com/elterminad0r/bfs_koch/blob/master/screenshot.png)

It's a bit off as I've turned off smoothing, but overall I prefer it this way.
### [stepbysierp](https://github.com/elterminad0r/stepbysierp)
A breadth-first Sierpinski triangle, using generators. It has been optimised a lot so that each stack frame needs only track coordinates, and crucially they share triangle dimension information. Originally, whenever a new depth was reached, the program stuttered as it had to create an exponential number of new generators with new calculations. It looks like this:

![screenshot](https://github.com/elterminad0r/stepbysierp/blob/master/screenshot.png)
### [py\_lerpbez](https://github.com/elterminad0r/py_lerpbez)
My first proper Python-processing project. It generates an arbitrary order Bezier Curve, showing some of the behind the scenes too. It's become slowly but steadily more bloated to the point where it can now also draw all subcurves, or draw rainbows.

Here it is in action:

![screenshot](https://github.com/elterminad0r/py_lerpbez/blob/master/screenshots/bez.png)

And with added rainbows:

![screenshot](https://github.com/elterminad0r/py_lerpbez/blob/master/screenshots/rainbow.png)
### [road\_screen](https://github.com/elterminad0r/road_screen)
My first foray into three-dimensional graphics programming. Done with purely 2-D primitives. Distance/perspective is simulated by interpolating on an arctangent, to confine a potentially infinite range (viewer to horizon) to a bounded range. Don't run it if you love your CPU.

This is what it looks like:

![screenshot](https://github.com/elterminad0r/road_screen/blob/master/screenshot.png)
### [rubiks\_cube](https://github.com/elterminad0r/rubiks_cube)
Visual interface to my Rubik's cube model, in python-processing using P3D.

Here are some screenshots:

![Screenshot](https://github.com/elterminad0r/rubiks_cube/blob/master/solved_ss.png "Solved state")
![Screenshot](https://github.com/elterminad0r/rubiks_cube/blob/master/scrambled_ss.png "Scrambled state")
### [ship\_game](https://github.com/elterminad0r/ship_game)
One of the earlier Python-processing projects. A ship using drag coefficients, and a half-baked autopilot. It has features for random walking using Perlin noise, and for trying to get to a destination (the mouse). Pretty options for exhaust fumes are available. Here is a sample screenshot, using confetti exhaust, with the help of the perlin autopilot:

![screenshot](https://github.com/elterminad0r/ship_game/blob/master/screenshot.png)
### [wind\_fans](https://github.com/elterminad0r/wind_fans)
Simulates nutella-style turbines being blown by the mouse. Can be a little intensive. They are all made in beautiful HSB colours. It looks like this (just pretend they're spinning):

![screenshot](https://github.com/elterminad0r/wind_fans/blob/master/screenshot.png)
