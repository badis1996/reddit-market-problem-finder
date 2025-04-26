# Reddit Market Problem Finder 🔍

## Discover Your Next Startup Idea

The Reddit Market Problem Finder is an AI-powered tool that crawls Reddit to identify hot niche market problems worth solving with a startup. It analyzes discussions across various subreddits to find recurring pain points, evaluates their business potential, and generates detailed reports of viable opportunities.

## 🚀 Features

- **Automated Reddit Crawling:** Scans dozens of subreddits known for discussing problems and pain points
- **AI-Powered Analysis:** Uses GPT models to classify problems and assess market potential
- **Opportunity Scoring:** Ranks problems based on frequency, severity, and market factors
- **Market Validation:** Identifies competing solutions and market gaps
- **Regular Reports:** Delivers findings in structured, easy-to-understand reports
- **Web Interface:** User-friendly dashboard to browse and analyze opportunities
- **API Access:** Programmatic access for integration with other tools

## 🔧 How It Works

1. **Data Collection:** The tool crawls predefined subreddits looking for posts that indicate problems
2. **Problem Identification:** AI detects and extracts problem statements from posts and comments
3. **Clustering & Classification:** Similar problems are grouped and categorized by industry/domain
4. **Opportunity Assessment:** Each problem cluster is evaluated for market size, competition, technical feasibility, etc.
5. **Reporting:** Detailed reports are generated highlighting the most promising opportunities

## 📊 Example Opportunities

Here are some example market problems identified by our tool:

| Problem | Score | Market Size | Competition |
|---------|-------|-------------|-------------|
| Remote workers struggle to find reliable coworking spaces in suburban areas | 8.3/10 | Medium | Low |
| Parents struggle to find reliable, short-notice childcare for sick kids | 8.7/10 | Large | Medium |
| Amateur athletes struggle to find pickup games at their skill level | 7.4/10 | Medium | Medium |

## 🛠️ Installation

### Prerequisites

- Python 3.9+
- Reddit API credentials
- OpenAI API key

### Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/reddit-market-problem-finder.git
cd reddit-market-problem-finder

# Install dependencies
pip install -r requirements.txt

# Copy the example env file and fill in your credentials
cp .env.example .env

# Run the tool
python main.py
```

For detailed installation instructions, see [SETUP.md](SETUP.md).

## 🖥️ Usage

### Command Line

```bash
# Run a full scan and generate a report
python main.py

# Evaluate a specific problem
python startup_evaluation.py "Problem statement to evaluate" --detailed
```

### Web Interface

```bash
# Start the web interface
streamlit run web_interface.py
```

Then open your browser to http://localhost:8501

### API

```bash
# Start the API server
uvicorn api:app --reload
```

The API will be available at http://localhost:8000 with documentation at http://localhost:8000/docs

## 📋 Configuration

You can customize the tool's behavior by modifying the following files:

- **config.py:** Target subreddits, problem keywords, search parameters, etc.
- **topics.py:** Market categories and industry-specific subreddits
- **.env:** API credentials and scheduling settings

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [PRAW](https://praw.readthedocs.io/) for Reddit API integration
- [OpenAI](https://openai.com/) for GPT models
- [Streamlit](https://streamlit.io/) for the web interface
- [FastAPI](https://fastapi.tiangolo.com/) for the API server

## 📝 Roadmap

- Add more sophisticated sentiment analysis
- Incorporate Google Trends data for validation
- Support more social platforms (Twitter, HackerNews, etc.)
- Create browser extension for opportunity identification
- Add competitive analysis features

## 📞 Contact

If you have any questions or suggestions, feel free to open an issue or contact us at your-email@example.com.
