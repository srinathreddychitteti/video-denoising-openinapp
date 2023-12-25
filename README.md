# Video Denoising Script

This Python script utilizes the BM3D denoising algorithm and OpenCV to process multiple video files. It is designed to download input videos from Google Drive, denoise each frame, and save the denoised videos in a subdirectory named "output_videos."

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Output](#output)
5. [Metrics](#metrics)
6. [Notes](#notes)
7. [File Descriptions](#file-descriptions)


## Prerequisites

Ensure that you have the required Python libraries installed:

bash
pip install -r requirements.txt

## Installation
Clone or download the repository:

```git clone https://github.com/srinathreddychitteti/video-denoising-openinapp.git```

Navigate to the script directory:


```cd videodenoisingscript```

Run the script:


```python video_denoising.py```

## Usage
Replace the placeholder Google Drive IDs in the video_drive_ids list in video_denoising_script.py with the actual IDs of your input videos.

Run the script as described in the Installation section.

The script will download each video from Google Drive, denoise it using BM3D, and save the denoised version in the "output_videos" subdirectory.

## Output
Denoised videos are saved in the "output_videos" subdirectory with filenames like "output_video_1.mp4", "output_video_2.mp4", and so on.

## Metrics
The script calculates the Peak Signal-to-Noise Ratio (PSNR) for each frame, indicating the quality of denoising. The average PSNR over all frames is also provided.

## Notes
Make sure to replace the Google Drive IDs in the script with the actual IDs of your input videos.
If the "output_videos" subdirectory does not exist, the script will create it.
The denoising parameters, such as the BM3D sigma_psd value, can be adjusted in the script according to specific requirements.

## File Descriptions
video_denoising.py: The main Python script for denoising videos.
requirements.txt: Specifies the required Python packages and their versions.
