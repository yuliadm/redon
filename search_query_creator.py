# Code found and adapted from https://huggingface.co/Salesforce/xLAM-1b-fc-r

import json
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.random.manual_seed(0)

model_name = "Salesforce/xLAM-1b-fc-r"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name) 

# Please use our provided instruction prompt for best performance
task_instruction = """
You are an expert in composing functions. You are given a question and a set of possible functions. 
Based on the question, you will need to make one or more function/tool calls to achieve the purpose. 
If none of the functions can be used, point it out and refuse to answer. 
If the given question lacks the parameters required by the function, also point it out.
""".strip()

format_instruction = """
The output MUST strictly adhere to the following JSON format, and NO other text MUST be included.
The example format is as follows. Please make sure the parameter type is correct. ALWAYS give an answer.
```
{
    "tool_calls": [
    {"name": "create_query", "arguments": {"word1": "value1", "word3": "value2"}},
    ]
}
```
""".strip()

# Define the input query and available tools
query = "Which materials can I use to build a supercapacitor, to ensure that it will be biodegradable?"

create_query = {
    "name": "create_query",
    "description": "Create a query for a search engine like Arxiv or google patents to answer the asked question. It need to consists of 2 words linked by 'AND'",
    "parameters": {
        "type": "object",
        "properties": {
            "word1": {
                "type": "string",
                "description": "The first word"
            },
            "word2": {
                "type": "string",
                "description": "The second word"
            }
        },
        "required": ["word1", "word2"]
    }
}


openai_format_tools = [create_query]

# Helper function to convert openai format tools to our more concise xLAM format
def convert_to_xlam_tool(tools):
    ''''''
    if isinstance(tools, dict):
        return {
            "name": tools["name"],
            "description": tools["description"],
            "parameters": {k: v for k, v in tools["parameters"].get("properties", {}).items()}
        }
    elif isinstance(tools, list):
        return [convert_to_xlam_tool(tool) for tool in tools]
    else:
        return tools

# Helper function to build the input prompt for our model
def build_prompt(task_instruction: str, format_instruction: str, tools: list, query: str):
    prompt = f"[BEGIN OF TASK INSTRUCTION]\n{task_instruction}\n[END OF TASK INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF AVAILABLE TOOLS]\n{json.dumps(xlam_format_tools)}\n[END OF AVAILABLE TOOLS]\n\n"
    prompt += f"[BEGIN OF FORMAT INSTRUCTION]\n{format_instruction}\n[END OF FORMAT INSTRUCTION]\n\n"
    prompt += f"[BEGIN OF QUERY]\n{query}\n[END OF QUERY]\n\n"
    return prompt
    
# Build the input and start the inference
xlam_format_tools = convert_to_xlam_tool(openai_format_tools)

import json
def create_search_query_from_question(question):
    content = build_prompt(task_instruction, format_instruction, xlam_format_tools, question)
    messages=[
        { 'role': 'user', 'content': content}
    ]
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)

    # tokenizer.eos_token_id is the id of <|EOT|> token
    outputs = model.generate(inputs, max_new_tokens=512, do_sample=False, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
    output = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
    output = json.loads(output)['tool_calls'][0]
    return output['arguments']['word1'] + ' AND ' +  output['arguments']['word2']
create_search_query_from_question('Which materials can I use to build a supercapacitor, to ensure that it will be biodegradable?')