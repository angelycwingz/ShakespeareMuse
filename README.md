# JokeGen App

A full-stack application for generating poetry using state-of-the-art AI models from Hugging Face.

## Overview

ShakespeareMuse App is a fun project that leverages generative AI to create original poetry. The backend is built with FastAPI, while the frontend provides a simple interface for users to generate and view poetry.

## Features
- Generate poetry using advanced AI models
- FastAPI backend for API endpoints
- Simple frontend for user interaction
- Powered by Hugging Face models

## Project Structure
```
backend/
    main.py           # FastAPI app
    genai.py          # AI logic using Hugging Face
    schemas.py        # Pydantic schemas
    requirements.txt  # Backend dependencies
frontend/
    app.py            # Frontend app
    requirements.txt  # Frontend dependencies
```

## Getting Started

### Backend
1. Navigate to the `backend` directory:
   ```powershell
   cd backend
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```powershell
   uvicorn main:app --reload
   ```

### Frontend
1. Navigate to the `frontend` directory:
   ```powershell
   cd frontend
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the frontend app:
   ```powershell
   python app.py
   ```

## Powered by Hugging Face
This project uses Hugging Face models for poetry generation. Learn more at [huggingface.co](https://huggingface.co/).

## License
MIT License
