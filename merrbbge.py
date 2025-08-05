import cv2
import os
from glob import glob
from tqdm import tqdm  # for progress bar

# === SETTINGS ===
input_folder = "/home/sakthees-monk/Videos/asd/animationfivethousand/animationfracone"
output_video = "output_video_4k_fast.mp4"
frame_rate = 2  # 2 FPS = each frame lasts 0.5 seconds
width, height = 3840, 2160  # 4K resolution

# === FETCH FILES ===
image_files = sorted(glob(os.path.join(input_folder, "*.png")))
total_images = len(image_files)

if total_images == 0:
    raise FileNotFoundError("❌ No .png files found in the folder.")

# === VIDEO WRITER INIT ===
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

# === PROCESS IMAGES WITH TQDM PROGRESS BAR ===
for img_path in tqdm(image_files, desc="🛠️ Rendering frames", unit="frame"):
    img = cv2.imread(img_path)
    if img is None:
        continue
    img_resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
    video_writer.write(img_resized)

video_writer.release()
print(f"\n✅ DONE! 4K video saved as: {output_video}")

