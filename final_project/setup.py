from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    description='Emotion detection package using Watson NLP',
    author='EKTA KHAMKAR',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)