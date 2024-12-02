def get_game_pulls(game):
    pulled_cubes_list = []
    red_count = 0
    blue_count = 0
    green_count = 0
    game_pulls = (game.strip().split(":")[1]).strip().split(";")
    for p in game_pulls:
        color_pulls = p.strip().split(",")
        for pull in color_pulls:
            count, color = pull.strip().split(" ")
            match color:
                case "red":
                    red_count = int(count)
                case "blue":
                    blue_count = int(count)
                case "green":
                    green_count = int(count)
            pulled_cubes = {
                "red": red_count,
                "blue": blue_count,
                "green": green_count
            }
            pulled_cubes_list.append(pulled_cubes)

    return pulled_cubes_list
    

##############################
# Part 1
##############################
total_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def part1(filename):
    game_ids = []
    with open(filename) as file:
        for line in file:
            possible = True
            game_id = (line.strip().split(":")[0]).split(" ")[1]
            pulled_cubes_list = get_game_pulls(line)
            for pulled_cubes in pulled_cubes_list:
                if pulled_cubes["red"] > total_cubes["red"]:
                    possible = False
                if pulled_cubes["green"] > total_cubes["green"]:
                    possible = False
                if pulled_cubes["blue"] > total_cubes["blue"]:
                    possible = False
            if possible: 
                game_ids.append(int(game_id))
    return sum(game_ids)

value = part1("input.txt")
print("Part 1: " + str(value))

##############################
# Part 2
##############################
def part2(filename):
    power_list = []
    with open(filename) as file:
        for line in file:
            needed_ball_count = {"red": 0, "blue": 0, "green": 0}
            
            pulled_cubes_list = get_game_pulls(line)
            for pulled_cubes in pulled_cubes_list:
                if pulled_cubes["red"] > needed_ball_count["red"]:
                    needed_ball_count["red"] = pulled_cubes["red"]

                if pulled_cubes["green"] > needed_ball_count["green"]:
                    needed_ball_count["green"] = pulled_cubes["green"]
                    
                if pulled_cubes["blue"] > needed_ball_count["blue"]:
                    needed_ball_count["blue"] = pulled_cubes["blue"]

            power = needed_ball_count["red"]*needed_ball_count["blue"]*needed_ball_count["green"]
            power_list.append(power)
    
    return sum(power_list)

value = part2("input.txt")
print("Part 2: " + str(value))