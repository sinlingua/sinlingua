from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
setup(
    name='sinlingua',
    version='0.1.4',
    packages=['sinlingua', 'sinlingua.src', 'sinlingua.singlish', 'sinlingua.summarizer', 'sinlingua.grammar_rule',
              'sinlingua.preprocessor', 'sinlingua.sinhala_audio'],
    project_urls={
        'Documentation': 'https://sinlingua.github.io/documentation/',
        'Source': 'https://github.com/sinlingua/sinlingua',
        'Bug Tracker': 'https://github.com/sinlingua/sinlingua/issues',
    },
    license='MIT',
    author='Supun Gurusinghe, Sandaruwini Galappaththi, Supun Sarada Wijesinghe, Binura Yasodya',
    author_email='supunsameeran@gmail.com, sandaruwinigalappaththi@gmail.com, saradawijesinghe@gmail.com, binurayasodya24@gmail.com',
    description='Package for Sinhala data processing',
    python_requires=">=3.7.0",
    long_description=(this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    install_requires=[
        "fuzzywuzzy==0.18.0",
        "gensim==4.3.1",
        "googletrans==4.0.0-rc1",
        "numpy==1.23.0",
        "openai==0.27.8",
        "pandas==1.5.3",
        "pygtrie==1.5.3",
        "Requests==2.31.0",
        "scikit_learn==1.1.3",
        "setuptools==65.5.1",
        "sinling==0.3.6",
        "SpeechRecognition==3.10.0",
        "torch==2.0.1",
        "jedi==0.16",
        "transformers==4.32.0"
    ]
)
