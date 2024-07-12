"""
VC1 - Voice Command 1
Copyright (C) 2024  Olanorw aka Olav SHarma

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from elevenlabs import save
from elevenlabs.client import ElevenLabs
from rich import print
import time
import requests
import re

# Define the ElevenLabsHandler class
class ElevenLabsHandler:
    def __init__(self, api_key):
        self.client = ElevenLabs(
            api_key=api_key # Initialize the ElevenLabs client with the provided API key
        )

    def generate(self, text, voice_id):
        print(f"[yellow]Making a request to the ElevenLabs API, please wait...[/yellow]")
        # Generate audio using the ElevenLabs client
        audio = self.client.generate(
            text=text,
            voice=voice_id,
            model="eleven_turbo_v2"
        )
        
        # Save the generated audio to a file
        timestamp = str(int(time.time()))
        file_name = timestamp + '.mp3'
        save(audio, file_name)
        
        return file_name
    
    def check_voice_status(voice_id, api_key):
        url = "https://api.elevenlabs.io/v1/voices/" + voice_id + "/"
        headers = {"xi-api-key": api_key}

        response = requests.request("GET", url, headers=headers)
        json_string = response.text
        match = re.search(r'"status":"(.*?)"', json_string)
        
        if match:
            status = match.group(1)
            if status == "voice_not_found":
                return "invalid"
            elif status == "invalid_uid":
                return "invalid"
            else:
                return "valid"
        else:
            print(f"Status not found")

    def check_api_key(api_key):
        url = "https://api.elevenlabs.io/v1/voices/"
        headers = {"xi-api-key": api_key}
        response = requests.request("GET", url, headers=headers)
        
        if response.text == '{"detail":{"status":"invalid_api_key","message":"Invalid API key"}}':
            return "invalid"
        else:
            return "valid"
        
# Tests
if __name__ == "__main__":
    el = ElevenLabsHandler("API_KEY_HERE")
    # Check the validity of an API key
    el.generate("Hello, world!", "VOICE_ID_HERE")
