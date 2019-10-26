from google.cloud import texttospeech_v1beta1
from google.oauth2 import service_account


key = "AIzaSyBKc_mIOVm4RPqtyU2z19VwMMw1EuJM0Iw"

# TODO(developer): Set key_path to the path to the service account key
#                  file.
# key_path = "path/to/service_account.json"
key_path = "JING-704cd29711ee.json"
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = texttospeech_v1beta1.TextToSpeechClient(credentials=credentials)

synthesis_input = texttospeech_v1beta1.types.SynthesisInput(text="Let's have a test")
voice = texttospeech_v1beta1.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech_v1beta1.enums.SsmlVoiceGender.FEMALE)
audio_config = texttospeech_v1beta1.types.AudioConfig(
        audio_encoding=texttospeech_v1beta1.enums.AudioEncoding.MP3)

response = client.synthesize_speech(synthesis_input, voice, audio_config)

with open('output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

raise KeyboardInterrupt
response = client.list_voices("en-US")
print(response)
input_ = ""

voice = {
  "language_codes": "en-US",
  "name": "en-US-Wavenet-C",
  "ssml_gender": FEMALE,
  "natural_sample_rate_hertz": 24000
}

conf = texttospeech_v1beta1.types.AudioConfig(audio_encoding="utf-8")

audio_config = {}

response = client.synthesize_speech(input_, voice, audio_config)
