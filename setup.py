from setuptools import setup, find_packages

setup(
    name='TwitchClient',
    version='0.0.1',
    url='https://github.com/deemonrider/scalable-twitch-irc-client.git',
    author='DeemonRider',
    author_email='',
    description='-',
    packages=find_packages(),
    install_requires=[
        "requests==2.27.1"
    ],
)