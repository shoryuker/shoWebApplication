import subprocess

def install_dependencies():
    print("Installing Dependencies")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "postgresql", "postgresql-contrib", "python", "python3", "python3-pip", "-y"])

def install_requirements():
    packages = ["django", "psycopg2", "pygresql"]
    print("Installing Requirements")
    for package in packages:
        subprocess.run(["pip", "install", package])



if __name__ == "__main__":
    install_dependencies()
    install_requirements()
    
