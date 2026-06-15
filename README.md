# Multi-Agent Research System

An AI-powered research assistant that automates the research workflow using a pipeline of specialized agents. Given a topic, the system searches the web, scrapes relevant content, writes a structured report, and critiques its own output — all orchestrated through LangGraph and exposed via a FastAPI backend with a modern Next.js frontend.

## Features

- **Search Agent** — finds recent, reliable, and detailed information on a given topic using the Tavily search API
- **Scrape Agent** — identifies the most relevant source from search results and extracts deeper content via web scraping
- **Writer Agent** — synthesizes search results and scraped content into a coherent research report
- **Critic Agent** — reviews the generated report and provides constructive feedback
- **Web UI** — clean, modern interface built with Next.js, Tailwind CSS, and Framer Motion, featuring smooth transitions and scroll animations

## Tech Stack

**Backend**
- Python, FastAPI, Uvicorn
- LangChain & LangGraph (agent orchestration)
- Groq / Mistral (LLMs)
- Tavily (web search)
- BeautifulSoup, Requests, lxml (web scraping)

**Frontend**
- Next.js (App Router)
- TypeScript
- Tailwind CSS
- Framer Motion
- Lucide Icons

## Project Structure
Multi agent system project/

├── .env                  # API keys (not committed)

├── requirements.txt      # Python dependencies

├── api.py                # FastAPI backend entry point

├── agents.py             # Agent definitions (search, scrape, writer, critic)

├── tools.py              # Custom tools used by agents

├── pipeline.py           # Core research pipeline logic

└── ui/

└── frontend/          # Next.js application

## Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- API keys for Groq, Mistral, and/or Tavily (as required by `agents.py` and `tools.py`)

### 1. Clone the repository

```bash
git clone https://github.com/amisha-ranjan34/Multi-Agent-Research-System.git
cd Multi-Agent-Research-System
```

### 2. Backend setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the project root with your API keys:

```env
GROQ_API_KEY=your_groq_api_key
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Frontend setup

```bash
cd ui/frontend
npm install
```

## Running the App

### Start the backend

From the project root:

```bash
uvicorn api:app --reload --port 8000
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

### Start the frontend

In a separate terminal:

```bash
cd ui/frontend
npm run dev
```

Open `http://localhost:3000` in your browser.

## Usage

1. Enter a research topic in the input field
2. Click **Run** to start the pipeline
3. The system sequentially runs the search, scrape, write, and critique agents
4. Results appear in cards: the final report, search results, scraped content, and critique

## Running via CLI (without UI)

The original terminal-based pipeline is still available:

```bash
python pipeline.py
```

This prompts you to enter a topic and prints each step's output to the console.

## How It Works

1. **Search** — the search agent queries the web for recent, reliable information on the topic
2. **Scrape** — the scrape agent selects the most relevant URL from the search results and extracts deeper content
3. **Write** — the writer agent combines search results and scraped content into a structured research report
4. **Critique** — the critic agent reviews the report and returns feedback for improvement

## Notes

- LLM provider rate limits (e.g. Groq free tier) may cause request failures during heavy testing. If you encounter a `429 Rate Limit` error, wait for the quota to reset or switch to a different model/provider in `agents.py`.
- The `.env` file should never be committed to version control.

## License

MIT
