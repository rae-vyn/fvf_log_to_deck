import json

def main():
    print("### FVF DECK CONVERTER ###")
    print("Uses your player.log file to snag your decks and turns them into deck sharing links.")
    print("Enter your player.log file location: ")
    log_location = input()
    print()
    found_user_string = ""
    for line in open(log_location).readlines():
        if line.startswith('===> {"code":0,"user"'):
            found_user_string = line
            break
    
    found_user_string = found_user_string[4:].strip()
    playerlog = json.loads(found_user_string)["user"]
    for deck in playerlog["decks"]:
        card_ids = []
        print(f"Deck #{deck['index'] + 1}: {deck['name']}")
        for card in deck["cards"]:
            for card_inv in playerlog["cards"]:
                if card_inv["_id"] == card:
                    card_ids.append(str(card_inv["cardid"]))
    
        print("https://friendsvsfriends.help/?deck=" + ".".join(card_ids))
        print()
    return 0


if __name__ == "__main__":
    main()