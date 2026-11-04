# SDGP

# Overview


# Setup 
## Windows 
Run all commands from the project root.

1. Run setup script:
    ``` powershell
    powershell -ExecutionPolicy Bypass -File .\setup_windows.ps1
    ```

2. if `uv` is not installed it will promt you with:
    ``` powershell
    uv is not installed. Run: winget install --id=astral-sh.uv -e                                                                         
    ```
    Run the command shown, Restart your terminal then run `powershell -ExecutionPolicy Bypass -File .\setup_windows.ps1` again. 
> [!NOTE] 
> If you are using vs code close and open the whole window to ensure the terminal has fully restarted.

3. Once the script finishes, activate the virtual environment:
    ``` powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    .\.venv\Scripts\Activate.ps1
    ```
    You will need to run this command in each new terminal session. Run `deactivate` to leave the environement 

## Mac

Run all commands from the project root

1. Run setup script:
    ``` bash
        chmod -x setup_darwin.sh
        ./setup_darwin.sh
    ```

2. If UV is not installed then run:
    ``` bash
        brew install pipx && pipx install uv
    ```

3. To activate the venv, run: 
    ``` bash
        source .venv/bin/activate
    ```

    You will need to run this command in each new terminal session. Run `deactivate` to leave the environement 

## Linux (Debian/Ubuntu-based)

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


