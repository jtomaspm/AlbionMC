import subprocess
import os


# TODO: add install function

def build_vue_app():
    print("Starting build!")
    try:
        cwd = os.path.dirname(os.path.realpath(__file__))
        cwd = os.path.abspath(os.path.join(cwd, 'app'))
        subprocess.run(["npm", "run", "build"],shell=True, cwd=cwd)
        print("Vue.js build completed successfully!")
    except Exception as e:
        print(f"An error occurred during Vue.js build: {e}")

if __name__ == "__main__":
    build_vue_app()