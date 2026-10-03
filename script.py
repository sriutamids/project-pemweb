import requests
import pandas as pd

# TAHAP 1: MENGAMBIL DATA API

url = "https://dummyjson.com/users?limit=100"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    users = data["users"]

    df = pd.DataFrame(users)

    df = df[
        [
            "id",
            "firstName",
            "lastName",
            "username",
            "email",
            "phone"
        ]
    ]

    print("Jumlah data:", len(df))

else:
    print("Gagal mengambil data.")
    exit()

# TAHAP 2 & 3: GENERATE HTML

html = """
<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Data Pengguna</title>

    <!-- Bootstrap 5 -->
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet">
</head>

<body>

<div class="container mt-5">

    <h1 class="text-center">
        Data Pengguna
    </h1>

    <p class="text-center text-muted">
        Data pengguna yang diperoleh dari API publik.
    </p>

    <table class="table table-striped table-bordered table-hover">

        <thead class="table-dark">
            <tr>
                <th>ID</th>
                <th>Nama</th>
                <th>Username</th>
                <th>Email</th>
                <th>Telepon</th>
            </tr>
        </thead>

        <tbody>
"""

# Looping data dari DataFrame
for index, row in df.iterrows():

    html += f"""
            <tr>
                <td>{row['id']}</td>
                <td>{row['firstName']} {row['lastName']}</td>
                <td>{row['username']}</td>
                <td>{row['email']}</td>
                <td>{row['phone']}</td>
            </tr>
"""


html += """
        </tbody>

    </table>

</div>

</body>
</html>
"""


# MENYIMPAN FILE HTML

with open("hasil_generate.html", "w", encoding="utf-8") as file:

    file.write(html)

print("hasil_generate.html berhasil dibuat!")