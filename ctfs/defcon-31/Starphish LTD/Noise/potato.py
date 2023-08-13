from pathlib import Path
from llama_hub.file.audio import AudioTranscriber
from pprint import pprint

loader = AudioTranscriber()
documents = loader.load_data(file=Path('./noise.mp3'))

pprint(documents)
