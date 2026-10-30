def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

test_cases = [59, 60, 61]
expected_results = ["Tidak lulus", "Lulus", "Lulus"]

print("=== PENGUJAN BUG BATAS KELULUSAN ===")
for nilai, expected in zip(test_cases, expected_results):
    actual = status_lulus(nilai)
    status = "PASS" if actual == expected else "FAIL"
    print(f"Input: {nilai} | Expected: {expected} | Actual: {actual} | Status: {status}")