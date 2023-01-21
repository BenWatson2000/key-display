# key-display

## Creating Virtual Environment

### Windows

```py -3 -m venv .venv```

```.venv\scripts\activate```

### UNIX

```python3 -m venv .venv```

```source .venv/bin/activate```


## Making using a small enough font for a 16x16 grid of pixels

The aim is to have a small font to enable the display to show as many pixels as possible at any given time.

For example, the font below is an example of two fonts that use a small number of pixels.

<img src=images/small_font.png  width=90% height=90%>

The chosen cont was similar to the later, with a 4x6 pixel usage which was taken from https://www.dafont.com/bm-mini.font

## Take each letter from the font and convert them into png icons

Description

## Find the 3D array representation of each letter in an 8x8 grid (this will be used to map letters to pixels on the 16x16 grid)

Description