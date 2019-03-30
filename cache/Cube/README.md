# Cube
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
