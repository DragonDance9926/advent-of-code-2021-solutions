xmin = 236
xmax = 262
ymin = -78
ymax = -58

def simulate(dx, dy, target_x_min, target_x_max, target_y_min, target_y_max):
  x = 0
  y = 0
  max_y = 0
  while True:
    x += dx
    y += dy
    max_y = max(max_y, y)
    dx = max(dx-1, 0)
    dy -= 1
    if target_x_min <= x <= target_x_max and target_y_min <= y <= target_y_max:
      return True
    if dy < 0 and y < target_y_min:
      return False


works_count = 0
for x in range(300):
  for y in range(ymin, 300):
    if simulate(x,y, xmin, xmax, ymin, ymax ):
      works_count += 1
print(works_count)