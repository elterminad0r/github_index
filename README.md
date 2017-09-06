# github\_inventory
A bit of a meta-project on creating a nicer index of my github repositories. Partially motivated because I'm too greedy to do with only 6 pinned repositories.
# My Postscript Repository
## [Postscript](https://github.com/elterminad0r/Postscript)
Some of my postscript projects - some early, some less so. `zut` means pile of rubbish.
# Miscellaneous Python projects
## [Sudoku](https://github.com/elterminad0r/sudoku)
A (brute-force) sudoku solver in Python.
## [A453](https://github.com/elterminad0r/A453)
From my GCSE computing course
## [Linked lists](https://github.com/elterminad0r/linked_list)
My Python linked list implementation. This is my expanded implementation from the HackerRank challenged. Note it's kind of half finished and untested so probably broken in all manner of fun ways. It's recursive so won't be able to handle any serious load due to Python's lack of tail call optimisation.
## [Calcudoku](https://github.com/elterminad0r/Calcudoku)
A simple brute force solver for an 8\*8 'calcudoku'.
## [Cube](https://github.com/elterminad0r/Cube)
My project expressing a Rubik's cube as a list of integers representing colours, and moves on the cube as permutations on the list. Uses some operator overloading for some pretty expressive syntax to build up the set of moves on the cube.
## [Punnet Squares](https://github.com/elterminad0r/Punnet)

Some leftover code for Punnet square generation, from a stackoverflow question. The question was deleted, so I decided to see how illegible I could make my code.
## [cookies](https://github.com/elterminad0r/cookies)
Some projects on "the cookie game" in Python. Includes an automatic opponent and some testing scripts on higher dimensions of the game.
## [Yahtzee](https://github.com/elterminad0r/yahtzee)

A work in progress - hoping to end up building a kind of nice yahtzee framework and then try to implement some different yahtzee playing algorithms (maybe monte carlo, neural network, etc)
# java-processing projects
## [asteroids](https://github.com/elterminad0r/asteroids)
Asteroids orbiting a planet in 3d processing. Again, familiarisation. The asteroids are, of course, rainbow-coloured.
## [balls](https://github.com/elterminad0r/balls)
Simple, slightly buggy implementation of balls that can bounce off both each other and walls.
## [cars](https://github.com/elterminad0r/cars)
Early experimenting in OOP in java-processing
## [circles](https://github.com/elterminad0r/circles)
Neat little effect in processing - radius increases the closer to the mouse.
## [colourconway](https://github.com/elterminad0r/colourconway)
Conway's game of life, with colourisation related to recent activity. It's pretty but the code is a godawful mess I might try to wade into one day.
## [mazes](https://github.com/elterminad0r/mazes)
Maze generation algorithms in Processing, featuring solutions and slower, frame-by-frame generation.
## [pendulums](https://github.com/elterminad0r/pendulums)
A little more experimentation with Java OO in processing. Uses the simple model of pendulums to produce a slow interference effect.
## [pixel\_sorting](https://github.com/elterminad0r/pixel_sorting)
Sorting rows of pixels in an image by brightness, in Processing. Most of the work was done by Daniel Shiffman.
## [pythanimated](https://github.com/elterminad0r/pythanimated)
Very simple code to eternally animate the angle of a Pythagoras Tree.
## [rainbow\_lines](https://github.com/elterminad0r/rainbow_lines)
A simpler project, doing some slightly diagonal rainbow shading on a canvas.
## [regen\_soup](https://github.com/elterminad0r/regen_soup)
Simple OO to display a kind of weird soup-like substance with some mildly hallucinogenic rainbows. It doesn't use drawing primitives to draw the rainbows as Processing doesn't support any kind of gradient, so it actually directly modifies the pixel array.
## [shading](https://github.com/elterminad0r/shading)

Processing fuzzy rainbow
## [snowflakes](https://github.com/elterminad0r/snowflakes)
From a Christmas CS lesson once upon a time - snowflakes simulated by ascii characters.
## [square\_filling\_circle](https://github.com/elterminad0r/square_filling_circle)
Squares that fill up the area of a circle, inspired by the classic pi paradox.
## [UI\_demo](https://github.com/elterminad0r/UI_demo)

A simpler implementation/demonstration of my UI elements in Processing, later to be used more in `moire_draggable`.
## [turtles](https://github.com/elterminad0r/turtles)
Custom turtle implementation in Processing, used to have multiple turtles follow the same instructions (from keyboard) for symmetric kinda pretty rainbow patterns.
# Implementations of games in Processing
## [platformer](https://github.com/elterminad0r/platformer)
An extremely bare-bones platformer in processing - both in content and implementation.
## [snake](https://github.com/elterminad0r/snake)
The game Snake in Processing. Not a particularly clear implementation.
## [spaceinvaders](https://github.com/elterminad0r/spaceinvaders)
Kind of old implementation of Space Invaders I did in processing. It serves as a great showcase of my mastery of graphic design.
## [tetris](https://github.com/elterminad0r/tetris)
Old implementation of Tetris in processing.
# projects on "chaos" demonstrations
## [sierp\_demo](https://github.com/elterminad0r/sierp_demo)
processing implementation of the "chaos game", with a couple of interactive features
## [chaos\_spreadsheet](https://github.com/elterminad0r/chaos_spreadsheet)
Illustration of the chaotic behaviour of the logistic map function (used for some interactive demoing once upon a time)
# massive project on moire effect
## [moire\_draggable](https://github.com/elterminad0r/moire_draggable)
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
# Mandelbrot and julia sets
## [julia](https://github.com/elterminad0r/julia)
Julia set visualisation next to mandelbrot set, illustrating what a julia set is (kind of) and more so its correspondance with the mandelbrot set.
## [mandelbrot](https://github.com/elterminad0r/mandelbrot)
Mandelbrot explorer in java-processing. Not very OO. Written when I wasn't very accustomed to java or processing, but works well enough. It can be a little intensive if not approached carefully.
# Python-processing projects
## [collatz\_tree](https://github.com/elterminad0r/collatz_tree)
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
## [bounce\_3d](https://github.com/elterminad0r/bounce_3d)
Very simple (ghostly) bouncing balls using Processing's 3d engine. Starting to familiarise.
## [bubbles](https://github.com/elterminad0r/bubbles)
Neon kinda bubbles that merge into one another. Makes for a kind of intereseting screensaver. There are a number of parameters - they're currently set to a pretty stable state. Decrease loss / increase some defaults for more action.
## [perl](https://github.com/elterminad0r/perl)
Has nothing to do with Perl. Rather, with George Perlin and Perlin noise. A couple of small pieces of code exploring the applications of Perlin noise.
## [drag\_grav](https://github.com/elterminad0r/drag_grav)
Some experimentation with my fun new model of movement. Terminal velocity isn't directly enforced, but a drag coefficient is - acceleration due to gravity is constant, but the velocity decays exponentially, making it naturally reach a limit/peter out.
## [kaleidoscope](https://github.com/elterminad0r/kaleidoscope)
Kaleidoscope-inspired pretty processing thing. Shapes are not allowed to collide. Generates sides using arctangent interpolation, and does a nice rolling effect to both save framerate and show off Python generators to all the java-processers.
## [lightning](https://github.com/elterminad0r/lightning)
Attempt at simulating a lightning-like figure (Lichtenberg figure). Works by keeping a field of potential electrons and randomly expanding into one.
## [bfs\_koch](https://github.com/elterminad0r/bfs_koch)
Breadth first Koch snowflake, similar to the sierpinski triangle.
## [stepbysierp](https://github.com/elterminad0r/stepbysierp)
A breadth-first Sierpinski triangle, using generators.
## [py\_lerpbez](https://github.com/elterminad0r/py_lerpbez)
My first proper Python-processing project. It generates an arbitrary order Bezier Curve, showing some of the behind the scenes too. It's become slowly but steadily more bloated to the point where it can now also draw all subcurves, or draw rainbows.
## [road\_screen](https://github.com/elterminad0r/road_screen)
My first foray into three-dimensional graphics programming. Done with purely 2-D primitives. Distance/perspective is simulated by interpolating on anarctangent, to confine a potentially infinite range (viewer to horizon) to a bounded range.
## [rubiks\_cube](https://github.com/elterminad0r/rubiks_cube)
Visual interface to my Rubik's cube model, in python-processing using 3D.
## [ship\_game](https://github.com/elterminad0r/ship_game)
One of the earlier Python-processing projects. A ship using drag coefficients, and a half-baked autopilot. Pretty options for exhaust fumes are available.
## [s\_zoom](https://github.com/elterminad0r/s_zoom)
A kind of inefficient zooming sierpinski triangle
## [wind\_fans](https://github.com/elterminad0r/wind_fans)
Simulates nutella-style turbines being blown by the mouse. Can be a little intensive.
