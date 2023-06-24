# Steganography

## Overview

Steganography is the practice of hiding information within another medium so that the existence of the information is concealed. By modifying the least significant bit of each pixel in an image, we can encode text in the image. The image will look the same to the human eye, but the text will be encoded in the image. The project focuses on implementing a web application that encodes text in images and decodes text from images. The application is written in Python using the Flask framework.
    
The application has 4 routes:
1. `/image/encode`: For a POST request, this route accepts an image and a text. The text will be encoded in the image and the resulting image will be displayed in the browser and can be downloaded.
2. `/image/decode`: For a POST request, this route accepts an image. The text encoded in the image will be displayed in the browser.
3. `/image/last/encode`: For a GET request, this route returns the last encoded image as a downloadable file.
4. `/image/last/decode`: For a GET request, this route returns the encoded text as plain text.

## Table of contents

- [Overview](#overview)
- [Table of contents](#table-of-contents)
- [Requirements](#requirements)
- [Usage](#usage)
    - [Implementation details](#implementation-details)


## Requirements

    - Python 3.8
    - Flask
    - PIL

## Usage
    
    To run the application, run the following commands in the root directory of the project:
        - pip install -r requirements.txt
        - python stegano.py

    Or you can run the application in a docker container:
        - docker build -t stegano .
        - docker run -p 8080:80 stegano 
            `-> it should run on http://localhost:8080

### Implementation details

*  Used flask to create a web server that returns the images provided by the user as downloadable files and to display the decoded text.
*  PIL library was used to represent each pixel as a RGB triplet.
*  To encode the text in the image I used the LSB (Least Significant Bit) method which consists in replacing the last bit of each RGB value of the pixel with a bit from the text to be encoded. I did a logical and with 0xFE which puts 0 on the last bit and I did a logical or with the bit from the text to be encoded. The original image, the encoded one and the encoded text are saved in `./static/image_requests/`.

*  Because I encountered problems when decoding the text (the returned text had other characters besides the encoded ones) I decided to add a '\0' at the end of the text before encoding, and when decoding to return the text until the first '\0' encountered.

*  For the design of the site I used css. I decided to use a minimalist design, so as not to distract from the functionality of the site. Also, I added short jokes on each page to make the site more enjoyable.

```python
# Each pixel is a (R, G, B) tuple
pixel = (R, G, B)
# Each character is represented by 8 bits
bit_message = [bit_1, bit_2, ..., bit_8]
# Encode the text in the image
# (color & 0xFE) | bit_message[i]
encoded_pixel = (R, G, B)
```

> **Note:** The application works on lossless compression formats ( e.g. PNG, BMP, TIFF). In contrast, lossy compression formats (e.g. JPEG) may alter the image and corrupt the encoded text.
>
> **Note:** I do not own or have any rights over the images used in this project (present in `./static/images/`). They were taken from [here](https://www.pxfuel.com/en/desktop-wallpaper-zbmaw).
