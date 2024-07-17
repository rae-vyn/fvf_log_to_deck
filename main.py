import json

def main():
    print("### FVF DECK CONVERTER ###")
    print("Uses your player.log file to snag your decks and turns them into deck sharing links.")
    
    # Get the player.log path
    print("Enter your player.log file location: ")
    log_location = input()

    print()
    found_user_string = ""

    # Search for the player info JSON. Wish this was in its own file, but whatever.
    for line in open(log_location).readlines():
        if line.startswith('===> {"code":0,"user"'):
            found_user_string = line
            break
    
    found_user_string = found_user_string[4:].strip()
    playerlog = json.loads(found_user_string)["user"]
    card_inventory = playerlog["cards"]

    for deck in playerlog["decks"]:
        card_ids = ""
        print(f"Deck #{deck['index'] + 1}: {deck['name']}")
        for card in deck["cards"]:
            for base_card in card_inventory:
                if base_card["_id"] == card:
                    card_ids += str(base_card["cardid"])
                    
        print("https://friendsvsfriends.help/?deck=" + card_ids + "\n")
    


if __name__ == "__main__":
    main()