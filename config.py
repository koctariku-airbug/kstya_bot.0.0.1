def load_token():
    with open("token.txt", "r", encoding="utf-8") as f:
        return f.readline().strip()