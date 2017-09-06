# github\_inventory
A bit of a meta-project on creating a nicer index of my github repositories. Partially motivated because I'm too greedy to do with only 6 pinned repositories. It's just about stable enough to function. It features several sub-utilities I chain together, including directory-searching and API-json reading. It files my projects under subcategories, and concatenates together readmes under a category heading.
## My Postscript Repository
### [Postscript](https://github.com/elterminad0r/Postscript)
Some of my postscript projects - some early, some less so. `zut` means pile of rubbish. There's lots to do with polysymmetry and fractals, and then some other stuff. A pretty small sample:

![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/penrose.svg)
![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/ster.svg)
![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/minkowski.svg)
![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/plusFractal.svg)
![screenshot](https://github.com/elterminad0r/Postscript/blob/master/svgs/pythagorasTree.svg)
## Miscellaneous Python projects
### [Sudoku](https://github.com/elterminad0r/sudoku)
A (brute-force) sudoku solver in Python.
### [A453](https://github.com/elterminad0r/A453)
From my GCSE computing course
### [Linked lists](https://github.com/elterminad0r/linked_list)
My Python linked list implementation. This is my expanded implementation from the HackerRank challenged. Note it's kind of half finished and untested so probably broken in all manner of fun ways. It's recursive so won't be able to handle any serious load due to Python's lack of tail call optimisation.
### [Calcudoku](https://github.com/elterminad0r/Calcudoku)
A simple brute force solver for an 8\*8 'calcudoku'.
### [Cube](https://github.com/elterminad0r/Cube)
My project expressing a Rubik's cube as a list of integers representing colours, and moves on the cube as permutations on the list. Uses some operator overloading for some pretty expressive syntax to build up the set of moves on the cube.
### [Punnet Squares](https://github.com/elterminad0r/Punnet)

Some leftover code for Punnet square generation, from a stackoverflow question. The question was deleted, so I decided to see how illegible I could make my code.
### [cookies](https://github.com/elterminad0r/cookies)
Some projects on "the cookie game" in Python. Includes an automatic opponent and some testing scripts on higher dimensions of the game.
### [Yahtzee](https://github.com/elterminad0r/yahtzee)

A work in progress - hoping to end up building a kind of nice yahtzee framework and then try to implement some different yahtzee playing algorithms (maybe monte carlo, neural network, etc)
## My Python basics repo:
### [backtobasics](https://github.com/elterminad0r/backtobasics)
Some Python basics should any of my one audience members wish to refer to them.
## java-processing projects
### [balls](https://github.com/elterminad0r/balls)
Simple, slightly buggy implementation of balls that can bounce off both each other and walls.
### [cars](https://github.com/elterminad0r/cars)
Early experimenting in OOP in java-processing
### [circles](https://github.com/elterminad0r/circles)
Neat little effect in processing - radius increases the closer to the mouse.
### [colourconway](https://github.com/elterminad0r/colourconway)
Conway's game of life, with colourisation related to recent activity. It's pretty but the code is a godawful mess I might try to wade into one day.
### [mazes](https://github.com/elterminad0r/mazes)
Maze generation algorithms in Processing, featuring solutions and slower, frame-by-frame generation.
### [pendulums](https://github.com/elterminad0r/pendulums)
A little more experimentation with Java OO in processing. Uses the simple model of pendulums to produce a slow interference effect.
### [pixel\_sorting](https://github.com/elterminad0r/pixel_sorting)
Sorting rows of pixels in an image by brightness, in Processing. Most of the work was done by Daniel Shiffman.

With this as input:

![input sunflower](https://github.com/elterminad0r/pixel_sorting/blob/master/data/sunflower.jpg)

It can produce this:

![output](https://github.com/elterminad0r/pixel_sorting/blob/master/sorted.jpg)

While it's running, it looks like this:

![screenshot](https://github.com/elterminad0r/pixel_sorting/blob/master/intermediary.png)
### [pythanimated](https://github.com/elterminad0r/pythanimated)
Very simple code to eternally animate the angle of a Pythagoras Tree.
### [rainbow\_lines](https://github.com/elterminad0r/rainbow_lines)
A simpler project, doing some slightly diagonal rainbow shading on a canvas.

Here is a screenshot:

![Screenshot](https://github.com/elterminad0r/rainbow_lines/blob/master/screenshot.png)
### [regen\_soup](https://github.com/elterminad0r/regen_soup)
Simple OO to display a kind of weird soup-like substance with some mildly hallucinogenic rainbows. It doesn't use drawing primitives to draw the rainbows as Processing doesn't support any kind of gradient, so it actually directly modifies the pixel array.
### [shading](https://github.com/elterminad0r/shading)

Processing fuzzy rainbow
### [snowflakes](https://github.com/elterminad0r/snowflakes)
From a Christmas CS lesson once upon a time - snowflakes simulated by ascii characters. It looks like this:

![screenshot](https://github.com/elterminad0r/snowflakes/blob/master/screenshot.png)
### [square\_filling\_circle](https://github.com/elterminad0r/square_filling_circle)
Squares that fill up the area of a circle, inspired by the classic pi paradox (as the total area of the squares approaches the area of the circle, then surely the perimeter does so too, which would lead to pi=4). It uses a real beauty of an equation worked through by hand to find the intersection of a line with gradient 1 and a circle arc - 

    intercept = 0.5 * (sqrt(-a * a + 2 * a * (b + c - d) - b * b - 2 * b * c + 2 * b * d - c * c + 2 * c * d - d * d + 2 * r * r) + a + b + c - d) - c;

Here is a screenshot of it in action:

![screenshot](https://github.com/elterminad0r/square_filling_circle/blob/master/screenshot.png)
### [UI\_demo](https://github.com/elterminad0r/UI_demo)

A simpler implementation/demonstration of my UI elements in Processing, later to be used more in `moire_draggable`.
### [turtles](https://github.com/elterminad0r/turtles)
Custom turtle implementation in Processing, used to have multiple turtles follow the same instructions (from keyboard) for symmetric kinda pretty rainbow patterns. Here is what it looks like:

![screenshot](https://github.com/elterminad0r/turtles/blob/master/screenshot.png)
### [s\_zoom](https://github.com/elterminad0r/s_zoom)
A kind of inefficient zooming sierpinski triangle
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
A breadth-first Sierpinski triangle, using generators. It looks like this:

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
