# MultiPaste

MultiPaste is a simple yet powerful tool designed to automate the process of entering a product's SKU number and its quantity into systems that do not support batch input directly. The application was developed to address the need for efficient data entry in distribution warehouses, where time and accuracy are critical. With MultiPaste, users can input a product SKU number (via barcode scanner or manual entry) along with the desired quantity, and then use a macro key to paste the SKU number the specified number of times. This functionality fills a gap in existing software, streamlining operations and reducing manual entry errors.

## Features

SKU Entry: Input a product SKU number for repeated pasting.
Quantity Specification: Define how many times the SKU number should be pasted.
Lock Inputs: Option to lock SKU and quantity inputs to prevent accidental changes.
Macro Key Activation: Use a predefined keybind (F8) to trigger the pasting process.
Error Handling: Displays error messages for invalid inputs.

## Requirements

To run MultiPaste, you'll need:

- Python 3.6 or later
- Tkinter (usually comes with Python)
- `pynput` for keyboard control
- `pyperclip` for clipboard management
- `threading` for managing concurrent operations

## Installation

Before running MultiPaste, ensure you have the required libraries installed. You can install them using pip:

```bash
Copy code
pip install pynput pyperclip
```

## Running the Application

To start MultiPaste, navigate to the directory containing the script and run:
    
```bash
Copy code
python multipaste.py
```
Ensure the script's name matches the command.

## Usage

1. Enter SKU: Input the SKU number in the designated field.
2. Enter Quantity: Specify the quantity in the next field.
3. Lock Inputs (optional): Click the "Lock" checkboxes to prevent accidental modification.
4. Activate Pasting: Press the F8 key to start pasting the SKU number the specified number of times.

## Packaging as a Standalone Windows Application

MultiPaste can be packaged into a single executable file for Windows using PyInstaller. This makes distribution and use in a warehouse setting more convenient.

1. Install PyInstaller:
    
```bash
Copy code
pip install pyinstaller
```
2. Package the Application:
Navigate to the application directory and run:

```bash
Copy code
pyinstaller --onefile --windowed multipaste.py
```
This command tells PyInstaller to package the script into a single executable file with a windowed interface (no console). The resulting .exe file can be found in the dist directory.

## Notes

- MultiPaste was specifically designed for use in distribution warehouses but can be adapted for other purposes.
- The application runs as a standalone Windows application for ease of use in professional environments.
