import speedtest

def speed_test_en():
    st = speedtest.Speedtest()

    print("Loading...")
    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {st.results.ping} ms")

if __name__ == "__main__":
    speed_test_en()
