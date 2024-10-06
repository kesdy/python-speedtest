import speedtest

def speed_test_tr():
    st = speedtest.Speedtest()

    print("Yükleniyor...")
    st.get_best_server()

    print("İndirme testi yapılıyor...")
    download_speed = st.download() / 1_000_000  # Mbps cinsine dönüştür
    upload_speed = st.upload() / 1_000_000      # Mbps cinsine dönüştür

    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    print(f"Ping: {st.results.ping} ms")

if __name__ == "__main__":
    speed_test_tr()
