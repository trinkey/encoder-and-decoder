from random import shuffle as resetseed
seed = [i for i in open("seed.txt", "r").read().replace("\n","")]
encoder = "FUd.RhCvjwgJYbQKstaWeD,uXc7Z1Mk3LOoxB6V4liHPp8r?0A2yNEGn5TSfIz9qm!"
tempchars = "席剙刴叁屌啘勑徥墽内唲佞剆佇增壵扲咈亶婌吧拻垶召唢宏奰傯什佂亁戜抾姕噱恛卬単伓懘埔孑埛冢嵀履憾噻侩弳帣嫵愮叩叅丑况啉堿側倳妺儎孂峇勺恦"
while True:
    print("What action do you want to do?\nR: Reset seed\nL: Load seed\nE: Encode text in input.txt\nD: Decode text in input.txt\nC: Close")
    action = input("Enter the action you want to do here: ").upper()
    if action == "R":
        if input("Are you 100% SURE you want to reset the seed?\ny/n: ").lower() == "y":
            print("Resetting seed.")
            resetseed(seed)
            f = open("seed.txt", "w")
            d = ""
            for i in seed: d += i
            f.write(d)
            f.close()
            del(f, i)
            print("Seed reset to " + d)
            del(d)
        else:
            print("No longer resetting seed.")
    elif action == "L":
        newseed = [i for i in input("Please enter the new seed.\nIt should be 66 characters long, containing one of each:\nA-Z a-z 0-9 .!?,\nInput here:")]
        seedcheck = []
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.!?":
            seedcheck.append(newseed.count(i))
        if seedcheck.count(1) == 66:
            print("Valid seed")
            seed = []
            d = ""
            for i in newseed:
                d += i
                seed.append(i)
            f = open("seed.txt", "w")
            f.write(d)
            f.close()
            del(f, d, i, newseed, seedcheck)
        else:
            print("Invalid seed.")
    elif action == "E":
        print("Encoding from input.txt")
        f = open("input.txt", "r").read()
        for i in range(66):
            f = f.replace(seed[i], tempchars[i])
        for i in range(66):
            f = f.replace(tempchars[i], encoder[i])
        del(i)
        g = open("output.txt", "w")
        g.write(f)
        del(g, f)
        print("Encoded output into output.txt")
    elif action == "D":
        print("Decoding from input.txt")
        f = open("input.txt", "r").read()
        for i in range(66):
            f = f.replace(encoder[i], tempchars[i])
        for i in range(66):
            f = f.replace(tempchars[i], seed[i])
        del(i)
        g = open("output.txt", "w")
        g.write(f)
        del(g, f)
        print("Decoded output into output.txt")
    elif action == "C":
        if not input("Press enter to close, type anything to not close! "):
            break
    else:
        print("Invalid action")
    print("")