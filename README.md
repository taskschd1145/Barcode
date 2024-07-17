# Barcode
[中文](https://github.com/taskschd1145/Barcode/blob/main/README_cn.md)

## Overview

This project is a tool written in Python designed to help users quickly generate barcode images in bulk. It utilizes the `python-barcode` library to generate barcodes and the `Pillow` library for image output processing.

## Installation and Setup

Ensure you have Python installed. If not, visit [python.org](https://www.python.org/downloads/) to download and install the latest version.

Run the following command in the terminal to install the necessary Python packages:

```bash
pip install python-barcode Pillow
```

## Usage

### Step 1: Get the Source Code

Download the source code from the Releases section of the GitHub repository.

### Step 2: Edit the Barcode List

Open the `main.txt` file and replace its contents with the barcode data you need to generate, with each data entry on a new line.

### Step 3: Run the Main Script

In the project directory, run the `main.py` script via the terminal:

```bash
python main.py
```

This will generate barcode images based on the data in `main.txt`.

### Step 4: View the Generated Images

The generated barcode images will be saved in the `images` folder. You can find and use the images from there.

### Step 5: Cleanup

To avoid duplicates, it is recommended to delete all images in the `images` folder before running the program again.

## Notes

By default, the barcode images are sized at 600x400 pixels. You can adjust this setting in the `main.py` file.
### Note:This project uses the Nerd Font for displaying text below the barcodes.

