import os
from dotenv import load_dotenv
from groq import Groq
from together import Together
from openai import OpenAI

load_dotenv()

groq_client = Groq(api_key=os.environ.get('GROQ_API_KEY'))
together_client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))
perplexity_client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url="https://api.perplexity.ai"
)

def collect_user_input():
    print("Welcome to the AI-powered Market Research and Cold Email Generator!")
    print("Please provide some information about your target:")
    
    while True:
        target_type = input("Are you targeting an industry or a specific company? (industry/company): ").lower().strip()
        if target_type in ['industry', 'company']:
            break
        print("Invalid input. Please enter 'industry' or 'company'.")
    
    if target_type == 'industry':
        target = input("Please enter the industry you want to target: ").strip()
    else:
        target = input("Please enter the name of the company you want to target: ").strip()
    
    additional_info = input("Any additional information or specific areas of interest? (Press Enter to skip): ").strip()
    
    return {
        "target_type": target_type,
        "target": target,
        "additional_info": additional_info
    }

def get_llama_response(prompt, max_tokens=256):
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that generates optimized search queries based on user input. Your queries should be concise and focused on gathering market research information."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>","<|eom_id|>"]
    )
    return response.choices[0].message.content

def optimize_search_queries(user_input):
    target_type = user_input["target_type"]
    target = user_input["target"]
    additional_info = user_input["additional_info"]

    prompt = f"Generate 5 optimized search queries for market research on the {target_type} '{target}'. "
    if additional_info:
        prompt += f"Additional information: {additional_info}. "
    prompt += "Each query should be on a new line and focus on different aspects of market research such as market size, competitors, trends, challenges, and opportunities."

    response = get_llama_response(prompt)
    queries = [query.strip() for query in response.split('\n') if query.strip()]

    return queries

def get_perplexity_response(query):
    response = perplexity_client.chat.completions.create(
        model="llama-3-sonar-large-32k-online",
        messages=[
            {
                "role": "system",
                "content": "You are an AI research assistant. Provide a concise summary of the most relevant information found online for the given query. Focus on factual data and key insights."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

def perform_web_research(queries):
    research_results = []
    for query in queries:
        print(f"Researching: {query}")
        result = get_perplexity_response(query)
        research_results.append({"query": query, "result": result})
    return research_results

def generate_cold_email(research_results, user_input):
    # Prepare a summary of the research results
    research_summary = "\n".join([f"- {result['query']}: {result['result'][:100]}..." for result in research_results])

    prompt = f"""
    You are an AI assistant tasked with writing a personalized cold email. Use the following information to craft the email:

    Target: {user_input['target_type'].capitalize()} - {user_input['target']}
    Additional Info: {user_input['additional_info']}

    Research Summary:
    {research_summary}

    Write a compelling cold email that:
    1. Has a clear and attention-grabbing subject line
    2. Introduces the sender and their company briefly
    3. Demonstrates knowledge of the target {user_input['target_type']} based on the research
    4. Highlights a specific pain point or opportunity
    5. Proposes a solution or collaboration
    6. Includes a clear call-to-action
    7. Keeps the tone professional yet conversational
    8. Is concise (aim for around 150-200 words)

    Format the email with Subject Line, Greeting, Body, and Signature.
    """

    email_content = get_llama_response(prompt, max_tokens=512)
    return email_content

def main():
    user_input = collect_user_input()
    print("User input collected:", user_input)
    
    optimized_queries = optimize_search_queries(user_input)
    print("Optimized search queries:")
    for i, query in enumerate(optimized_queries, 1):
        print(f"{i}. {query}")
    
    research_results = perform_web_research(optimized_queries)
    print("\nResearch Results Summary:")
    for result in research_results:
        print(f"Query: {result['query']}")
        print(f"Summary: {result['result'][:150]}...")  # Print first 150 characters of each result
        print()
    
    cold_email = generate_cold_email(research_results, user_input)
    print("\nGenerated Cold Email:")
    print(cold_email)

if __name__ == "__main__":
    main()
