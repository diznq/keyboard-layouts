# Keyboard layout benchmark

Ever wondered which keyboard layout is the master layout for programming or whatever other tasks? 😄
This repository serves to answer that question by analyzing distance travelled by fingers while writing input text.

## Configuration

Layouts can be easily configured by typing out letters top to bottom, left to right of four basic keyboard rows and by configuring mapping of fingers for each key, i.e. `A` maps to `left pinky finger (5)`.
Analyzed text is located in `example.py`

## Running

Comparison can be performed by running `python compare.py`, which goes over all defined layouts and prints distances travelled.
Additionally `IN` env var can be specified to change input file, i. e. `IN=data/sample.txt python compare.py`

## Example output

```
layout: SK_QWERTZ, left:  128373.57, right:  149036.03, sum:  277409.59
layout: SK_QWERTY, left:  119815.58, right:  149036.03, sum:  268851.61
layout: EN_QWERTZ, left:  128059.70, right:  141763.46, sum:  269823.16
layout: EN_QWERTY, left:  119410.43, right:  141763.46, sum:  261173.89
layout: EN_DVORAK, left:  118450.22, right:  129759.01, sum:  248209.23
```

Please note that there are no units specified, as basis for calculation, pythagorean distance is used between row and column numbers, i.e. if Q is 2nd row, 1st letter and S is 3rd row, 2nd letter, then distance is `sqrt((3 - 2)**2 + (2 - 1)**2)` which essentially equals `~1.41`