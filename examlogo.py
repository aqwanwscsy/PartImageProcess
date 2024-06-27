import cv2


def Image_add_logo(image_path, logo_path, position=(0, 0), size=(100, 300)):
    image1 = cv2.imread(image_path)
    image2 = cv2.imread(logo_path)
    image2 = cv2.resize(image2, size)

    rows, cols, channels = image2.shape

    # Define the region of interest (ROI) in the bottom-right corner
    start_row = position[0]
    start_col = position[1]
    end_row = start_row + rows
    end_col = start_col + cols

    roi = image1[start_row:end_row, start_col:end_col]

    # Convert logo image to grayscale and create a mask
    image2gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(image2gray, 254, 255, cv2.THRESH_BINARY)
    mask_reverse = cv2.bitwise_not(mask)

    # Extract background and logo regions using masks
    image1_background = cv2.bitwise_and(roi, roi, mask=mask)
    image2_logo = cv2.bitwise_and(image2, image2, mask=mask_reverse)

    # Combine background and logo to get the final image
    result = cv2.add(image1_background, image2_logo)

    # Replace the ROI in the original image with the result
    image1[start_row:end_row, start_col:end_col] = result

    return image1


if __name__ == "__main__":
    Image = "img/Hd.jpg"
    Logo = "img/logo.png"
    Position = (680, 855)  # Adjust the position here (row, col) in pixels
    Size = (100, 40)

    # Add logo to the image at the specified position
    image = Image_add_logo(Image, Logo, Position, Size)

    # Display the watermarked image
    cv2.imshow("Watermarked Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
