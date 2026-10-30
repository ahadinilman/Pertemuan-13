def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)

test_data = [
    [80, 90, 70],        
    [100, 80],           
    [],                  
    [80, 60, 90, 70, 50]
]

print("=== PENGUJIAN FUNGSI RATA-RATA ===")
for i, data in enumerate(test_data, 1):
    hasil = rata_rata(data)
    print(f"Test {i} | Input: {data} -> Rata-rata: {hasil}")