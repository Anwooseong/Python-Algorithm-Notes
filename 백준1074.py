def insert(xpos, ypos, count, dest_x, dest_y, size):
    ans = imsi(xpos, ypos, count, dest_x, dest_y, size)
    if ypos + 2 < size:
        count += 4
        insert(xpos, ypos + 2, count, dest_x, dest_y, size)
    if xpos + 2 < size:
        count += 4
        insert(xpos + 2, ypos, count, dest_x, dest_y, size)
    if xpos + 2 < size and ypos + 2 < size:
        count += 4
        insert(xpos + 2, ypos + 2, count, dest_x, dest_y, size)
    if dest_x-1 == xpos and dest_y-1 == ypos:
        return ans

def imsi(xpos, ypos, count, dest_x, dest_y, size):
    if ypos + 1 < size:
        count += 1
        imsi(xpos, ypos + 1, count, dest_x, dest_y, size)
    if xpos + 1 < size:
        count += 1
        imsi(xpos + 1, ypos, count, dest_x, dest_y, size)
    if xpos + 1 < size and ypos + 1 < size:
        count += 1
        imsi(xpos + 1, ypos + 1, count, dest_x, dest_y, size)
    if dest_x-1 == xpos and dest_y-1 == ypos:
        return count

N, r, c = map(int, input().split())
print(insert(0, 0, 0, r, c, 2**(N)))