with open("dataset_24465_4 (4).txt") as f, open("text.txt", "w") as w:
    list=f.read().splitlines()
    print(list)
    w.write("\n".join(list[::-1]))
