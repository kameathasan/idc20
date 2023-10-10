player_name = input("Enter your name: ")
total_boxes = 36

print("")
print("GAME #1: ")
print("")
opponent1 = input("Enter your opponents name: ")
your_points1 = int(input("Enter your points:"))
opp_points1 = int(input("Enter your opponent's points: "))
box_percent1 = your_points1/total_boxes

print("")
print("GAME #2: ")
print("")
opponent2 = input("Enter your opponents name: ")
your_points2 = int(input("Enter your points:"))
opp_points2 = int(input("Enter your opponent's points: "))
box_percent2 = your_points2/total_boxes

print("")
print("GAME #3: ")
print("")
opponent3 = input("Enter your opponents name: ")
your_points3 = int(input("Enter your points:"))
opp_points3 = int(input("Enter your opponent's points: "))
box_percent3 = your_points3/total_boxes

print("")
print("GAME #4: ")
print("")
opponent4 = input("Enter your opponents name: ")
your_points4 = int(input("Enter your points:"))
opp_points4 = int(input("Enter your opponent's points: "))
box_percent4 = your_points4/total_boxes

print("")
print("GAME #5: ")
print("")
opponent5 = input("Enter your opponents name: ")
your_points5 = int(input("Enter your points:"))
opp_points5 = int(input("Enter your opponent's points: "))
box_percent5 = your_points5/total_boxes

print("")
print("")
print("Dots and Boxes Score Tracker")
print(f"Players name: {player_name}")
print("")
print("")
print(f"{'Opponent':<10} {'Your Points':>10} {' Opponent Points':>11} {'Box %':>14}")
print(f"======================================================")
print(f"{opponent1:<10} {your_points1:>10} {opp_points1:>17} {box_percent1:>13.2%}")
print(f"{opponent2:<10} {your_points2:>10} {opp_points2:>17} {box_percent2:>13.2%}")
print(f"{opponent3:<10} {your_points3:>10} {opp_points3:>17} {box_percent3:>13.2%}")
print(f"{opponent4:<10} {your_points4:>10} {opp_points4:>17} {box_percent4:>13.2%}")
print(f"{opponent5:<10} {your_points5:>10} {opp_points5:>17} {box_percent5:>13.2%}")
print(f"======================================================")