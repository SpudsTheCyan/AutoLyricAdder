from setuptools import setup

setup(name='autolyricadder',
      version='1.1',
      description='Automatically adds lyric metadata to .mp3 files',
      url='http://github.com/storborg/funniest',
      author='relyt1224',
      packages=['autolyricadder'],
      install_requires=[
          'dotenv',
          'eyed3',
          'lyricsgenius',
          'progressbar'
      ],
      zip_safe=False)