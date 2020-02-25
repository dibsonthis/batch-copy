import threading
import pyperclip

def get_clipboard_data():
    data = pyperclip.paste()
    return data

def copy_to_clipboard(content):
    pyperclip.copy(content)

def clear_clipboard():
    pyperclip.copy('')

def batch_copy():

    content_list = []

    # Clears the clipboard
    clear_clipboard()

    # Clears file
    open('batch_copy.txt', 'w').close()

    print("Batch Copy Started")

    while not stop_event.isSet():
        # Opens file for appending
        with open('batch_copy.txt', 'a+') as file:
            content = get_clipboard_data()
            if content:
                content_list.append(content)
                file.write(content + ' ')
                clear_clipboard()
                print(content_list)

    print("Batch Copy Ended")

    with open('batch_copy.txt', 'r') as file:
        file_content = file.read()

    copy_to_clipboard(file_content)

    # Join all blocks together
    content_list = ' '.join(content_list)
    # Insert into clipboard
    copy_to_clipboard(content_list)

def begin_batch_copy():
    thread = threading.Thread(target=batch_copy)
    thread.start()

def end_batch_copy():
    stop_event.set()

stop_event = threading.Event()
