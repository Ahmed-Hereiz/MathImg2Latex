# Project Title: Math Equation Drawer

## Overview
This project provides a graphical user interface (GUI) for drawing mathematical equations and saving them as images. The main functionality is implemented in two files: `draw.py` and `main.py`.

## Files

### draw.py
This file contains the GUI implementation using the Tkinter library. It allows users to draw on a canvas and save their drawings as PNG images. The images are enhanced for better contrast before saving.

#### Key Functions:
- `gui_draw()`: Initializes the GUI, sets up the canvas for drawing, and handles the saving of images.
- `draw(event)`: Draws an oval on the canvas where the mouse is clicked and dragged.
- `enhance_image(image_path)`: Enhances the contrast of the saved image.
- `save_image()`: Saves the drawn image and applies enhancement.

### main.py
This file serves as the entry point for the application. It loads configuration settings, invokes the drawing GUI, and processes the saved image using a multimodal agent.

#### Key Components:
- Loads configuration from a JSON file.
- Calls the `gui_draw()` function to open the drawing interface.
- Opens the saved image and prepares it for further processing with a multimodal agent.
