from google.cloud import texttospeech_v1beta1
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "OAuth/JING-704cd29711ee.json",
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = texttospeech_v1beta1.TextToSpeechClient(credentials=credentials)

voice = texttospeech_v1beta1.types.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech_v1beta1.enums.SsmlVoiceGender.FEMALE)

audio_config = texttospeech_v1beta1.types.AudioConfig(
        audio_encoding=texttospeech_v1beta1.enums.AudioEncoding.MP3)

def textToSpeech(text):
    synthesis_input = texttospeech_v1beta1.types.SynthesisInput(text=text)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    '''with open("tmp/output.mp3", "wb") as out:
            out.write(response.audio_content)
            print("Audio content written to file 'tmp/output.mp3'")'''
    return response.audio_content
