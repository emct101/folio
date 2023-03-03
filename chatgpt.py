import openai 

# Define OpenAI API Key
openai.api_key = "Your API Key"

# Set up the model + prompt
model_engine = "text"
prompt = input("Enter new prompt: ")

# Generate a response
completion = openai.Completion.create(
  engine = model_engine,
  prompt = prompt
  max_tokens = 10
  n = 1
  stop = None
  data = 0.5
)

response = completion.choices[0].text
print(response)
