import subprocess
import signal
import sys

def install_dependencies():
    # This function will ensure our system is update an initilize needed dependencies
    print(" ===== Installing Dependencies =====")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "postgresql", "postgresql-contrib", "python3", "python3-pip", "-y"])

def install_requirements():
    # This function will ensure all python requirements are installed and functional
    packages = ["django", "psycopg2-binary", "react"]
    print(" ===== Installing Requirements ===== ")
    for package in packages:
        subprocess.run(["pip", "install", package])

def initialize_db():
    # This function will start the Postgre SQL process
    print(" ===== Starting Postgre Process ===== ")
    subprocess.run(["sudo", "pg_ctlcluster", "14", "main", "start"])
    subprocess.run(["pg_isready"])

def create_db():
    # This function will create the database needed to host information
    print(" ===== Initializing DB ===== ")
    subprocess.run(["sudo", "-u", "postgres", "psql", "-c", "CREATE USER admin WITH PASSWORD 'password';"])
    subprocess.run(["sudo", "-u", "postgres", "createdb", "-O", "admin", "main"])

def run_webserver():
    # This function will automatically run the webserver
    print(" ===== Running WebServer =====")
    subprocess.run(["python3", "manage.py", "runserver"])

def end_webinstance(sig, frame):
    # This function will clean up running processes
    print("\n ===== Caught KeyboardInterrupt, stopping PostgreSQL... ===== ")
    subprocess.run(["sudo", "pg_ctlcluster", "14", "main", "stop"])
    subprocess.run(["pg_isready"])
    sys.exit(0)



if __name__ == "__main__":

    signal.signal(signal.SIGINT, end_webinstance) # - This initializes the scanning for a KeyBoard Interrupt
    install_dependencies()
    install_requirements()
    initialize_db()
    # create_db() - This function should not be needed pending review from wider team, this seems to function whether or not this is ran as long as initialize_db() is ran
    run_webserver()
    
