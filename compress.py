import moviepy.editor as mp

def compress_video(input_file, output_file, target_size):
    video = mp.VideoFileClip(input_file)
    video.write_videofile(output_file, codec="libx264", bitrate=f"{target_size}k")

input_file = "C:\Users\mcrom\OneDrive\Desktop\IMG_1876.MOV"
output_file = "output.mov"
target_size = 20000  # 20MB in kilobits

compress_video(input_file, output_file, target_size)