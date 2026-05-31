# QR Maker

A simple Python script that generates QR codes from URLs and saves them as PNG files.

## Features

- Validates that the input is a valid URL (must start with `http://` or `https://`)
- Lets you choose a custom filename for the output
- Saves the QR code as a `.png` file in the current directory

## Requirements

Install dependencies with:

```bash
pip install qrcode customtkinter
```

## Usage

```bash
python main.py
```

You will be prompted to enter a URL and a filename. The QR code will be saved as `<filename>.png` in the folder where you run the script.

## Example

```
Enter your link here: https://github.com/nemanja233/qr-maker
Enter the name for the file: my-qr
→ Image saved as my-qr.png
```

## License

MIT
