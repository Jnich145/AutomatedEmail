# AI-powered Market Research and Cold Email Generator

This Python script uses artificial intelligence to perform market research and generate personalized cold emails based on user input. It's designed to help businesses gather information about specific industries or companies and create targeted outreach emails.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Setting Up API Keys](#setting-up-api-keys)
5. [Running the Script](#running-the-script)
6. [How It Works](#how-it-works)
7. [Customization](#customization)
8. [Troubleshooting](#troubleshooting)
9. [Additional Resources](#additional-resources)

## Introduction

This script combines several AI technologies to automate the process of market research and cold email generation. It uses three different AI models:

- Llama (via Together AI) for generating search queries and the final email
- Perplexity AI for web research
- Groq (not currently used in the script, but available for future expansion)

## Prerequisites

Before you can use this script, you need to have the following installed on your computer:

- Python 3.7 or higher
- pip (Python package installer)

You should also be familiar with basic command-line operations.

## Installation

1. Create a new directory for your project:
   - mkdir market-research-email-generator
   - cd market-research-email-generator

2. Create a virtual environment (this keeps your project dependencies separate from other Python projects):
   - python -m venv venv

3. Activate the virtual environment:
   - On Windows: venv\Scripts\activate
   - On macOS and Linux: source venv/bin/activate

4. Create a new file called `requirements.txt` and add the following lines:
   - python-dotenv
   - groq
   - together
   - openai

5. Install the required packages:
   - pip install -r requirements.txt

6. Create a new file called `main.py` and paste the entire script into it.

## Setting Up API Keys

1. Sign up for accounts and obtain API keys from:
   - Together AI
   - Perplexity AI
   - Groq (optional for now)

2. Create a new file in your project directory called `.env`.

3. Add your API keys to the `.env` file:
   - TOGETHER_API_KEY=your_together_api_key_here
   - OPENAI_API_KEY=your_perplexity_api_key_here
   - GROQ_API_KEY=your_groq_api_key_here

   Replace `your_*_api_key_here` with your actual API keys.

## Running the Script

1. Make sure your virtual environment is activated.

2. Run the script:
   - python main.py

3. Follow the prompts to enter information about your target industry or company.

4. The script will generate search queries, perform web research, and create a cold email based on the results.

## How It Works

1. **User Input**: The script asks you whether you're targeting an industry or a specific company, and collects relevant information.

2. **Query Generation**: It uses the Llama AI model to create optimized search queries based on your input.

3. **Web Research**: The script uses these queries to perform web searches using the Perplexity AI model, which summarizes the most relevant information found online.

4. **Email Generation**: Finally, it uses the Llama AI model again to create a personalized cold email based on the research results and your initial input.

## Customization

You can customize the script by modifying the prompts sent to the AI models. Look for the `prompt` variables in the `optimize_search_queries` and `generate_cold_email` functions.

## Troubleshooting

- If you get an error about missing modules, make sure you've activated your virtual environment and installed all requirements.
- If you get API errors, double-check that your API keys in the `.env` file are correct and that you have sufficient credits/quota with each service.

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Virtual Environments in Python](https://docs.python.org/3/tutorial/venv.html)
- [Environment Variables in Python](https://docs.python.org/3/library/os.html#os.environ)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

Remember to keep your API keys secret and never share them publicly. Happy coding!
