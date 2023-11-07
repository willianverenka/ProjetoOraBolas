def exportarRobo(x_robo, y_robo):
    with open("./orabolas-godot/trajetoria_robo.txt", "w") as file:
        t = 0.02
        for x, y in zip(x_robo, y_robo):
            file.write(f"{t:.2f}\t{x}\t{y}\n")
            t += 0.02