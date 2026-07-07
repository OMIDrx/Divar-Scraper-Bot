# Divar Scraper API

A Python application that scrapes advertisements from Divar, exposes the collected data through a REST API, stores it in a SQLite database, and provides a Telegram bot interface for searching and browsing ads.

## Features

- Scrape advertisements from Divar
- REST API built with FastAPI
- SQLite database using SQLAlchemy
- Telegram Bot integration
- Search advertisements by keyword
- View advertisement statistics
- Store scraped data locally
- Retrieve advertisements by ID

## Project Structure

```
divar-scraper/
├── api.py
├── scraper.py
├── app_db.py
├── telegram_bot.py
├── base.py
├── Divar.db
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/home` | Welcome message |
| GET | `/ads` | Fetch live advertisements |
| GET | `/save` | Save advertisements to the database |
| GET | `/database` | Retrieve stored advertisements |
| GET | `/stats` | Display the number of stored advertisements |
| GET | `/search/{keyword}` | Search advertisements by title |
| GET | `/item/{id}` | Retrieve a specific advertisement |

## Telegram Bot Commands

```
/start
/help
/search <keyword>
/item <id>
```

The bot also provides inline buttons for:

- Show Ads
- Show Prices
- Save Database
- Show Database
- Statistics

## Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- BeautifulSoup4
- Requests
- pyTelegramBotAPI

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/divar-scraper-api.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn api:app --reload
```

Start the Telegram bot:

```bash
python telegram_bot.py
```

## Screenshots

You can add screenshots of:

- REST API
- Telegram Bot
- Database results

## Notes

This project is intended for educational purposes. Since Divar's website structure may change over time, the scraper may require updates to remain functional.

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

If you found this project useful, consider giving it a ⭐.
