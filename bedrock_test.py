# bedrock_test.py 
# Local Bedrock dry-run, no API calls 
 
def invoke_model(prompt): 
    if "translate" in prompt.lower(): 
        return "Bonjour le monde!" 
    elif "summarize" in prompt.lower(): 
        return "This is a summary of the text." 
    else: 
        return "Simulated Bedrock output: " + prompt 
 
prompts = [ 
    "Translate this sentence to French: 'Hello world!'", 
    "Summarize this paragraph: 'Python is great for ML projects.'" 
] 
 
for p in prompts: 
    output = invoke_model(p) 
    print("Prompt:", p) 
    print("Model output:", output) 
    print("-" * 40) 
