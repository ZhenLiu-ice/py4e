largest_so_far = smallest_so_far = None
while True:
    num = input("Enter a number:")
    if num == "done":
        print("Maximum is", largest_so_far)
        print("Minimum is", smallest_so_far)
        break

    try:
        num = int(num)
        if largest_so_far is None:
            largest_so_far = smallest_so_far = num
        elif num > largest_so_far:
            largest_so_far = num
        elif num < smallest_so_far:
            smallest_so_far = num
    except Exception:
        print("Invalid input")
        continue
