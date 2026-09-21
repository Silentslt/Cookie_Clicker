score = 0
def click_cookie(score_label):
    global score
    score += 1
    score_label.config(text=f"Cookies:{score}")