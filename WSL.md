# Configure WSL
Install windows sub-system for linux to enable with the easier manipulation of linux
1. Install wsl
2. Open powershell and confirm that wsl is installed. Run the command ```wsl --status``` The return statement should contain a ```Default Version: 2```
3. Ope n office store and search ubuntu and install ubuntu
4. Open ubuntu and runt the  following command to check the release. ```lsb_release```
- if prompted to enter the UNIX user name. 
    ```
    Enter new UNIX username: <username>
    New password:
    Retype new password:
    ```
5. Open the windows explorer anfd under the search bar look for the wsl network.
6. On vs code
- Open Remote -WSL extension from microst
- Go to the bottom lef green/blue button ```><``` and click.
- On the popup click on ```New WSL Window using Distro```
- Select the WSL and let the updates to occur
- Some things are not shared such as ubuntu
