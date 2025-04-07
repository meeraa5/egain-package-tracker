#!/usr/bin/env python3
"""
eGain Package Tracking Chatbot
Internship Assignment
"""

import sys
try:
    from colorama import init, Fore, Style, Back
    # Initialize colorama for cross-platform colored terminal output
    init()
    COLORAMA_AVAILABLE = True
except ImportError:
    print("Note: For colored output, install colorama: pip install colorama")
    COLORAMA_AVAILABLE = False

# The PACKAGES dictionary contains sample tracking data for demonstration purposes
PACKAGES = {
    "TN123456789US": "Your package is in transit. Last location: Denver, CO. Expected delivery: April 6, 2023.",
    "987654321098": "Your package is delayed due to weather. Current location: Chicago, IL. New delivery: April 8, 2023.",
    "ER123456789CH": "Your package was delivered to the wrong address: 123 Main St, Apt 4B instead of Apt 4C."
}

def print_colored(text, color=Fore.WHITE, bright=False):
    """Print text with color if colorama is available"""
    if COLORAMA_AVAILABLE:
        if bright:
            print(f"{Style.BRIGHT}{color}{text}{Style.RESET_ALL}")
        else:
            print(f"{color}{text}{Style.RESET_ALL}")
    else:
        print(text)

def print_title():
    """Print the eGain-themed title banner"""
    border = "=" * 60
    
    if COLORAMA_AVAILABLE:
        print(f"\n{Style.BRIGHT}{Fore.MAGENTA}{border}")
        print(f"{Style.BRIGHT}{Fore.MAGENTA}  e{Style.RESET_ALL}{Style.BRIGHT}{Fore.MAGENTA}Gain Package Tracker")
        print(f"{Style.BRIGHT}{Fore.MAGENTA}{border}{Style.RESET_ALL}")
    else:
        print(f"\n{border}")
        print("  eGain Package Tracker")
        print(f"{border}")

def print_bot_message(message):
    """Print a message from the bot"""
    if COLORAMA_AVAILABLE:
        print(f"\n{Fore.MAGENTA} {message}{Style.RESET_ALL}")
    else:
        print(f"\n {message}")

def print_options(options):
    """Print menu options"""
    if COLORAMA_AVAILABLE:
        print(f"\n{Fore.MAGENTA}{Back.BLACK}Options:{Style.RESET_ALL}")
        for i, option in enumerate(options, 1):
            print(f"{Fore.MAGENTA}  {i}. {Style.RESET_ALL}{option}")
    else:
        print("\nOptions:")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")

def get_user_input():
    """Get input from the user"""
    if COLORAMA_AVAILABLE:
        return input(f"\n{Fore.MAGENTA} {Style.RESET_ALL}")
    else:
        return input("\n ")

# Main function for the chatbot
# Displays welcome message, main menu, and handles primary navigation
def main():
    """Main function to run the chatbot"""
    print_title()
    print_bot_message(f"Welcome to the eGain Package Tracking Assistant!")
    
    while True:
        # Display main menu options
        print_bot_message("What would you like to do today?")
        print_options([
            "Track a package", 
            "Report a lost package", 
            "Fix a delivery problem",
            "Exit"
        ])
        
        choice = get_user_input()

         # Process user selection
        if choice == "1":
            track_package()
        elif choice == "2":
            handle_lost_package()
        elif choice == "3":
            handle_delivery_problem()
        elif choice == "4" or choice.lower() in ["exit", "quit", "bye"]:
            # Handle exit command with friendly goodbye
            print_bot_message("Thank you for using the eGain Package Tracker. Goodbye!")
            break
        else:
             # Error handling for invalid menu selections
            if COLORAMA_AVAILABLE:
                print_bot_message(f"{Fore.RED}Please select a valid option (1-4).{Style.RESET_ALL}")
            else:
                print_bot_message("Please select a valid option (1-4).")

# Handles the package tracking workflow
# Asks for tracking number, validates it, displays status, and offers alerts
def track_package():
    """Handle package tracking"""
    print_bot_message("Please enter your tracking number:")

    # Convert input to uppercase and remove spaces for consistent formatting
    tracking_number = get_user_input().upper().replace(" ", "")
    
    if tracking_number in PACKAGES:
        # Display tracking information for valid tracking numbers
        print_bot_message(PACKAGES[tracking_number])
    else:
        # Provide helpful guidance when tracking number isn't found
        invalid_message = "Tracking number not found. For this demo, I can only track these numbers: "
        if COLORAMA_AVAILABLE:
            print_bot_message(f"{invalid_message}{Fore.MAGENTA}TN123456789US, 987654321098, ER123456789CH{Style.RESET_ALL}")
        else:
            print_bot_message(f"{invalid_message}TN123456789US, 987654321098, ER123456789CH")
    
    print_bot_message("Would you like to set up SMS alerts for this package?")
    print_options(["Yes", "No"])
    
    alert_choice = get_user_input()
    
    if alert_choice == "1":
        if COLORAMA_AVAILABLE:
            print_bot_message(f"{Fore.GREEN}SMS alerts have been set up. You'll receive updates when your package status changes.{Style.RESET_ALL}")
        else:
            print_bot_message("SMS alerts have been set up. You'll receive updates when your package status changes.")
    else:
        print_bot_message("No problem. No alerts will be set up.")

# Handles the lost package reporting workflow
# Determines if package is eligible for claim based on time since expected delivery
def handle_lost_package():
    """Handle lost package reporting"""
    print_bot_message("I'm sorry to hear your package may be lost.")
    print_bot_message("Has it been more than 7 days since the expected delivery date?")
    print_options(["Yes", "No"])
    
    days_choice = get_user_input()
    
    if days_choice == "1":
        if COLORAMA_AVAILABLE:
            print_bot_message(f"{Fore.GREEN}You can file a claim for your lost package. For this demo, your claim has been filed.{Style.RESET_ALL}")
        else:
            print_bot_message("You can file a claim for your lost package. For this demo, your claim has been filed.")
    else:
        print_bot_message("Please wait a few more days. The package might still be in transit.")

# Handles delivery problem resolution
# Offers options for redelivery or replacement
def handle_delivery_problem():
    """Handle delivery problems"""
    print_bot_message("I'm sorry you're having a delivery problem.")
    print_bot_message("What would you like to do?")
    print_options(["Schedule a redelivery", "Request a replacement"])
    
    problem_choice = get_user_input()
    
    if problem_choice == "1":
        if COLORAMA_AVAILABLE:
            print_bot_message(f"{Fore.GREEN}A redelivery has been scheduled for tomorrow between 2-4 PM.{Style.RESET_ALL}")
        else:
            print_bot_message("A redelivery has been scheduled for tomorrow between 2-4 PM.")
    else:
        if COLORAMA_AVAILABLE:
            print_bot_message(f"{Fore.GREEN}A replacement package will be shipped within 2 business days.{Style.RESET_ALL}")
        else:
            print_bot_message("A replacement package will be shipped within 2 business days.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThank you for using eGain Package Tracker. Goodbye!")
        sys.exit(0)
