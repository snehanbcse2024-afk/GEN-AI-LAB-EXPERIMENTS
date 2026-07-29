# Lab 3: Conversational AI Chatbot

## Objective
To build an interactive chatbot using Microsoft's DialoGPT model that can maintain conversation context across multiple turns.

## Theory
DialoGPT is a fine-tuned version of GPT-2 trained on 147M multi-turn dialogues from Reddit. It is designed for open-domain conversation and can maintain context within a session by appending previous conversation history to each new input.

### Key Concepts
- **Tokenization** — Converts user input into model-compatible tokens
- **Chat History** — Concatenates previous turns to maintain context
- **EOS Token** — End-of-sequence token signals the model where responses end

## Code Explanation
1. Loads `microsoft/DialoGPT-medium` tokenizer and model
2. Enters a loop accepting user input
3. Encodes user input + EOS token
4. Concatenates with chat history for multi-turn context
5. Generates model response using sampling
6. Decodes and displays bot reply
7. Loop exits on `quit`

## Dependencies
```
transformers
torch
```

## Expected Output
```
Chatbot ready! Type 'quit' to exit.
>> User: Hello, how are you?
Bot: I'm doing well, thanks for asking!
>> User: What's your name?
Bot: I'm a chatbot created by Microsoft.
>> User: quit
```

## References
- [Microsoft DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium)
- [Hugging Face — Conversational](https://huggingface.co/docs/transformers/main/en/tasks/sequence_modeling)
