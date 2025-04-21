import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        df = df[df["Judul Paper"].notna()]  
        print("Kolom dalam file Excel:", df.columns.tolist())
        return df.to_dict('records')
    except Exception as e:
        print(f"Gagal membaca file Excel: {e}")
        return []


def linear_search(data, key, target):
    results = []
    for item in data:
        if str(item.get(key, '')).lower() == str(target).lower():
            results.append(item)
    return results

def binary_search(data, key, target):
    sorted_data = sorted(data, key=lambda x: str(x.get(key, '')).lower())
    low = 0
    high = len(sorted_data) - 1
    target = str(target).lower()
    results = []

    while low <= high:
        mid = (low + high) // 2
        mid_val = str(sorted_data[mid].get(key, '')).lower()

        if mid_val == target:
            results.append(sorted_data[mid])
            
            i = mid - 1
            while i >= 0 and str(sorted_data[i].get(key, '')).lower() == target:
                results.append(sorted_data[i])
                i -= 1
            i = mid + 1
            while i < len(sorted_data) and str(sorted_data[i].get(key, '')).lower() == target:
                results.append(sorted_data[i])
                i += 1
            break
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return results

if __name__ == "__main__":
    file_path = r"Struktur_Data_Dataset_Kelas_A_B_C (1).xlsx"
    data = load_data(file_path)

    if not data:
        print("Tidak ada data yang bisa diproses.")
        exit()

    print("\nPilih metode pencarian:")
    print("1. Linear Search")
    print("2. Binary Search")
    metode = input("Masukkan pilihan (1/2): ")

    print("\nPilih kriteria pencarian:")
    print("1. Judul")
    print("2. Tahun")
    print("3. Penulis")
    kriteria = input("Masukkan pilihan (1/2/3): ")

    
    key_map = {"1": "Judul Paper", "2": "Tahun Terbit", "3": "Nama Penulis"}
    key = key_map.get(kriteria)

    if not key:
        print("Kriteria tidak valid.")
        exit()

    target = input(f"Masukkan {key} yang ingin dicari: ")

    print("\nDEBUG:")
    print(f"Key: {key}")
    print(f"Target: {target}")
    print("Contoh data:", data[0])

    if key not in data[0]:
        print(f"Kolom '{key}' tidak ditemukan dalam data.")
    else:
        
        if metode == "1":
            hasil = linear_search(data, key, target)
        elif metode == "2":
            hasil = binary_search(data, key, target)
        else:
            print("Metode pencarian tidak valid.")
            exit()

        print("\nHasil Pencarian:")
        if hasil:
            for item in hasil:
                print(item)
        else:
            print("Data tidak ditemukan.")
