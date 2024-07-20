import torch
from transformers import BitsAndBytesConfig, pipeline
import whisper
import gradio as gr
from gtts import gTTS
from PIL import Image
import re
import os
import datetime
import locale
import numpy as np
import nltk

nltk.download('punkt')
from nltk import sent_tokenize
