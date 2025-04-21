import cv2
import os

def capture_images(output_directory):
    # Open the laptop camera (usually camera index 0)
    cap = cv2.VideoCapture(1)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        i = 0
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Display the captured frame (optional)
            cv2.imshow('Frame', frame)

            # Wait for the space key to capture an image
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '):
                i += 1
                image_path = os.path.join(output_directory, f"image_{i}.jpg")
                cv2.imwrite(image_path, frame)
                print(f"Image {i} captured and saved to {image_path}")

            # Break the loop if the Esc key is pressed
            elif key == 27:
                break

    finally:
        # Release the camera when done
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Get the desired output folder name from the user
    output_folder = input("Enter the name of the folder to save images: ")    
    current_directory = r"F:\4-2\EEE 404 Lab Robotics\Project\MyProject2\VSCodeVersion\dataset"
    output_directory = os.path.join(current_directory, output_folder)
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Call the function to capture images
    capture_images(output_directory)
