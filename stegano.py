from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

# Encode message into image
@app.route('/image/encode', methods=['POST'])
def encode_html():

    image = request.files['image']
    text = request.form['text']

    # Open image and convert to RGB
    img = Image.open(image)
    img = img.convert('RGB')

    # Save initial image
    img.save('static/image_requests/uploaded.png')

    # Encode data into image
    image_encoded = encode(img, text)

    # Save encoded image
    image_encoded.save('static/image_requests/encoded.png')

    return send_file('static/image_requests/encoded.png', mimetype='image/png', as_attachment=True)

# Return last encoded image as a file
@app.route('/image/last/encode', methods=['GET'])
def last_encode_html():
    return send_file('static/image_requests/encoded.png', mimetype='image/png', as_attachment=True)

# Decode message from image
@app.route('/image/decode', methods=['POST'])
def decode_html():

    image = request.files['image']

    # Open image and convert to RGB
    img = Image.open(image)
    img = img.convert('RGB')

    # Decode data from image
    text = decode(img)

    return render_template('result_decode.html', text=text)

# Return last decoded message as plain text
@app.route('/image/last/decode', methods=['GET'])
def last_decode_html():
    text = open('static/image_requests/message.txt', 'r').read()
    return text

def encode(img, message):

    # Get the width and height of the image
    width, height = img.size
    
    # Convert the message to binary
    binary_message = ""
    for char in message:
        binary_message += '{0:08b}'.format(ord(char))

    # Add a null terminator to the end of the message
    binary_message += '{0:08b}'.format(0)


    bit_pos = 0

    for y in range(height):
        for x in range(width):
            # Get the RGB values of the current pixel
            r, g, b = img.getpixel((x, y))

            # Modify the least significant bit of each RGB value
            if bit_pos < len(binary_message):
                # Clear the least significant bit of each RGB value
                r = r & 0xFE
                # Set the bit to the value of the next bit in the message
                r = r | int(binary_message[bit_pos])
                bit_pos += 1

            if bit_pos < len(binary_message):
                # Clear the least significant bit of each RGB value
                g = g & 0xFE
                # Set the bit to the value of the next bit in the message
                g = g | int(binary_message[bit_pos])
                bit_pos += 1
            if bit_pos < len(binary_message):
                # Clear the least significant bit of each RGB value
                b = b & 0xFE
                # Set the bit to the value of the next bit in the message
                b = b | int(binary_message[bit_pos])
                bit_pos += 1

            # Update the pixel
            img.putpixel((x, y), (r, g, b))

            # If message is encoded
            if bit_pos >= len(binary_message):
                break

        if bit_pos >= len(binary_message):
            break

    # return the encoded image
    return img

def decode(img):
    # Get the width and height of the image
    width, height = img.size

    binary_message = ""

    for y in range(height):
        for x in range(width):

            # Get the RGB values
            r, g, b = img.getpixel((x, y))

            # Extract the least significant bit
            binary_message += str(r & 0x01)
            binary_message += str(g & 0x01)
            binary_message += str(b & 0x01)

    # Convert the binary message to ASCII characters
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        message += char

    # Save the message until the null terminator
    null_index = message.find('\x00')
    message = message[:null_index]

    # Save the message to a text file
    message_file = open('static/image_requests/message.txt', 'w')
    message_file.write(message)
    message_file.close()

    # Return the message
    return message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)