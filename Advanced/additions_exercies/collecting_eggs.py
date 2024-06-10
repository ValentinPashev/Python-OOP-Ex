from collections import deque

eggs_with_size = deque(int(x) for x in input().split(", "))
piece_of_papers = deque(int(x) for x in input().split(", "))
filled_boxes = 0


while eggs_with_size and piece_of_papers:
    current_egg = eggs_with_size.popleft()
    current_paper = piece_of_papers.pop()

    if current_egg <= 0:
        piece_of_papers.append(current_paper)
        continue

    elif current_egg == 13:
        paper = piece_of_papers.popleft()
        piece_of_papers.append(paper)
        piece_of_papers.appendleft(current_paper)

    elif current_paper + current_egg <= 50:
        filled_boxes += 1


if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")

else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_with_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_with_size)}")

if piece_of_papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in piece_of_papers)}")