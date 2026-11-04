# SDGP

# Overview


# Setup 
## Windows 

## Mac

## Linux (Debain/Ubuntu-based)

Run all commands from the project root.

1. Run setup script:
    ``` bash
    chmod -x setup_ubuntu.sh
    ./setup_ubuntu
    ```

2. If `uv` is not installed it will promt you with:
    ``` bash
    uv is not installed. Run: sudo apt install pipx && pipx install uv
    ```
    Run the command shown, then run `./setup_ubuntu` again. If `uv` isn't found afterwards run `pipx ensurepath` and restart your terminal

3. Once the script finsishes, activate the virtual environment:
    ``` bash 
    source .venv/bin/activate
    ```
    You will need to run this command in each new terminal session. Run `deactivate` to leave the environement 



# Usage


