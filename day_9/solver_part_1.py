with open("input.txt", "r") as f:
    disk_map = f.read().strip()


# Example
# disk_map = "2333133121414131402"

disk_map = [int(i) for i in disk_map]

start = 0

if len(disk_map) % 2 == 0:
    end = len(disk_map) - 2
else:
    end = len(disk_map) - 1

checksum = 0

id = 0
position = 0

while start <= end:
    if start % 2 == 0:
        id = start // 2
        for i in range(disk_map[start]):
            checksum += position * id
            position += 1
        disk_map[start] = 0
        start += 1

    else:
        id = end // 2 + (end % 2)
        if disk_map[end] == disk_map[start]:
            n_ids = disk_map[end]
            disk_map[end] = 0
            disk_map[start] = 0
            end -= 2
            start += 1
        elif disk_map[end] < disk_map[start]:
            n_ids = disk_map[end]
            disk_map[start] -= disk_map[end]
            disk_map[end] = 0
            end -= 2
        else:
            n_ids = disk_map[start]
            disk_map[end] -= disk_map[start]
            disk_map[start] = 0
            start += 1
        for i in range(n_ids):
            checksum += position * id
            position += 1

print(checksum)
