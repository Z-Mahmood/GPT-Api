import datetime

class ChatCompletionMessage:
    def __init__(self, content, role):
        self.content = content
        self.role = role

class Choice:
    def __init__(self, finish_reason, index, message):
        self.finish_reason = finish_reason
        self.index = index
        self.message = message  # This will be an instance of ChatCompletionMessage

class CompletionUsage:
    def __init__(self, completion_tokens, prompt_tokens, total_tokens):
        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens
        self.total_tokens = total_tokens

class ChatCompletion:
    def __init__(self, completion_id, choices, model, created, usage):
        self.id = completion_id
        self.choices = choices  # This will be a list of Choice instances
        self.model = model
        self.created = datetime.datetime.fromtimestamp(created)
        self.usage = usage  # This will be an instance of CompletionUsage

def parse_response(response):
    choices = []
    for choice_data in response.choices:
        message_data = choice_data.message
        message = ChatCompletionMessage(content=message_data.content, role=message_data.role)
        choice = Choice(
            finish_reason=choice_data.finish_reason, 
            index=choice_data.index, 
            message=message
        )
        choices.append(choice)

    usage_data = response.usage
    usage = CompletionUsage(
        completion_tokens=usage_data.completion_tokens, 
        prompt_tokens=usage_data.prompt_tokens, 
        total_tokens=usage_data.total_tokens
    )

    chat_completion = ChatCompletion(
        completion_id=response.id,
        choices=choices,
        model=response.model,
        created=response.created,
        usage=usage
    )
    
    return chat_completion