# OpenCV Basics

This repository demonstrates basic image processing operations using OpenCV and NumPy in Python.

## Contents

- `image_basics.py` - Reads an image, applies grayscale conversion, blur, thresholding, and edge detection, then displays and saves the combined output.
- `requirements.txt` - Core dependencies for Python projects.
- `requirements-linux.txt` - Recommended dependencies for Linux environments.
- `requirements-win.txt` - Recommended dependencies for Windows environments.
- `run.sh` - Bash script to run the example on Linux/macOS.
- `run.bat` - Batch script to run the example on Windows.
- `images/test.jpg` - Example input image used by the script.
- `outputs/processed_output.jpg` - Output file created when the script runs successfully.

## Prerequisites

- Python 3.8 or newer
- `pip` installed

## Install Dependencies

### Linux/macOS

```bash
python -m pip install -r requirements-linux.txt
```

### Windows

```powershell
python -m pip install -r requirements-win.txt
```

## Run the Script

### Linux/macOS

```bash
./run.sh
```

### Windows

```powershell
run.bat
```

## Notes

- The script expects `images/test.jpg` to exist in the `images/` directory.
- The processed result is saved to `outputs/processed_output.jpg`.
- If a display window is not available or if you prefer command-line execution, you can comment out the OpenCV `imshow` block in `image_basics.py`.
