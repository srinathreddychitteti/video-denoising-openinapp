import os
import cv2
import bm3d
import numpy as np
import gdown

# Create a subdirectory for output if it doesn't exist
output_directory = 'output_videos'
os.makedirs(output_directory, exist_ok=True)

# Google Drive IDs for input videos
video_drive_ids = [
    '1AQDLDkZTFXBkZcgyV4PZz9oA8Jw5dm88',
    '1THy90K8xPgWq46z-3R5H4OE1ufT7F-5J',
    '1uzccNyXy-g3GEYeMGxxFNmaszrAuO7dJ'
   
]

def download_video_from_drive(drive_id, output_path):
    url = f'https://drive.google.com/uc?id={drive_id}'
    gdown.download(url, output_path, quiet=False)

def process_video(input_path, output_path):
    # Load the video
    cap = cv2.VideoCapture(input_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print(f"Error: Couldn't open the video {input_path}.")
        return

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width, height = int(cap.get(3)), int(cap.get(4))
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create VideoWriter object to save the output video with original settings
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Process each frame
    total_psnr = 0.0  # Variable to accumulate PSNR values

    for frame_number in range(num_frames):
        ret, frame = cap.read()

        # Check for the end of the video
        if frame is None:
            break

        # Denoise each color channel separately
        denoised_frame = np.zeros_like(frame)
        for i in range(3):  # Iterate over BGR channels
            denoised_channel = bm3d.bm3d(frame[:, :, i].astype(np.float64), sigma_psd=20)
            denoised_channel = np.clip(denoised_channel, 0, 255).astype(np.uint8)
            denoised_frame[:, :, i] = denoised_channel

        # Compute PSNR for the current frame
        psnr = cv2.PSNR(frame, denoised_frame)
        total_psnr += psnr

        # Print PSNR for each frame (optional)
        print(f"Frame {frame_number + 1}: PSNR = {psnr:.2f} dB")

        # Write the denoised frame to the output video
        out.write(denoised_frame)

    # Calculate and print the average PSNR over all frames
    average_psnr = total_psnr / num_frames
    print(f"\nAverage PSNR: {average_psnr:.2f} dB")

    # Release video capture and writer objects
    cap.release()
    out.release()

def main():
    # Process each video
    for idx, drive_id in enumerate(video_drive_ids):
        # Download video from Google Drive
        input_path = f'input_video_{idx + 1}.mp4'
        download_video_from_drive(drive_id, input_path)

        # Construct the output path
        output_path = os.path.join(output_directory, f'output_video_{idx + 1}.mp4')

        # Process the video
        process_video(input_path, output_path)

        # Remove the input video after processing 
        os.remove(input_path)

    print("Processing complete.")

if __name__ == "__main__":
    main()
