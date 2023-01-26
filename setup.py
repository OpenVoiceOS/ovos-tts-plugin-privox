#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-tts-plugin-privox = ovos_tts_plugin_privox:PrivoxTTS'
CONFIG_ENTRY_POINT = 'ovos-tts-plugin-privox.config = ovos_tts_plugin_privox:PrivoxTTSConfig'

setup(
    name='ovos-tts-plugin-privox',
    version='0.0.1',
    description='A tts plugin for ovos using privox',
    url='https://github.com/OpenVoiceOS/ovos-tts-plugin-privox',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_tts_plugin_privox'],
    install_requires=["ovos-plugin-manager>=0.0.1"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft ovos plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT,
                  'mycroft.plugin.tts.config': CONFIG_ENTRY_POINT}
)
