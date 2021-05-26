from distutils.core import setup
import py2exe

setup(
    name="AutoLyricAdder_v1.1",
    console=[
        {
            "script":"main.py",
            'dest_base' : 'AutoLyricAdder'
        }
    ],
    options={
        "py2exe": {
            "bundle_files": True,
            "optimize": 2,
        }
    },
    zipfile=None,
)
