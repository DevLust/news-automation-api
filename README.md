# 📰 News Automation & Scraper API

A professional, high-performance API built with **FastAPI** and **Python** designed for real-time news retrieval and automated data structuring. This project is optimized for deployment as a **Micro-SaaS** on marketplaces like **RapidAPI**.

## 🚀 Key Features
- **Real-Time Global Search:** Fetches the latest headlines from thousands of worldwide sources.
- **Clean JSON Output:** Returns structured data ready for frontend, bots, or RPA integrations.
- **Production Ready:** Implements security best practices with Environment Variables.
- **FastAPI Powered:** Extremely low latency and high concurrency support.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Security:** OS Environment Variables (No hardcoded keys)
- **Deployment:** Fully compatible with Railway, Render, and AWS Lambda.

## ⚙️ Setup & Local Development

1. **Clone the repository:**
```bash
git clone https://github.com/DevLust/news-automation-api.git
cd news-automation-api
```

2. **Set up Environment Variables:**
Create a `.env` file in the root directory and add your NewsAPI key:
```
NEWS_API_KEY=your_secret_key_here
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the server:**
```bash
uvicorn main:app --reload
```

## 🔌 API Endpoints

### GET /
Health check to verify if the service is online.

**Response:**
```json
{
  "status": "Online",
  "mensagem": "API de Notícias pronta para uso"
}
```

### GET /buscar-noticias?tema={topic}
Fetches the top 10 news articles about a specific subject.

**Parameters:**
- `tema` (string, required) - The keyword to search for

**Response:**
```json
{
  "tema_buscado": "technology",
  "total_resultados": 10,
  "noticias": [...]
}
```

## 💰 Monetization
This API is designed to work with RapidAPI. It supports tiered subscription models, allowing developers to monetize based on request volume.

## 👨‍💻 Author
Developed by **Luis Felype** - Software Engineering Student & Automation Enthusiast
