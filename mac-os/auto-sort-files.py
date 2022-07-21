import os
from shutil import move
import pathlib

downloads_dir = pathlib.Path("~").expanduser() / "Downloads"
user = os.getenv('USER')

root_dir = downloads_dir / ""
image_dir = downloads_dir / "Downloaded-images"
video_dir = downloads_dir / "Downloaded-videos"
docx_dir = downloads_dir / "Downloaded-docx"
excl_dir = downloads_dir / "Downloaded-excl"
other_dir = downloads_dir / "Other"

# create folders
downloaded_images = '/Users/{}/Downloads/Downloaded-images/'.format(user)
downloaded_videos = '/Users/{}/Downlaods/Downloaded-videos/'.format(user)
downloaded_docx = '/Users/{}/Downlaods/Downloaded-docx/'.format(user)
downloaded_excl = '/Users/{}/Downlaods/Downloaded-excl/'.format(user)
other = '/Users/{}/Downlaods/Other'

for f in (
    image_dir,
    video_dir,
    docx_dir,
    excl_dir,
    other_dir,
):
    f.mkdir(parents=True, exist_ok=True)

# file types

doc_types = ('.doc', '.docx', '.txt')
excl_types = ('.excl')
img_types = ('.m1v', '.mpeg', '.mov', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4', '.HEIF' '.HEIC')
video_types = ('.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm')
wip = ('WIP')
te = ('TE')

def get_non_hidden_files_except_current_file(root_dir):
    return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]

def move_files(files):

    for file in files:
        if file.endswith(doc_types):
            move(file, '{}/{}'.format(docx_dir, file))
        elif file.endswith(excl_types):
            move(file, '{}/{}'.format(excl_dir, file))
        elif file.endswith(img_types):
            move(file, '{}/{}'.format(image_dir, file))
        elif file.endswith(video_types):
            move(file, '{}/{}'.format(video_dir, file))
        else:
            move(file, '{}/{}'.format(other_dir, file))

if __name__ == "__main__":
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files)


