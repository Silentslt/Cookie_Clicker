import playerdata

player_data = playerdata.load_data()

def click_cookie(score_label, level_label):
    amount = playerdata.get_click_value(player_data)
    playerdata.update_score(player_data, amount)
    score_label.config(text=f"Cookies: {player_data['total_score']}")
    level_label.config(text=f"Level: {player_data['Level']}")

def upgrade_level(level_label, score_label):
    success = playerdata.next_level(player_data)
    if success:
        level_label.config(text=f"Level: {player_data['Level']}")
        score_label.config(text=f"Cookies: {player_data['total_score']}")
    else:
        cost = playerdata.get_upgrade_cost(player_data)
        if cost is None:
            print("Already at max")
        else:
            print(f"Not enough cookies.")