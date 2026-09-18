import logging

# Configure logging
logging.basicConfig(
    filename='web_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def login(username):
    logging.info(f"User {username} logged in")
    # Simulate login processing

def process_data(data):
    try:
        # Simulate data processing
        if data == "bad_data":
            raise ValueError("Invalid data")
        logging.info(f"Data processed: {data}")
    except ValueError as e:
        logging.error(f"Error processing data: {e}", exc_info=True) #when exec info = true we will get information about the exception

def logout(username):
    logging.info(f"User {username} logged out")
    # Sim


if __name__ == "__main__":
    user_name = "Kshitish"
    login(user_name)
    process_data("good_data")
    logout(user_name)