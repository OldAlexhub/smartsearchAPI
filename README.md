# AI-Powered Smart Policy Search API

## Description

This project is an **AI-powered Smart Policy Search API** built with Flask and Python. It allows users to search for company policies by typing in keywords, leveraging **Natural Language Processing (NLP)** and fuzzy search techniques. The search queries are analyzed in real-time using **AI models** (like `distilbert-base-cased-distilled-squad` from Hugging Face) to provide relevant policies, making it highly intuitive and interactive.

The backend is powered by Flask and MongoDB, where policies are stored and retrieved. It also implements a typewriter-like effect when displaying results for a more engaging user experience.

## Purpose

The purpose of this project is to provide a **smart search tool** for employees or users to quickly and efficiently find company policies using keywords or phrases. The AI-based approach ensures that even vague or incomplete queries can still return relevant results by using fuzzy search and question-answering models.

This API can be integrated into a web interface or a chatbot where users can input search queries and receive relevant policy descriptions in real-time.

## Key Features

- **AI-powered search**: Uses a question-answering transformer model to retrieve the most relevant results based on the query.
- **Fuzzy matching**: Allows for flexible searching even with typos or incomplete phrases.
- **Real-time query handling**: As users type, the system retrieves relevant policies in real-time.
- **Typewriter effect**: Results are displayed with a typewriter animation to enhance the user experience.

## Technologies Used

- **Flask**: A lightweight Python web framework for building APIs.
- **MongoDB**: A NoSQL database to store and retrieve policies.
- **Pandas**: For data handling and manipulation.
- **Hugging Face Transformers**: For AI-powered question-answering capabilities.
- **FuzzyWuzzy**: A fuzzy matching library to handle approximate string matching.
- **Gunicorn**: A production-grade WSGI server for deploying Flask applications.

## Installation

### Prerequisites

- Python 3.x
- MongoDB (installed and running locally or remotely)
- Git

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-policy-search.git
   cd ai-policy-search
   ```
