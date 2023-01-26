import requests
from ovos_plugin_manager.templates.tts import TTS


class PrivoxTTS(TTS):
    LEGACY_URL = "http://api.privox.io/tts"
    URL = "https://secure.privox.io/tts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.voice = self._get_voice()
        self.key = self.config.get("key")

    def _get_voice(self, voice=None):
        voice = voice or self.voice or self.config.get("voice")
        if not voice or voice == "default" or voice == "male":
            voice = "voice1"
        elif voice == "female":
            voice = "voice2"
        return voice

    def get_tts(self, sentence, wav_file, lang=None, voice=None):
        lang = lang or self.lang
        voice = self._get_voice(voice)
        data = f'key={self.key}&language={lang.split("-")[0]}&voice={voice}&text={sentence}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = requests.post(self.LEGACY_URL, data=data, headers=headers)
        with open(wav_file, "wb") as f:
            f.write(data.content)
        return wav_file, None

    def available_languages(self) -> set:
        # TODO - ?
        return {"en-us"}


PrivoxTTSConfig = {}

if __name__ == "__main__":
    t = PrivoxTTS()
    utt = "Privox is a free, anonymous, privacy respecting open source, user supported voice network. It provides speech to text and text to speech services suitable for use in consumer grade applications"
    t.get_tts(utt, "voice1.wav", voice="voice1")
    t.get_tts(utt, "voice2.wav", voice="voice2")
