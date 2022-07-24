import os
from shutil import move
import pathlib
import daemon
import time

user = os.getenv('USER')

downloads_dir = pathlib.Path("~").expanduser() / "Downloads"
desktop_dir = pathlib.Path("~").expanduser() / "Desktop"

root_dir = downloads_dir / ""
image_dir = downloads_dir / "Downloaded-images"
video_dir = downloads_dir / "Downloaded-videos"
docx_dir = downloads_dir / "Downloaded-docx"
excl_dir = downloads_dir / "Downloaded-excl"
other_dir = downloads_dir / "Other"
to_edit_dir = desktop_dir / "To-edit"
edited_img_dir = desktop_dir / "Edited-Images"

# create folders
downloaded_images = '/Users/{}/Downloads/Downloaded-images/'.format(user)
downloaded_videos = '/Users/{}/Downloads/Downloaded-videos/'.format(user)
downloaded_docx = '/Users/{}/Downloads/Downloaded-docx/'.format(user)
downloaded_excl = '/Users/{}/Downloads/Downloaded-excl/'.format(user)
other = '/Users/{}/Downloads/Other'
edited_img = '/Users/{}/Desktop/Edited-Images/'.format(user)
to_edit = '/Users/{}/Desktop/Images-to-edit/'. format(user)
work_in_progress = '/Users/{}/Desktop/Work-in-progress'.format(user)

for f in (
    image_dir,
    video_dir,
    docx_dir,
    excl_dir,
    other_dir,
    to_edit_dir,
    edited_img_dir,
    work_in_progress,
):
    f.mkdir(parents=True, exist_ok=True)

# file types

doc_types = '.doc', '.docx', '.txt'
excl_types = '.excl'
img_types = '.m1v', '.mpeg', '.mov', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4', '.HEIF' '.HEIC'
video_types = '.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm'
wip = 'WIP' img_types
te = 'TE'

def get_non_hidden_files_except_current_file(root_dir):
    return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(_file_)]

def move_files(files):
    for file in files:
        if file.endswith(te, img_types):
            move(file, '{}/{}'.format(to_edit_dir, filr))
        if file.endswith(wip, img_types):
            move()
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

with daemon.DaemonContext():
    while True:
        if _name_ == "_main_":
            files = get_non_hidden_files_except_current_file(root_dir)
            move_files(files)
            time.sleep(1)