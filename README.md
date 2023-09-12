# MerbuzPixelImage
Sub-repository of the MerbuzPixel project. Library on Python (not Micropython) for creating files for draw images.

## How it work?

Just download and import this library. After that, call `merbuzPixelCreate` function and load filename of picture.

```python
from merbuzpixelimage import *

merbuzPixelCreate(path_to_image='cherry.jpg')
```

You will receive a file in the directory and its name
