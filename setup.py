from setuptools import setup

setup(
    name='sinlingua_test',
    version='0.0.5',
    packages=['sinlingua', 'sinlingua.src', 'sinlingua.singlish', 'sinlingua.summarizer', 'sinlingua.grammar_rule',
              'sinlingua.preprocessor', 'sinlingua.sinhala_audio'],
    url='https://github.com/SupunGurusinghe/SinlinguaDocumentation/blob/main/README.md',
    license='MIT',
    author='Supun Gurusinghe, Sandaruwini Galappaththi, Supun Sarada Wijesinghe, Binura Yasodya',
    author_email='supunsameeran@gmail.com, sandaruwinigalappaththi@gmail.com, saradawijesinghe@gmail.com, binurayasodya24@gmail.com',
    description='Package for Sinhala data processing',
    python_requires=">=3.7.0",
    install_requires=[
        "fuzzywuzzy==0.18.0",
        "gensim==4.3.1",
        "googletrans==3.0.0",
        "numpy==1.22.4",
        "openai==0.27.8",
        "pandas==2.0.3",
        "pygtrie==2.5.0",
        "Requests==2.31.0",
        "scikit_learn==1.1.3",
        "setuptools==56.0.0",
        "sinling==0.3.6",
        "SpeechRecognition==3.10.0",
        "torch==2.0.1",
        "transformers==4.32.0"
    ]
)
