# Extract-PAN-details
Given any PAN card image, the code extracts name, father's name, date of birth and PAN card number from the image.

# Modus Operandi
1)I used pillow module to read the image.
2)The preprocessing involved converting the image to grayscale. Binarizing the image and removing noise was not needed in this case, but it would be great to do so.
3)I then used pytesseract module to extract the information.

