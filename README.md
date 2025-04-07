eGain Package Tracking Chatbot

A command-line chatbot for tracking packages, reporting lost items, and resolving delivery issues. Created for the eGain internship assignment.

Overview:
This Python-based chatbot demonstrates a simple, effective conversation flow for package tracking customer service. It's styled with eGain's official magenta/black branding and designed to handle three main scenarios:
Tracking a package with a tracking number
Reporting a lost package
Resolving delivery problems

Installation:
Requirements:
Python 3.6 or higher
Colorama (optional, for enhanced visual experience)

Setup:
Clone this repository:
Copy git clone https://github.com/meeraa5/egain-package-tracker.git

Install colorama (optional but recommended for the best experience):
Copy pip install colorama

Run the chatbot:
Copy python package_tracker4.py


Features:
Simple Interface: Clean, menu-driven command-line interface
eGain Branding: Magenta and black colors matching eGain's official branding
Guided Navigation: Numbered options for easy selection
Error Handling: Clear validation and error messages
Demo Data: Sample tracking information for demonstration


How It Works:
The chatbot follows a simple, logical conversation flow:
Main menu with 4 clearly defined options
Each option leads to a specific, self-contained process
When the process completes, control returns to the main menu
Clear exit option available at any time

Here's a flowchart showing the conversation paths in the chatbot:
![flowchart](https://github.com/user-attachments/assets/5b350f8c-5cdf-4482-bff4-6298c1c5e19c)


Sample Tracking Numbers:
For this demo, you can track these numbers:
TN123456789US (In transit)
987654321098 (Delayed)
ER123456789CH (Wrong address)


Error Handling
The chatbot implements two main error handling mechanisms:
Invalid Menu Selection: When a user selects an option that doesn't exist, they receive a clear error message and are prompted to try again.
Invalid Tracking Number: When a tracking number isn't recognized, the chatbot provides examples of valid numbers and continues the conversation.
These error handling approaches ensure a smooth user experience even when unexpected inputs are provided.
![image](https://github.com/user-attachments/assets/b723c353-1341-4183-b443-75c4f5e82d20)


Screenshots:
![screenshot1](https://github.com/user-attachments/assets/1dda840d-037a-4d92-81b5-f8477f42d548)
![screenshot2](https://github.com/user-attachments/assets/bc6fd354-1b77-4700-baae-e70e6eb42234)
![screenshot3](https://github.com/user-attachments/assets/b0fc2150-2113-4e1e-af35-716db2309b84)
![screenshot4](https://github.com/user-attachments/assets/dc64dd7f-2085-459f-8396-4beb2cd63b83)
![screenshot5](https://github.com/user-attachments/assets/6306ad22-dfa2-4c7b-958b-5e2bcc82ad15)


Design Approach:
I approached this project with a focus on simplicity and user experience:
I prioritized clear navigation and helpful error messages to guide users through the conversation.
I incorporated eGain's visual identity through its signature magenta color and clean design aesthetic.
I structured the code with separate functions for each conversation path to enhance maintainability.
Information is presented in manageable chunks rather than overwhelming users with too much at once.
The chatbot works well even without the colorama library, though it looks best with color support.


Future Improvements:
With more time and resources, this chatbot could be enhanced with:
Web interface matching eGain's website design
Natural language processing for more flexible conversation
Integration with real carrier tracking APIs
User authentication for personalized tracking history
Multi-language support
Voice interface capabilities
