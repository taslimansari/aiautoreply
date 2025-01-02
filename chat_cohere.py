# LVwy0jXt62EqxQ5pSpwDrW1rrL6EPAY4TZL4mkxg

import cohere

co = cohere.Client("LVwy0jXt62EqxQ5pSpwDrW1rrL6EPAY4TZL4mkxg")  # Replace with your API key

command= '''
# it can be anything like a sample chat to test the module independently
'''

# First prompt
response1 = co.generate(
    model="command-xlarge-nightly",
    prompt="You are a person named Taslim Ansari who speaks hindi as well as english. She is from India and is a coder. Analyse the given chat history and respond like Taslim Ansari",
    max_tokens=50
)
print("Response 1:")
print(response1.generations[0].text)

# Second prompt
response2 = co.generate(
    model="command-xlarge-nightly",
    prompt=command,
    max_tokens=50
)
print("\nResponse 2:")
print(response2.generations[0].text)
