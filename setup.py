from distutils.core import setup
import py2exe

mainfile = 'main.py'
exefile = 'AutoLyricAdder'

setup(
    name="AutoLyricAdder",
    version='0.9',
    description="Automaticly adds lyrics to mp3s",
    scripts=[mainfile],
    windows=[
        {
            "script":mainfile,
            'company_name' : "Spuds (c) 2021",
            'copyright' : "Spuds (c) 2021",
            #'uac_info': "requireAdministrator",
            'dest_base' : exefile
        }
    ],
    #"icon_resources":[(0, icon_file)]}],
    data_files = [],
    options={
        "py2exe": {
            "unbuffered": True,
            "optimize": 2,
            "bundle_files": True,
            "compressed": False,
            "includes": [
                #".env"
            ],
            "excludes" : [],
            "packages": [],
            "dll_excludes": []
        }
    },
    console = ["main.py"],
    zipfile=None,
)