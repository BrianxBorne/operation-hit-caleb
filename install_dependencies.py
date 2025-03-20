import os

def install_dependencies():
    print("Alright, let's install some dependencies. This won't hurt... probably.")
    print("Summoning the Python package gods. Offerings include internet and patience.")
    os.system("pip install numpy matplotlib")
    print("If no errors appeared, congratulations.")

if __name__ == "__main__":
    install_dependencies()
    print("▶To launch the game run the command below")
    print("python hit_caleb.py")

