import csv

# Coba import dua-duanya
try:
    import whois
except ImportError:
    import python_whois as whois

INPUT_FILE = "domains.txt"
OUTPUT_FILE = "result.csv"

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        registrar = w.registrar if hasattr(w, "registrar") else "N/A"
        creation_date = w.creation_date if hasattr(w, "creation_date") else "N/A"
        expiration_date = w.expiration_date if hasattr(w, "expiration_date") else "N/A"

        # Jika berupa list → ambil yang pertama
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        return {
            "domain": domain,
            "registrar": registrar,
            "creation_date": creation_date,
            "expiration_date": expiration_date
        }
    except Exception as e:
        return {
            "domain": domain,
            "registrar": f"Error: {str(e)[:30]}",  # potong biar pendek
            "creation_date": "N/A",
            "expiration_date": "N/A"
        }

def main():
    with open(INPUT_FILE, "r") as f:
        domains = [line.strip() for line in f if line.strip()]

    results = []
    for domain in domains:
        print(f"Checking {domain}...")
        info = get_whois_info(domain)
        results.append(info)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["domain", "registrar", "creation_date", "expiration_date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Hasil disimpan di {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
