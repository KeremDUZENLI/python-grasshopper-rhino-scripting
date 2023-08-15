import imageio
from PIL import Image
import os
import moviepy.video.io.ImageSequenceClip


# Image --> Video
image_folder = 'Animation'
fps = 10

image_files = [os.path.join(image_folder, img)
               for img in os.listdir(image_folder)
               if img.endswith(".bmp")]

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
    image_files, fps=fps)
clip.write_videofile('my_video.mp4')


# Image --> Gif
image_folder = 'Animation'

image_files = [f for f in os.listdir(image_folder) if f.endswith('.bmp')]
image_files.sort()

images = []
for filename in image_files:
    image_path = os.path.join(image_folder, filename)
    img = Image.open(image_path)
    images.append(img)

output_gif_path = 'output.gif'
imageio.mimsave(output_gif_path, images, duration=5)
