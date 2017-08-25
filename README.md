# Word blocks

This software is for creating squares of letters that form words in
each direction.  It uses git submodules, so you will need to clone it
with

    git clone --recursive https://github.com/droundy/word-blocks

which will grab the necessary genalg package.

To use the package, you will want to run

    pypy four.py

which will generate some optimum 4x4 word blocks, suitable for use on
a 3D blocks puzzle.

If you just want to see my plans for puzzles, you could examine
[poems.svg](blob/master/poems.svg), which gives a few nice poems.

![poems.svg](https://github.com/droundy/word-blocks/raw/master/poems.svg)
