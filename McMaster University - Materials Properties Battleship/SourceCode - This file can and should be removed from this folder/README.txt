This program was built using pygame and packaged using Pyinstaller. 
The reason for the "Source" folder is not because it's an actual source folder, but to purposely hide the solution GRANTA charts in nested dummy files
All of files in this folder are assets for the game. They're hidden by default.
Due to this game being packaged using pyinstaller, some Window's machines throw a warning before opening the .exe
	This can be safely ignored and bypassed. An alternative packaging method may also work such as cx_freeze to avoid this, but pyinstaller is confirmed safe and functional for this game.

The ctypes.windll.user32.SetProcessDPIAware() line automatically scales the game to the correct DPI, but also makes it a windows exclusive game.
	The default game display is 1600x896, made for modern desktops and laptops



2021, Dr. Bosco Yu and Muhammad Arshad, Department of Materials Science and Engineering & Experiential Learning Office, McMaster University.

These materials may be used for educational, research, and non-commercial purposes only. Any other use, including commercial purposes, is strictly prohibited. If you have any questions about your use, please contact Dr. Bosco Yu, bosco.yu@mcmaster.ca 

These materials are provided on an “as is” basis, without warranty of any kind (either express or implied), including but not limited to any implied warranties of merchantability and fitness for a specific or general purpose.