def log_step(func):
    def wrapper():
        print("Starting:", func.__name__)

        func()

        print("Finished:", func.__name__)

    return wrapper


@log_step
def extract_data():
    print("Extracting data from CSV")


@log_step
def transform_data():
    print("Cleaning the data")


@log_step
def load_data():
    print("Loading data into PostgreSQL")


extract_data()
transform_data()
load_data()