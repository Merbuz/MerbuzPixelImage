# MerbuzPixelImage
Sub-repository of the MerbuzPixel project. Library on Python (not Micropython) for creating files for draw images.

## How it work?

Just download and import this library. After that, call `merbuzPixelCreate` function and load filename of picture. **important note: width and height MUSE BE THE SAME**

```python
from merbuzpixelimage import *

merbuzPixelCreate(path_to_image='cherry.jpg', width=16, height=16)
```

You will receive a file in the directory and its name
