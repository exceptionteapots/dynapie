#!/usr/bin/env python3
# import requests
import argparse
import yaml

from colorama import init as colorama_init, Fore, Back, Style

AVAILABLE_COMMANDS = ["status", "test"]
CONFIG_PATH = "/etc/exceptionteapots/dynapie/client.yaml"

def get_status():
    pass

def load_config(path: str):
    raise Exception("test")


def main():
    parser = argparse.ArgumentParser(prog="dynapie-client", description="Client module of dynapie suite",
                                     epilog=f"by {Back.WHITE}{Fore.BLACK} exception:{Fore.RED}teapots {Style.RESET_ALL} | 2024")

    parser.add_argument("command", metavar="COMMAND", type=str, nargs="?", choices=AVAILABLE_COMMANDS, help=" | ".join(AVAILABLE_COMMANDS))

    parser.parse_args()
    
    # Load the config
    try:
        load_config(CONFIG_PATH)
    except Exception as e:
        print("Failed to load the configuration file:", e)    
    

if __name__ == "__main__":
    main()