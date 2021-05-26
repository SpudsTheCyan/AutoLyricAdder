# imports
import os
from dotenv import load_dotenv
import eyed3
import lyricsgenius
import sys
import logging
import progressbar

# sets up logging
logging.basicConfig(
    level=logging.INFO,
    filename="log.txt",
    filemode='w',
    format='%(asctime)s - %(message)s'
)

# sets the dragged file to the music directory
music_path = input(
    f"Drag and drop the folder containing you music below, or type the "
    "directory of folder of music to add lyrics to and then press enter...\n"
)
os.chdir(music_path)

# gets genius api token, then defines and configures genius obj
load_dotenv()
genius = lyricsgenius.Genius("GENIUS_ACCESS_TOKEN")
genius.verbose = False
genius.skip_non_songs = False

# creates a list of all .mp3 files in directory
music_dir = os.listdir(music_path)
for file in music_dir:
    if not file.endswith('.mp3'):
        music_dir.remove(file)

# searched for lyrics and adds them to mp3 metadata
with progressbar.ProgressBar(max_value=len(music_dir), redirect_stdout=True) as bar:
    bar.update(0)
    for song_file in music_dir:
        # if song_file.endswith('.mp3'):
        song = eyed3.load(song_file)
        print (f"Proccessing {song.tag.title} by {song.tag.artist}...")
        try:
            logging.info(f"Searching for lyrics to {song.tag.title} by {song.tag.artist}...")
            song_genius = genius.search_song(title=song.tag.title, artist=song.tag.artist)
            if song_genius is None:
                raise Exception("Song cannot be found or has no lyrics!")
        except:
            logging.info(f"{song.tag.title} by {song.tag.artist} cannot be found or has no lyrics! Skipping...\n")
        else:
            logging.info(f"Found lyrics for {song.tag.title} by {song.tag.artist}! Adding...")
            song.tag.lyrics.set(song_genius.lyrics)
            song.tag.save()
            logging.info(f"Added lyrics to {song.tag.title} by {song.tag.artist}!\n")
        finally:
            # progresses bar and prints it
            bar.update(music_dir.index(song_file))
            print (f"Finished proccessing {song.tag.title} by {song.tag.artist}!\n")
    else:
        logging.info(f"{song_file} is not an .mp3. Skipping...\n")
print (f"\nFinished proccessing all files!")
logging.info(f"All songs proccessed")

# closes the program once the user presses enter
exit_program = input("Press enter to exit...")
