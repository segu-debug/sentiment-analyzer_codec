# Sentiment Analyzer

A simple Flask web app that analyzes text and predicts sentiment using a Hugging Face Transformers model.

## Overview

This project lets users paste a sentence, review, or short paragraph into a web form and get a sentiment prediction with a confidence score. The current interface includes a text input area, an analyze button, and a result section that shows the predicted label and score.

## Features

- Analyze user-entered text for sentiment.
- Show the predicted sentiment label.
- Display a confidence score for the prediction.
- Run through a lightweight Flask web interface.

## Tech Stack

- Python
- Flask
- Hugging Face Transformers
- Torch
- HTML
- CSS

## Project Structure

```text
sentiment-analyzer/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── screenshots/
│   └── sentiment-result.jpg
└── README.md
```

## How It Works

1. Enter text into the input box.
2. Submit the form.
3. The Flask backend sends the text to the sentiment model.
4. The app returns the predicted sentiment and confidence score.
5. The result is shown on the same page.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open the local Flask URL in your browser.
## Screenshot

![Sentiment Analyzer Result](screenshots/screenshot-sentiment-analyzer.jpg)
https://github.com/segu-debug/sentiment-analyzer_codec/blob/main/screeenshots/screenshot-sentiment-analyzer.png
## Example Inputs

- `This product is amazing and works perfectly.`
- `The experience was okay.`
- `I am very disappointed with this service.`


## Future Improvements

- Add a `requirements.txt` file if it is missing.
- Mention the exact pre-trained model name.
- Add more screenshots, including the empty state and mobile layout.
- Deploy the app on Render, Railway, or Hugging Face Spaces.
- Support multi-class sentiment if you want richer predictions.
