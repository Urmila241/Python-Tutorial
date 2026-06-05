import time 
import sys
def print_lyrics():
    lyrics=[
        "Main ab kyun hosh m ata nhi?",
        "Sukoon yeh dil kyun pata nhi?",
        "Kyun torun khud se jo thy waady",
        "KE ab ye ishq nibhana nhi?",
        "Main morun tum se jo ye chehra",
        "Dobara nazar milana nhi",
        "Yeh duniya jany mera dard",
        "Tuje yeh kyun nazar ata nhi?"
    ]
    delays=[
        0.3,0.3,0.4,0.3,0.3,0.3,0.8
    ]
    print("Pal Pal : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()