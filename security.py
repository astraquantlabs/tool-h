def check_password(password):
    if len(password) < 6:
        return "Weak ❌"
    elif len(password) < 10:
        return "Medium ⚠️"
    return "Strong ✅"