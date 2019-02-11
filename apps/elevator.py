def elevator(left, right, call):
    return "left" if abs(call - left) < abs(call - right) else "right"

print(elevator(1,2,0))