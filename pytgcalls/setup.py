import re

from setuptools import setup, find_packages

packages = find_packages()

with open('pytgcalls/__init__.py', encoding='utf-8') as f:
    version = re.findall(r"__version__ = '(.+)'", f.read())[0]

with open('../README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='pytgcalls',
    version=version,
    author='Il`ya Semyonov',
    author_email='ilya@marshal.dev',
    license='LGPLv3',
    url='https://github.com/MarshalX/tgcalls',
    keywords='python, library, telegram, async, asynchronous, webrtc, lib, voice-chat, '
             'voip, group-chat, video-call, calls, pyrogram, pytgcalls, tgcalls ',
    description='Library connecting python binding for tgcalls and pyrogram',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=packages,
    install_requires=['tgcalls == 0.0.3', 'pyrogram >= 1.1.13'],
    python_requires="~=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Capture',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Communications',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    project_urls={
        'Author': 'https://github.com/MarshalX',
        'Telegram Channel': 'https://t.me/tgcallslib',
        'Telegram Chat': 'https://t.me/tgcallschat',
    }
)
