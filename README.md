# Whois-Lookup-Automator-Python-
## Cara install
1. Clone repository ini:
# passive-recon-whois


Skrip Python untuk melakukan WHOIS lookup sederhana dari daftar domain (file `domains.txt`) dan menyimpan ringkasan (registrar, creation_date, expiration_date) ke `result.csv`.

## Fitur
- Baca daftar domain dari `domains.txt` (satu domain per baris)
- Lakukan WHOIS query tiap domain (memakai paket `python-whois`)
- Simpan ringkasan ke CSV (`result.csv`)
- Fallback import detection (coba `python_whois` bila perlu)


```bash
git clone https://github.com/<username>/passive-recon-whois.git
cd passive-recon-whois
