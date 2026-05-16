import cv2
import numpy as np


# ---------------------------------------------------
# Read Image
# ---------------------------------------------------

img = cv2.imread("images/test.jpg")

# Check if image loaded successfully
if img is None:
    print("Image not found")
    exit()

# Resize image for consistent display
img = cv2.resize(img, (500, 400))


# ---------------------------------------------------
# Grayscale Conversion
# ---------------------------------------------------

# Convert BGR image to grayscale
grey_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert grayscale back to BGR
# (required for stacking images together)
grey = cv2.cvtColor(grey_1, cv2.COLOR_GRAY2BGR)


# ---------------------------------------------------
# Gaussian Blur
# ---------------------------------------------------

# Reduce noise using Gaussian Blur
blur_1 = cv2.GaussianBlur(grey_1, (5, 5), 0)

# Convert back to BGR for stacking
blur = cv2.cvtColor(blur_1, cv2.COLOR_GRAY2BGR)


# ---------------------------------------------------
# Thresholding
# ---------------------------------------------------

# Convert grayscale image into black & white
_, thresh_1 = cv2.threshold(
    grey_1,
    127,
    255,
    cv2.THRESH_BINARY
)

# Convert back to BGR for stacking
thresh = cv2.cvtColor(
    thresh_1,
    cv2.COLOR_GRAY2BGR
)


# ---------------------------------------------------
# Edge Detection
# ---------------------------------------------------

# Edge detection after blur
edge_1 = cv2.Canny(blur_1, 100, 200)

# Convert back to BGR
edge = cv2.cvtColor(
    edge_1,
    cv2.COLOR_GRAY2BGR
)

# Edge detection directly on grayscale image
edge_2 = cv2.Canny(grey_1, 100, 200)

# Convert back to BGR
edge2 = cv2.cvtColor(
    edge_2,
    cv2.COLOR_GRAY2BGR
)


# ---------------------------------------------------
# Add Titles on Images
# ---------------------------------------------------

# Bright green text color
text_color = (0, 255, 0)

cv2.putText(
    img,
    "Original",
    (10, 35),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    text_color,
    2
)

cv2.putText(
    grey,
    "Gray",
    (10, 35),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    text_color,
    2
)

cv2.putText(
    blur,
    "Blur",
    (10, 35),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    text_color,
    2
)

cv2.putText(
    thresh,
    "Threshold",
    (10, 35),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    text_color,
    2
)

cv2.putText(
    edge,
    "Edge after Blur",
    (10, 35),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    text_color,
    2
)

cv2.putText(
    edge2,
    "Edge with Gray",
    (10, 35),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    text_color,
    2
)


# ---------------------------------------------------
# Stack Images
# ---------------------------------------------------

# Create top row
top = np.hstack((img, grey, blur))

# Create bottom row
bottom = np.hstack((thresh, edge, edge2))

# Combine top and bottom rows
combined = np.vstack((top, bottom))


# ---------------------------------------------------
# Save Output Image
# ---------------------------------------------------

cv2.imwrite(
    "outputs/processed_output.jpg",
    combined
)


# ---------------------------------------------------
# Display Final Output
# ---------------------------------------------------

cv2.imshow(
    "Phases of Image Processing",
    combined
)

cv2.waitKey(0)
cv2.destroyAllWindows()