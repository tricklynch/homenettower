from uvicorn import run

if __name__ == "__main__":
    run("homenettower:create_app", port=5000, log_level="debug")
