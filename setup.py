#!/usr/bin/python3
try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages, Extension

data_files=[
    ('/etc/autobgch/scripts/',['autobgch/scripts/feh', 'autobgch/scripts/mate',
        'autobgch/scripts/gnome3', 'autobgch/scripts/unity']),
    ('/etc/autobgch/autostart/', ['autobgch/autostart/bgchd-gnome.desktop',
        'autobgch/autostart/bgchd-mate.desktop'])
]

setup(
    name='auto background changer',
    version='0.3.1',
    description='A simple wallpaper changer',
    long_description="""A simple wallpaper changer supporting multiple backends
        for Linux or other X11 system""",
    url='https://github.com/AlvinJian/auto_background_changer',
    author='AlvinJian',
    author_email='alvinchien0624@gmail.com',
    keywords='wallpaper changer',
    packages=find_packages(),
    package_data = {'autobgch':['scripts/*']},
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'bgchd=autobgch.bgchd:run',
            'bgctl=autobgch.bgctl:run'
        ],
    },
)
