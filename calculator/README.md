# เครื่องคิดเลข Python

เดโมเว็บเครื่องคิดเลขสำหรับคลาส Docker ใช้ Python 3.12 และ Flask ตาม `requirements.txt`

## กิจกรรมแรก: ลองรันก่อนติดตั้ง dependencies

```sh
python main.py
```

ถ้าใช้ macOS/Linux อาจต้องใช้ `python3 main.py` เปิด `http://localhost:5000` หาก error ให้จดข้อความไว้เพื่อใช้ในคลาส

## รันตามปกติหลังจบกิจกรรม

แนะนำใช้ virtual environment แล้วติดตั้ง:

```sh
python -m pip install -r requirements.txt
python main.py
```

## Docker (ครูใช้เตรียม image)

```sh
docker build -t de-calculator:1 .
docker run -d --name de-calculator -p 127.0.0.1:5000:5000 de-calculator:1
```

เปิด `http://localhost:5000` แอพใช้ Flask development server สำหรับสาธิตในคลาส ไม่มีฐานข้อมูลหรือประวัติการคำนวณ
