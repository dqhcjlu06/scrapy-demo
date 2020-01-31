def request_from_master():
    return []

def send_to_master():
    pass

def store():
    pass

if __name__ == "__main__":
    current_url = request_from_master()
    to_send = []
    for next_url in current_url:
        to_send.append(next_url)
    
    store(current_url)
    send_to_master(to_send)
