import random

def initialize_boxes():
    return [random.randint(1, 7) for _ in range(3)]

def move_boxes(boxes):
    for i in range(len(boxes)):
        boxes[i] = random.randint(1, 7)

def check_cargo(boxes):
    return sum(boxes) == 713

def main():
    print("Welcome to the Martian Cargo Locator Program!")

    boxes = initialize_boxes()

    while True:
        print("\nEnter the kilometer mark for each box:")
        for i in range(1, 4):
            kilometer_mark = int(input(f"Box {i}: "))
            if kilometer_mark in boxes:
                print(f"Box {i} found at {kilometer_mark} km!")
            else:
                print(f"No box found at {kilometer_mark} km. Boxes are moving!")

                # Simulate box movement
                move_boxes(boxes)

                break
        else:
            if check_cargo(boxes):
                print("\nCongratulations! You found all the boxes with the Martian cargo.")
                break
            else:
                print("\nWeight of the found boxes is not 713 kg. Try again.")

if __name__ == "__main__":
    main()
