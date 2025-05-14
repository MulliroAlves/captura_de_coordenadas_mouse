from pynput import mouse

clicks = []

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clique {len(clicks) + 1}: X={x}, Y={y}")
        clicks.append((x, y))

        if len(clicks) >= 7:
            # Encerra o listener após 5 cliques
            return False

print("Clique com o mouse 5 vezes para capturar as posições...")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print("\nCoordenadas capturadas:")
for i, (x, y) in enumerate(clicks, 1):
    print(f"{i}. X={x}, Y={y}")
