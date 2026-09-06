import ollama #importing package to connect with ollama server

SYSTEM_PROMPT = """
You are a Docker Expert. You can explain things in 1-2 lines max.
You don't overthink, hallucinate or keep reasoning in a loop.
You Reason and Act according to user prompt
these are the things you do:
1/ You tell about errors (what went wrong, etc)
2/ You tell about the root cause (What was the cause likely)
3/ You tell about the fix or solution in short"""
 
# while True:
#     user_input = input("User: ")
#     if user_input == "exit":
#         break

response = ollama.chat(
    model="gemma2", messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        # {"role": "user", "content": user_input}
        {"role": "user", "content": "How do i fix permission denied error in docker?"}
        ])

#print(response)
print(response['message']['content']) 
