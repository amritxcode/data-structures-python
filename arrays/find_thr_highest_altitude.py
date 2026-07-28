gain = [-5,1,5,0,-7]

max_altitude = 0
current_altitude = 0

for i in gain:
    current_altitude += i
    if current_altitude >= max_altitude:
        max_altitude = current_altitude

return max_altitude