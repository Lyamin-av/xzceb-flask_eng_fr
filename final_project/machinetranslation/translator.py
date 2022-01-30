"""This script for translate En to Fr and Fr to En"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('0kQedKP98q7hjsoQZP0GQY5dtYwr1UGMRK1gT_P4nxY0')
language_translator = LanguageTranslatorV3(
    version='2022-01-28',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/0fcd4c0c-660f-4357-82c4-75bd9e407565')

def english_to_french(englishtext):
    """English to French"""
    frenchtext = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    frenchtextfin = frenchtext['translations'][0]['translation']
    return frenchtextfin

def french_to_english(frenchtext):
    """French to English"""
    englishtext = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    englishtextfin = englishtext['translations'][0]['translation']
    return englishtextfin
