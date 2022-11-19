from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('taQp6erVDVgw9q1MgUdFNef1tLuBYOCMIzEvk6yXJqSn')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/06a8b29d-451d-4553-890f-860aafbabc32')

with open('Tab.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'its the time to take azithromycin now',
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)
