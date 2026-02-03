import boto3 
 
# Create Bedrock client 
client = boto3.client("bedrock", region_name="us-east-1") 
 
# Example prompt 
prompt = "Translate this sentence to French: 'Hello world!'" 
 
# Call a foundation model 
response = client.invoke_model( 
    modelId="anthropic.claude-v2",  
    body=prompt,  
    contentType="text/plain"  
) 
 
# Read and print output 
output = response["body"].read().decode() 
print("Bedrock model output:", output) 
