choiceList = ("s", "w", "g")


def game(choices):
    import random
    cpu = random.choice(choices)
    player = input("CPU selected something. Your turn (s/w/g): ")

    if player != 's' and player != 'w' and player != 'g':
        return -1, -1

    player_score = 0
    cpu_score = 0
    if cpu == player:
        player_score = 0
        cpu_score = 0
    elif cpu == 's':
        if player == 'w':
            cpu_score += 1
        elif player == 'g':
            player_score += 1
    elif cpu == 'w':
        if player == 's':
            player_score += 1
        elif player == 'g':
            cpu_score += 1
    elif cpu == 'g':
        if player == 's':
            cpu_score += 1
        elif player == 'w':
            player_score += 1

    print(f"Reveal: CPU had selected = {cpu}")

    return player_score, cpu_score


def game_play():
    print("Snake Water Gun game")
    player_score = []
    cpu_score = []

    count = 0
    while count < 10:
        player, cpu = game(choiceList)
        if player == -1 and cpu == -1:
            print("Your input has been discarded. Please enter only s / w / g")
            continue
        player_score.append(player)
        cpu_score.append(cpu)
        count += 1

    player_total = sum(player_score)
    cpu_total = sum(cpu_score)

    return player_total, cpu_total

def initiate_game():
    player, cpu = game_play()
    print(f"Your total score = {player} and CPU's total score = {cpu}")
    if player > cpu:
        print("You won")
    elif player < cpu:
        print("You lost")
    else:
        print("It's draw")


initiate_game()
