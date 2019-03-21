#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sound_recorder
# from konlpy.tag import Okt
import json
from socket import *
from select import *

import requests


def run_quickstart():
    # [START speech_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START migration_import]
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    # [END migration_import]

    # okt = Okt()

    # Instantiates a client
    # [START migration_client]
    client = speech.SpeechClient()
    # [END migration_client]

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        '.',
        'file.wav')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ko-KR')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    API_HOST = 'http://localhost:8080'

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        msg = result.alternatives[0].transcript
        res = requests.post(
            API_HOST, {'word': msg})

    # PORT='8080'

    # while(True):
    #     if(result.alternatives[0].transcript):
    #         res = requests.post(
    #             API_HOST, {'word': result.alternatives[0].transcript})
    #         break

    # if(res):
    #     print('Success')
    # else:
    #     print('fail')


if __name__ == '__main__':
    sound_recorder.record_sound()
    run_quickstart()
