# Divar Scraper Bot

A simple Python project that scrapes advertisements from Divar, provides the data through FastAPI, stores it in a SQLite database using SQLAlchemy, and allows users to view the information using a Telegram Bot.

## Technologies

- Python
- BeautifulSoup
- Requests
- FastAPI
- SQLAlchemy
- SQLite
- Telegram Bot API

## Features

- Scrape Divar advertisements
- Extract title, price and link
- Save data to SQLite
- Search advertisements
- FastAPI endpoints
- Telegram Bot interface

## Run

```bash
uvicorn app:app --reload
```

```bash
python bot.py
```

Developed as the final project for a Python course.
