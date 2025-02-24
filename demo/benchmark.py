#               Copyright © DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it isn't allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macrame, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).


import sys
from time import time


FACTOR = 5.0

def make_animation():
    """
    Return a new function that prints the next frame
    of an animation after it is called interval times
    """
    interval = 100000
    frames = ["Ooo", "OOo", "oOO", "ooO", ".oo", "..o", "o..", "oo."]
    pointer = 0
    count = len(frames)
    def frame(turn):
        if turn % interval != 0:
            return
        nonlocal pointer
        pointer += 1
        if pointer == count:
            pointer = 0
        print(f"\rMeasuring performance {frames[pointer]} ", end="")
    return frame


if len(sys.argv) < 2:
    print("Usage: demo/benchmark.py DATA_DIR", file=sys.stderr)
    sys.exit(1)


lines = 0
chars = 0
animate = make_animation()
before = time()

f = open(f"{sys.argv[1]}/area-titles.csv")
for line in f:
    line.split(",", maxsplit=1)
    lines += 1
    chars += len(line)
    animate(lines)
f.close()

f = open(f"{sys.argv[1]}/2023.annual.singlefile.csv")
for line in f:
    line.split(",")
    lines += 1
    chars += len(line)
    animate(lines)
f.close()

duration = time() - before
print("\rDone!                    ")
print(f"It took {duration:.2f}s to process {lines:,} lines of data ({int(chars/1024/1024)} MB)")
print(f"On this computer big_data.py should finish in under {duration * FACTOR:.2f}s")
