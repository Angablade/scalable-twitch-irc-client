from setuptools import setup, find_packages

setup(
    name='ScalableTwitchIrcClient',
    version='0.2.8',
    url='https://github.com/deemonrider/scalable-twitch-irc-client.git',
    author='DeemonRider',
    author_email='',
    description='-',
    packages=find_packages(),
    install_requires=[
        "requests==2.28.1"
    ],
)