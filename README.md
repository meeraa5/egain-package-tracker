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
Copy package_tracker4.py


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
