import json
import random



# Get recent messages
def get_recent_messages():
    
    # Define the file name and learn instruction
    file_name ='stored_data.json'
    learn_instruction = {
        'role': 'system',
        'content': 'You are interviewing the user for a job as a retail assistant.\
                    Ask short questions that are relevant to the junior position.\
                    Your name in Rachel. the user is called Ashkan. keep your answers to under 30 words.',
        # 'content': 'تو یک ارشد برنامه نویس پایتون هستی و میخوای از من توی یک مصاحبه سوالاتی برای شغل برنامه نویس تازه کار بپرسی جواب هات رو زیر 30 کلمه بده.',
    }

    # initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction['content'] = learn_instruction['content'] + 'Your response will include some dry humour.'
    else:
        learn_instruction['content'] = learn_instruction['content'] + 'Your response will include a rather challenging question.'
    
    # Append instruction to messages
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            
            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)  
    except Exception as e:
        print(e)
        pass

    # Return messages
    return messages


# Store Messages
def store_messages(request_message, response_message):
    
    # Define the file name
    file_name = 'stored_data.json'

    # Get recent messages
    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {'role': 'user', 'content': request_message}
    assistant_message = {'role': 'assistant', 'content': request_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(file_name, 'w') as f:
        json.dump(messages, f)


# Reset Messages
def reset_messages():
    
    # Overwrite existing messages with noting
    open('stored_data.json', 'w')
