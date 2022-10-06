## Files
มีทั้งหมด 5 ไฟล์ ประกอบไปด้วย
1. app_get_message.py       เป็น console app สำหรับทดสอบส่งข้อมูล
2. app_publish_message.py   เป็น console app สำหรับรอรับข้อมูล
3. index.html               เป็น html ไฟล์
4. index.py                 สำหรับควบคุม html ไฟล์
5. ws.py                    เป็น websocket server

## Requirements
* python3
* redis https://redis.io/docs/getting-started/installation/
* หรือใช้ redis บน docker docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
* ติดตั้ง pip packages ที่จำเป็นด้วยคำสั่ง
> pip install -r requirements.txt

## Usage
1. เปิดใช้งาน websocket server  ด้วยคำสั่ง
> python3 ws.py
2. เปิดใช้งาน web ด้วยคำสั่ง
> python3 -m http.server 8080
3. เปิดใช้งาน app เพื่อรอรับข้อมูล ด้วยคำสั่ง (Optional) 
> python3 app_get_message.py
4. เปิดใช้งาน app เพื่อทดสอบส่งข้อมูล
> python3 app_publish_message.py

