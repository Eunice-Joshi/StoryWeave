import requests

# 🔹 Replace this with your actual API key from Together AI
API_KEY = "tgp_v1_4NWwD3gCLsrp6r-xB4-3S5BCUu1ZYkpsOi0l445OJOQ"

# 🔹 Together AI API URL for chat models
url = "https://api.together.ai/v1/chat/completions"

# 🔹 Set up headers with your API key
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 🔹 Define the request payload
data = {
    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Change this if the model isn't available
    "messages": [{"role": "user", "content": "Tell me a short fantasy story."}]
}

# 🔹 Send the API request
response = requests.post(url, json=data, headers=headers)

# 🔹 Print the response (check if it works)
print(response.json())

