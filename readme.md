# NLP Text Summarizer

## Overview
A web application for text summarization using Hugging Face's pre-trained BART model.

## Setup and Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`

## Deployment Instructions (Render)
1. Create a `render.yaml` file
2. Sign up on Render.com
3. Connect GitHub repository
4. Select "Web Service" during deployment
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn app:app`

## Technologies
- Flask
- Hugging Face Transformers
- Tailwind CSS
- Pre-trained BART model