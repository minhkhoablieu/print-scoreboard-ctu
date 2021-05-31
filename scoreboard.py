import requests, stdiomask, webbrowser

URL = "http://qldt.ctu.edu.vn/htql/sinhvien/dang_nhap.php"


Username = input('MSSV: ')
Password = stdiomask.getpass()


DATA = {'txtDinhDanh': Username, 'txtMatKhau': Password}
login = requests.post(url=URL, data=DATA, verify=False)


getSc = "http://qldt.ctu.edu.vn/htql/sinhvien/qldiem/codes/HamInBangDiemSinhVien.php"

par = {
    "IN": "motso", "maxNH": "2021", "maxHK": "2", "fileIn": "HamInBangDiemSinhVien.php", "maHDDT": "CQ", "rdoInDiem": "rdoInMotSo", "cboTuNamHoc": "2019", "cboTuHocKi": "1", "cboDenNamHoc": "2021", "cboDenHocKi": "2"
}

get = requests.post(url=getSc, data=par, verify=False, cookies=login.cookies)
file = open("index.html", "wb")
file.write((get.text).encode("utf-8"))
file.close
webbrowser.open("index.html")
