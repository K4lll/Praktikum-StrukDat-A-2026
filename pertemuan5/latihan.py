    #No1
    stok_barang = [15, 40, 30, 10, 25]
    index = stok_barang.index(10)
    print(index)
    nosatuubah = stok_barang[index] = 50
    print("ganti 10 jadi 50")
    print(stok_barang)


    stok_barang.append(5)
    print("tambah 5 diakhir")
    print(stok_barang)
    stok_barang.sort()
    stok_barang.reverse()
    print("sort dari besar ke kecil")
    print(stok_barang)

    x = sum(stok_barang)
    print(x)


    rata_rata = x / 5
    print("stok aman" if rata_rata > 20 else "waspada")

    #No 2
    data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

    for x in data_aktivitas:
        a, b = x 

        if b > 80:
            print(f"{a} mendapat prediket Gold")
        elif b > 50:
            print(f"{a} mendapat prediket silver")
        else :
            print(f"{a} mendapat prediket Bronze")

    #No 3 
    ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
    ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 

    ukm_codingaja = ukm_coding - ukm_robotik 
    print(ukm_codingaja)

    totalsemua = ukm_coding | ukm_robotik
    print(totalsemua)

    apakahada = "Andi" in ukm_robotik
    print(apakahada)

    #N04
    gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
    ]
    for x in gudang_pc:
        if x["item"] == "Keyboard":
            x ["kategori"] = "Aksesoris"

    gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 4})
    print(gudang_pc)
    
    for x in gudang_pc:
        total = x["harga"] * x["stok"]
        print(f"item : {x[item]} | Total Aset: Rp. {total}")