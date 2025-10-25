#!/usr/bin/env python3
"""
Streamer Manager - A simple script to manage and watch streamers with MPV
"""

import json
import os
import subprocess
import sys

# File to store streamer data
STREAMERS_FILE = "streamers.json"


def load_streamers():
    """Load streamers from the JSON file"""
    if os.path.exists(STREAMERS_FILE):
        try:
            with open(STREAMERS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: {STREAMERS_FILE} is corrupted. Starting with empty list.")
            return {}
    return {}


def save_streamers(streamers):
    """Save streamers to the JSON file"""
    with open(STREAMERS_FILE, 'w') as f:
        json.dump(streamers, f, indent=2)


def add_streamer():
    """Add a new streamer with name and URL"""
    print("\n=== Add Streamer ===")
    name = input("Enter streamer name: ").strip()
    
    if not name:
        print("Error: Streamer name cannot be empty!")
        return
    
    url = input("Enter streamer URL: ").strip()
    
    if not url:
        print("Error: Streamer URL cannot be empty!")
        return
    
    streamers = load_streamers()
    
    # Check if streamer already exists
    if name in streamers:
        confirm = input(f"Warning: '{name}' already exists. Overwrite? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Cancelled.")
            return
    
    streamers[name] = url
    save_streamers(streamers)
    
    print(f"✓ Streamer '{name}' added successfully!")


def watch_streamer():
    """Display streamers and play the selected one in MPV"""
    streamers = load_streamers()
    
    if not streamers:
        print("\nNo streamers found. Please add a streamer first.")
        return
    
    print("\n=== Available Streamers ===")
    streamer_list = list(streamers.keys())
    
    for i, name in enumerate(streamer_list, 1):
        print(f"{i}. {name}")
    
    try:
        choice = input("\nSelect a streamer (number) or 'q' to quit: ").strip()
        
        if choice.lower() == 'q':
            return
        
        choice_num = int(choice)
        
        if 1 <= choice_num <= len(streamer_list):
            selected_name = streamer_list[choice_num - 1]
            selected_url = streamers[selected_name]
            
            print(f"\nLaunching {selected_name} in MPV...")
            print(f"URL: {selected_url}")
            
            # Launch MPV with the selected URL
            try:
                subprocess.run(['mpv', selected_url])
            except FileNotFoundError:
                print("\nError: MPV not found. Please install MPV to watch streams.")
                print("Install with: sudo apt install mpv (Ubuntu/Debian)")
            except Exception as e:
                print(f"\nError launching MPV: {e}")
        else:
            print("Invalid selection!")
    
    except ValueError:
        print("Invalid input! Please enter a number.")
    except KeyboardInterrupt:
        print("\n\nCancelled.")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("     STREAMER MANAGER")
    print("="*40)
    print("1. Watch")
    print("2. Add Streamer")
    print("3. Exit")
    print("="*40)


def main():
    """Main program loop"""
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                watch_streamer()
            elif choice == '2':
                add_streamer()
            elif choice == '3':
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print("\nInvalid choice! Please select 1, 2, or 3.")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
