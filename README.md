# Retrieval-Augmented Generation (RAG) System

This Retrieval-Augmented Generation (RAG) system processes multilingual PDFs, extracts information, and provides summaries and answers to questions based on the content.

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Multilingual Support**: Process PDFs in various languages.
- **Information Extraction**: Extract key information and summarize content.
- **Question Answering**: Provide answers to user queries based on PDF content.

## Directory Structure

The project is organized into the following directories and files:

## Setup

To set up the RAG system on your local machine, follow these steps:

1. **Clone the Repository**  
   Clone this repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Create a Virtual Environment (Recommended)**
   It is recommended to create a virtual environment to manage dependencies. You can do this with:

   ```bash
    python -m venv venv
   ```

   On macOS/Linux

   ```bash
    source venv/bin/activate
   ```

   On Windows

   ```bash
   .\venv\Scripts\activate
   ```

3. **Install Required Packages**
   Install the required Python packages listed in requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**
   Create a .env file in the project root and add your environment variables. You may need to include API keys, model configurations, and other settings. Here’s an example:

   ```bash
   HUGGINGFACE_API_KEY=your_api_key_here
   ```

5. **Run the Application**
   Execute the main application script to start using the RAG system:
   ```bash
   python -m src.app
   ```
