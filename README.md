# Stock Analysis App

## 🚀 Features
- AI-powered stock, research, and investment analysis
- Modern frontend (served by FastAPI backend)
- Ready for Railway, Render, or local Docker deployment

---

## 🖥️ Running Locally

### 1. **Clone the Repository**
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. **Set Up Environment Variables**
Create a `.env` file in the project root (or export variables in your shell):
```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
GOOGLE_CSE_ID=your_google_cse_id
# Optional: COMPANY_TICKERS=AAPL,GOOG,MSFT
```
Or, export them in your terminal:
```bash
export OPENAI_API_KEY=your_openai_key
export GOOGLE_API_KEY=your_google_key
export GOOGLE_CSE_ID=your_google_cse_id
```

### 3. **Install Python Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. **Install Node.js Dependencies for Google Search MCP**
```bash
cd google-search-mcp
npm install
npm run build
cd ..
```

### 5. **Run the App**
```bash
export PORT=8000  # or any port you want
python main.py
```
- The app will be available at [http://localhost:8000](http://localhost:8000)
- The frontend is served at `/`
- Healthcheck endpoint: [http://localhost:8000/health](http://localhost:8000/health)

### 6. **(Optional) Run with Docker**
```bash
docker build -t stock-analysis-app .
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_openai_key \
  -e GOOGLE_API_KEY=your_google_key \
  -e GOOGLE_CSE_ID=your_google_cse_id \
  stock-analysis-app
```

---

## ⚙️ **What to Change for Local vs. Deployment**

- **Environment Variables:**
  - Locally: Use `.env` or `export ...` in your shell
  - Deployment: Set them in your cloud platform’s dashboard (Railway, Render, etc.)
- **Port:**
  - Locally: You can use any port (default is 8000)
  - Deployment: The platform sets the `PORT` variable automatically; your code already handles this
- **Start Command:**
  - Locally: `python main.py`
  - Deployment: Use `python main.py` (not `uvicorn ... --port $PORT`)
- **Frontend:**
  - Served automatically by FastAPI at `/`

---

## 🛠️ **Troubleshooting**

- **App crashes on startup?**
  - Check that all required environment variables are set
  - Check logs for missing package errors
- **Healthcheck fails on deployment?**
  - Make sure you do NOT set a custom `PORT` variable in Railway/Render
  - Your code should use `os.getenv("PORT", 8000)`
  - Healthcheck endpoint must be `/health` and return 200 OK
- **Docker build fails?**
  - Make sure Node.js and Python dependencies are installed as per the Dockerfile

---

## 📦 **Project Structure**
- `main.py` — FastAPI backend and static frontend serving
- `frontend/` — HTML, JS, and CSS for the dashboard
- `google-search-mcp/` — Node.js tool for Google search
- `requirements.txt` — Python dependencies
- `Dockerfile` — For containerized deployment

---

## 🌐 **Deploying to Cloud**
See [DEPLOYMENT.md](DEPLOYMENT.md) for full cloud deployment instructions (Railway, Render, AWS, etc.)

---

**Happy coding!**

