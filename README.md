# Mutt Theme Generator

### Synopsis

Generates Mutt/Neomutt themes from .Xresources files.

Most (all?) theme generating websites (such as [terminal.sexy] and [4bit]) do
not support exporting to a .muttrc color scheme (after all, this wouldn't even
really make sense).  To make matters worse, muttrc colors must be defined as
xterm-256 colors, which are palettized, as opposed to 24-bit true colors.

This repo contains a template muttrc (which has my name in it; you might want
to change that) based on [~ben's ncurses linked Mutt adapted solarized.muttrc]
which is in turn based on [altercation's solarized.muttrc]. This code is the
definition of a hack job, but it works for my purposes so maybe it'll work for
yours as well.

There are three main components to this repo: the .muttrc template file, a
short Awk script that can be used to generate a .muttrc file from the template,
and a Python script that can be used to convert a .Xresources file with color
information into a format ready for the Awk script.  These tools can all be
used independetly, or, alternatively, there is a shell script that glues them
together into a single operation. There is also a directory filled with
.Xresources files, most of which were exported from [terminal.sexy]. I ended up
settling on Lumifoo for the time being.

Okay, time to do some actual work.

### Usage

Or I guess I could slap a few usage examples here.

Generating at heme from manually entered data.

```
$ cat ./sample.colors
BACKGROUND = color234
BLACK = color239
BRBLACK = color243
RED = color132
BRRED = color181
GREEN = color71
BRGREEN = color151
YELLOW = color137
BRYELLOW = color187
BLUE = color67
BRBLUE = color152
MAGENTA = color133
BRMAGENTA = color182
CYAN = color72
BRCYAN = color151
WHITE = color246
BRWHITE = color252
~/src/mcg$ awk -f ./generate-muttrc.awk ./sample.colors
./template.muttrc > /tmp/sample.muttrc
~/src/mcg$ cat /tmp/sample.muttrc
# Generated .muttrc theme.
# Based on https://git.sr.ht/~ben/cfg/tree/2b90c65225a3d7154fca2e9a723c2f5fe5ec06b8/mutt/solarized.muttrc
# Based on https://github.com/altercation/mutt-colors-solarized/

# The original by @altercation only works if mutt is linked against slang.
# This color scheme has been modified to work with ncurses.

# Highlight my name and other personally relevant strings
color body color137 color234 "(shawn|chapla|shawn m\. chapla)"

# for background in 16 color terminal, valid background colors include:
# base03, bg, black, any of the non brights

# Basic colors
color normal color152 color234
color error color132 color234
color tilde color246 color234
color message color72 color234
color markers color132 color234

...
```

Generating a muttrc file directly from one of the themes in the themes
directory.

```
moth@chrysalis:~/src/mcg$ ./xres-to-muttrc.sh
./themes/solarized3.xresources
# Generated .muttrc theme.
# Based on https://git.sr.ht/~ben/cfg/tree/2b90c65225a3d7154fca2e9a723c2f5fe5ec06b8/mutt/solarized.muttrc
# Based on https://github.com/altercation/mutt-colors-solarized/

# The original by @altercation only works if mutt is linked against slang.
# This color scheme has been modified to work with ncurses.

# Highlight my name and other personally relevant strings
color body color136 color234 "(shawn|chapla|shawn m\. chapla)"

# for background in 16 color terminal, valid background colors include:
# base03, bg, black, any of the non brights

# Basic colors
color normal color246 color234
color error color166 color234
color tilde color254 color234
color message color36 color234
color markers color166 color234
color attachment default color234
color search color62 color234

...
```

### License

Copyright 2020 Shawn M. Chapla

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[terminal.sexy]: https://terminal.sexy/
[4bit]: http://ciembor.github.io/4bit/
[~ben's ncurses linked Mutt adapted solarized.muttrc]: https://git.sr.ht/~ben/cfg/tree/2b90c65225a3d7154fca2e9a723c2f5fe5ec06b8/mutt/solarized.muttrc
[altercation's solarized.muttrc]: https://github.com/altercation/mutt-colors-solarized/
