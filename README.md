# Keyboard layout benchmark

Ever wondered which keyboard layout is the master layout for programming or whatever other tasks? 😄
This repository serves to answer that question by analyzing distance travelled by fingers while writing input text.

## Configuration

Layouts can be easily configured by typing out letters top to bottom, left to right of four basic keyboard rows and by configuring mapping of fingers for each key, i.e. `A` maps to `left pinky finger (5)`.
Analyzed text is located in `example.py`

## Running

Comparison can be performed by running `python compare.py`, which goes over all defined layouts and prints distances travelled.

## Example output

```
layout: SK_QWERTZ, left:    2582.20, right:    2390.15, sum:    4972.34
layout: SK_QWERTY, left:    2458.15, right:    2390.15, sum:    4848.30
layout: EN_QWERTZ, left:    2455.66, right:    2795.04, sum:    5250.70
layout: EN_QWERTY, left:    2331.16, right:    2795.04, sum:    5126.20
```

Please note that there are no units specified, as basis for calculation, pythagorean distance is used between row and column numbers, i.e. if Q is 2nd row, 1st letter and S is 3rd row, 2nd letter, then distance is `sqrt((3 - 2)**2 + (2 - 1)**2)` which essentially equals `~1.41`