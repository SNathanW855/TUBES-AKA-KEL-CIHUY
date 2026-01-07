from flask import Flask, render_template
import time

app = Flask(__name__)

# ================= WORD COUNT ITERATIF =================
def word_count_iterative(tweets):
    freq = {}
    for tweet in tweets:
        for w in tweet.lower().split():
            freq[w] = freq.get(w, 0) + 1
    return freq

# ================= INSERTION SORT ITERATIF =================
def insertion_sort_iterative(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][1] < key[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ================= WORD COUNT REKURSIF =================
def word_count_recursive(tweets, idx, freq):
    if idx == len(tweets):
        return
    for w in tweets[idx].lower().split():
        freq[w] = freq.get(w, 0) + 1
    word_count_recursive(tweets, idx + 1, freq)

# ================= INSERTION SORT REKURSIF =================
def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j][1] < last[1]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

# ================= ROUTE =================
@app.route("/")
def index():

    tweets = [
        "pekerja bekerja kantor",
        "mahasiswa belajar kampus",
        "warga olahraga stadion",
        "pengunjung berbelanja mall",
        "anak bermain taman",
        "pekerja rapat kantor",
        "atlet olahraga stadion",
        "mahasiswa olahraga kampus",
        "warga berbelanja mall",
        "keluarga bersantai taman",
        "komunitas olahraga stadion",
        "pekerja bekerja kantor pusat",
        "mahasiswa belajar kampus pagi",
        "warga olahraga taman kota",
        "pengunjung berbelanja mall besar",
        "anak bermain taman kota",
        "pekerja rapat kantor pusat",
        "atlet latihan stadion nasional",
        "mahasiswa olahraga kampus sore",
        "keluarga bersantai taman kota"
    ]

    loop_values = [100, 300, 500, 700, 1000]
    iter_times = []
    rec_times = []

    # ===== HITUNG RUNNING TIME ITERATIF =====
    for loop in loop_values:
        start = time.time()
        for _ in range(loop):
            freq = word_count_iterative(tweets)
            insertion_sort_iterative(list(freq.items()))
        iter_times.append((time.time() - start) * 1000)

    # ===== HITUNG RUNNING TIME REKURSIF =====
    for loop in loop_values:
        start = time.time()
        for _ in range(loop):
            freq = {}
            word_count_recursive(tweets, 0, freq)
            pairs = list(freq.items())
            insertion_sort_recursive(pairs, len(pairs))
        rec_times.append((time.time() - start) * 1000)

    # ===== HASIL ITERATIF =====
    freq_iter = word_count_iterative(tweets)
    pairs_iter = insertion_sort_iterative(list(freq_iter.items()))
    top_iter = pairs_iter[:5]

    # ===== HASIL REKURSIF =====
    freq_rec = {}
    word_count_recursive(tweets, 0, freq_rec)
    pairs_rec = list(freq_rec.items())
    insertion_sort_recursive(pairs_rec, len(pairs_rec))
    top_rec = pairs_rec[:5]

    return render_template(
        "index.html",
        iteratif=top_iter,
        rekursif=top_rec,
        loop_values=loop_values,
        iter_times=iter_times,
        rec_times=rec_times
    )

if __name__ == "__main__":
    app.run(debug=True)
