import pygame
import sys
import textwrap

# Inisialisasi pygame
pygame.init()

# Ukuran layar
lebar, tinggi = 900, 500
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("🎓 Strategi Kesiapan Ujian Praktik")

# Warna
putih = (255, 255, 255)
hitam = (30, 30, 30)
biru_muda = (135, 206, 250)
hijau_muda = (170, 240, 180)
kuning_lembut = (255, 245, 180)
pink_lembut = (255, 200, 220)
ungu_lembut = (210, 180, 255)
abu = (235, 235, 235)

# Font
font = pygame.font.SysFont("arialrounded", 26)
font_kecil = pygame.font.SysFont("arialrounded", 20)
font_judul = pygame.font.SysFont("comic sans ms", 36, bold=True)

# Pertanyaan
pertanyaan_list = [
    {
        "soal": "Apa hal pertama yang harus dilakukan sebelum ujian praktik dimulai?",
        "opsi": ["Menyiapkan alat dan bahan yang diperlukan", "Bermain dulu agar tidak tegang", "Menunggu guru memanggil"],
        "benar": 0
    },
    {
        "soal": "Mengapa penting membaca petunjuk ujian praktik terlebih dahulu?",
        "opsi": ["Agar tahu langkah-langkah dan aturan ujian", "Supaya terlihat sibuk", "Karena disuruh teman"],
        "benar": 0
    },
    {
        "soal": "Sikap apa yang harus ditunjukkan saat mempersiapkan ujian praktik?",
        "opsi": ["Santai saja tanpa latihan", "Serius dan penuh tanggung jawab", "Menunda-nunda persiapan"],
        "benar": 1
    },
    {
        "soal": "Mengapa menjaga kebersihan alat sebelum ujian penting?",
        "opsi": ["Agar hasil ujian lebih rapi dan higienis", "Agar alat terlihat baru", "Agar guru senang saja"],
        "benar": 0
    },
    {
        "soal": "Apa manfaat berlatih lebih dulu sebelum ujian praktik?",
        "opsi": ["Meningkatkan keterampilan dan percaya diri", "Membuang waktu", "Membuat lelah"],
        "benar": 0
    },
    {
        "soal": "Bagaimana cara mengatur waktu agar ujian praktik berjalan lancar?",
        "opsi": ["Mengerjakan sesuai langkah dan waktu yang ditentukan", "Melakukan semua langkah sekaligus", "Mengabaikan petunjuk waktu"],
        "benar": 0
    },
    {
        "soal": "Apa yang sebaiknya dilakukan jika alat ujianmu rusak?",
        "opsi": ["Segera melapor pada guru pengawas", "Meninggalkan ujian", "Meminjam tanpa izin"],
        "benar": 0
    },
    {
        "soal": "Mengapa kerja sama dengan teman penting dalam ujian praktik kelompok?",
        "opsi": ["Agar tugas cepat selesai dan hasil lebih baik", "Agar bisa bersantai", "Supaya orang lain bekerja sendiri"],
        "benar": 0
    },
    {
        "soal": "Bagaimana cara menenangkan diri sebelum ujian praktik?",
        "opsi": ["Bernapas dalam-dalam dan fokus pada persiapan", "Bermain HP sampai mulai", "Mengobrol keras dengan teman"],
        "benar": 0
    },
    {
        "soal": "Apa yang harus dilakukan setelah ujian praktik selesai?",
        "opsi": ["Membersihkan area kerja dan merapikan alat", "Langsung keluar tanpa membereskan", "Meninggalkan alat di meja"],
        "benar": 0
    }
]

# Variabel game
tahap = "mulai"
index_pertanyaan = 0
skor = 0
pesan_feedback = ""

# Fungsi membungkus teks panjang agar tidak keluar kolom
def bungkus_teks(teks, font, max_width):
    wrapped_lines = []
    for line in textwrap.wrap(teks, width=50):  # 50 kata per baris kira-kira pas 400–500px
        wrapped_lines.append(font.render(line, True, hitam))
    return wrapped_lines

# Fungsi menggambar background
def gambar_background():
    pygame.draw.rect(layar, biru_muda, (0, 0, lebar, tinggi // 2))
    pygame.draw.rect(layar, hijau_muda, (0, tinggi // 2, lebar, tinggi // 2))
    pygame.draw.circle(layar, kuning_lembut, (80, 80), 40)

# Fungsi karakter lucu
def gambar_karakter():
    pygame.draw.ellipse(layar, pink_lembut, (150, 270, 100, 120))
    pygame.draw.circle(layar, putih, (180, 300), 12)
    pygame.draw.circle(layar, putih, (210, 300), 12)
    pygame.draw.circle(layar, hitam, (180, 300), 5)
    pygame.draw.circle(layar, hitam, (210, 300), 5)

# Fungsi tombol
def gambar_tombol(teks, x, y, warna):
    pygame.draw.rect(layar, warna, (x, y, 400, 45), border_radius=15)
    pygame.draw.rect(layar, hitam, (x, y, 400, 45), 2, border_radius=15)
    lines = bungkus_teks(teks, font_kecil, 380)
    offset_y = y + 10
    for line in lines:
        layar.blit(line, (x + 20, offset_y))
        offset_y += 22

# Loop utama
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if tahap == "mulai":
                tahap = "kuis"

            elif tahap == "kuis":
                if index_pertanyaan < len(pertanyaan_list):
                    q = pertanyaan_list[index_pertanyaan]
                    for i in range(3):
                        btn_y = 270 + i * 70
                        if 250 < x < 650 and btn_y < y < btn_y + 45:
                            if i == q["benar"]:
                                pesan_feedback = "✅ Jawabanmu benar!"
                                skor += 1
                            else:
                                pesan_feedback = "❌ Jawaban kurang tepat."
                            index_pertanyaan += 1
                            pygame.time.wait(400)
                            if index_pertanyaan >= len(pertanyaan_list):
                                tahap = "hasil"
                            break

    # Tampilan layar
    layar.fill(putih)
    gambar_background()
    gambar_karakter()

    if tahap == "mulai":
        judul = font_judul.render("🎓 Strategi Kesiapan Ujian Praktik 🎓", True, hitam)
        layar.blit(judul, (140, 120))
        deskripsi = font.render("Bantu Mojo mempersiapkan diri menghadapi ujian praktik!", True, hitam)
        layar.blit(deskripsi, (120, 180))
        gambar_tombol("Mulai Permainan", 250, 300, ungu_lembut)

    elif tahap == "kuis":
        if index_pertanyaan < len(pertanyaan_list):
            q = pertanyaan_list[index_pertanyaan]

            # Tampilkan soal dengan pembungkus teks
            teks_soal = bungkus_teks(f"Soal {index_pertanyaan + 1}: {q['soal']}", font, 700)
            y_text = 100
            for line in teks_soal:
                layar.blit(line, (100, y_text))
                y_text += 28

            for i, opsi in enumerate(q["opsi"]):
                warna_btn = abu if i != q["benar"] else kuning_lembut
                gambar_tombol(opsi, 250, 270 + i * 70, warna_btn)

            if pesan_feedback:
                umpan = font_kecil.render(pesan_feedback, True, hitam)
                layar.blit(umpan, (100, 220))

    elif tahap == "hasil":
        pygame.draw.rect(layar, putih, (200, 150, 500, 200), border_radius=20)
        pygame.draw.rect(layar, hitam, (200, 150, 500, 200), 3, border_radius=20)
        hasil = font_judul.render("🎉 Ujian Selesai! 🎉", True, hitam)
        layar.blit(hasil, (280, 180))
        skor_teks = font.render(f"Skor Akhir: {skor} / {len(pertanyaan_list)}", True, hitam)
        layar.blit(skor_teks, (310, 240))

        if skor >= 8:
            pesan = "Kamu sangat siap menghadapi ujian praktik! 💪"
        elif skor >= 5:
            pesan = "Lumayan! Tinggal sedikit lagi latihan. 😊"
        else:
            pesan = "Ayo belajar lagi agar makin siap! 📘"

        pesan_tampil = font_kecil.render(pesan, True, hitam)
        layar.blit(pesan_tampil, (240, 290))

    pygame.display.flip()
    clock.tick(30)
