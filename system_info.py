import platform

def get_system():
    return {
        "OS": platform.system(),
        "Version": platform.release(),
        "Processor": platform.processor()
    }
