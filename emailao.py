import random
import string
import time
import os
import threading
from colorama import init, Fore
from datetime import datetime, timedelta

init(autoreset=True)

# UPDATE DATABASE VỚI THỜI GIAN TÍNH BẰNG GIÂY
TEMP_EMAIL_SITES = {
    "SHORT_TERM": [
        {"name": "10MinuteMail", "domain": "10minutemail.com", "duration": 600, "quality": "⭐⭐⭐⭐⭐"},  # 10 phút
        {"name": "GuerrillaMail", "domain": "guerrillamail.com", "duration": 3600, "quality": "⭐⭐⭐⭐⭐"},  # 60 phút
        {"name": "Mailinator", "domain": "mailinator.com", "duration": 7200, "quality": "⭐⭐⭐⭐"},  # 2 giờ
        {"name": "TempMail", "domain": "temp-mail.org", "duration": 600, "quality": "⭐⭐⭐⭐"},  # 10 phút
        {"name": "MailDrop", "domain": "maildrop.cc", "duration": 86400, "quality": "⭐⭐⭐"},  # 24 giờ
        {"name": "TempMailNet", "domain": "temp-mail.net", "duration": 1200, "quality": "⭐⭐⭐"},  # 20 phút
        {"name": "MyTemp", "domain": "mytemp.email", "duration": 2700, "quality": "⭐⭐⭐"},  # 45 phút
        {"name": "QuickMail", "domain": "quick-mail.cc", "duration": 1500, "quality": "⭐⭐"},  # 25 phút
        {"name": "InstaMail", "domain": "insta-mail.com", "duration": 300, "quality": "⭐⭐"},  # 5 phút
        {"name": "FakeMail", "domain": "fake-mail.com", "duration": 7200, "quality": "⭐⭐"},  # 2 giờ
    ],
    
    "LONG_TERM": [
        {"name": "YopMail", "domain": "yopmail.com", "duration": 691200, "quality": "⭐⭐⭐⭐⭐"},  # 8 ngày
        {"name": "Disposable", "domain": "dispostable.com", "duration": 259200, "quality": "⭐⭐⭐⭐"},  # 3 ngày
        {"name": "MailTM", "domain": "mail.tm", "duration": 172800, "quality": "⭐⭐⭐⭐⭐"},  # 2 ngày
        {"name": "TempMailIO", "domain": "temp-mail.io", "duration": 432000, "quality": "⭐⭐⭐⭐"},  # 5 ngày
        {"name": "TrashMail", "domain": "trashmail.com", "duration": 604800, "quality": "⭐⭐⭐⭐"},  # 7 ngày
        {"name": "MailNesia", "domain": "mailnesia.com", "duration": 2592000, "quality": "⭐⭐⭐⭐⭐"},  # 30 ngày
        {"name": "TempMailPro", "domain": "temp-mail.pro", "duration": 604800, "quality": "⭐⭐⭐"},  # 7 ngày
        {"name": "LongTempMail", "domain": "longtempmail.com", "duration": 2419200, "quality": "⭐⭐⭐⭐"},  # 28 ngày
        {"name": "EmailTemp", "domain": "emailtemp.org", "duration": 518400, "quality": "⭐⭐⭐"},  # 6 ngày
        {"name": "PermaTemp", "domain": "permatemp.com", "duration": 1814400, "quality": "⭐⭐⭐"},  # 21 ngày
    ]
}

class AdvancedTempEmail:
    def __init__(self):
        self.generated_emails = []
        self.stats = {"short_term": 0, "long_term": 0}
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def format_duration(self, seconds):
        """Chuyển seconds sang định dạng dễ đọc"""
        if seconds < 60:
            return f"{seconds} giây"
        elif seconds < 3600:
            minutes = seconds // 60
            return f"{minutes} phút"
        elif seconds < 86400:
            hours = seconds // 3600
            return f"{hours} giờ"
        else:
            days = seconds // 86400
            return f"{days} ngày"
    
    def get_remaining_time(self, created_time, total_duration):
        """Tính thời gian còn lại"""
        elapsed = time.time() - created_time
        remaining = total_duration - elapsed
        return max(0, remaining)  # Không âm
    
    def generate_email(self, category="SHORT_TERM", custom_name=None):
        sites = TEMP_EMAIL_SITES.get(category, [])
        sites.sort(key=lambda x: x['quality'], reverse=True)
        site = sites[0] if random.random() > 0.3 else random.choice(sites[:3])
        
        if custom_name:
            username = custom_name
        else:
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            
        email = f"{username}@{site['domain']}"
        
        email_info = {
            "email": email,
            "site_name": site['name'],
            "total_duration": site['duration'],
            "duration_display": self.format_duration(site['duration']),
            "quality": site['quality'],
            "category": category,
            "created_at": time.time(),
            "created_time_display": time.strftime("%H:%M:%S - %d/%m/%Y")
        }
        
        self.generated_emails.append(email_info)
        self.stats["short_term" if category == "SHORT_TERM" else "long_term"] += 1
        
        return email_info
    
    def display_all_emails(self):
        if not self.generated_emails:
            print(Fore.RED + "❌ Chưa có email nào được tạo!")
            return
            
        print(Fore.CYAN + f"\n📧 DANH SÁCH EMAIL ({len(self.generated_emails)}):")
        print(Fore.YELLOW + "─" * 80)
        
        for i, email_info in enumerate(self.generated_emails[-10:], 1):
            category_icon = "⚡" if email_info['category'] == "SHORT_TERM" else "🐢"
            
            # Tính thời gian còn lại
            remaining = self.get_remaining_time(email_info['created_at'], email_info['total_duration'])
            remaining_display = self.format_duration(remaining)
            
            # Hiển thị trạng thái
            if remaining == 0:
                status = Fore.RED + "🛑 HẾT HẠN"
            elif remaining < 300:  # Dưới 5 phút
                status = Fore.RED + f"⏰ {remaining_display}"
            elif remaining < 1800:  # Dưới 30 phút
                status = Fore.YELLOW + f"⏳ {remaining_display}"
            else:
                status = Fore.GREEN + f"✅ {remaining_display}"
            
            print(Fore.WHITE + f" {i:2d}. {email_info['email']}")
            print(Fore.CYAN + f"     {category_icon} {email_info['duration_display']} | {status} | {email_info['quality']}")
            print(Fore.CYAN + f"     🕐 Tạo lúc: {email_info['created_time_display']}")
            
        print(Fore.YELLOW + "─" * 80)
    
    def show_stats(self):
        print(Fore.CYAN + f"\n📊 THỐNG KÊ:")
        print(Fore.WHITE + f"   ⚡ Email ngắn hạn: {self.stats['short_term']}")
        print(Fore.WHITE + f"   🐢 Email dài hạn: {self.stats['long_term']}")
        print(Fore.WHITE + f"   📧 Tổng số: {sum(self.stats.values())}")
        
        # Thống kê email còn hạn/hết hạn
        active_count = 0
        expired_count = 0
        
        for email in self.generated_emails:
            remaining = self.get_remaining_time(email['created_at'], email['total_duration'])
            if remaining > 0:
                active_count += 1
            else:
                expired_count += 1
                
        print(Fore.GREEN + f"   ✅ Còn hạn: {active_count}")
        print(Fore.RED + f"   ❌ Hết hạn: {expired_count}")
    
    def quick_generate(self, count=5):
        print(Fore.YELLOW + f"\n🚀 Đang tạo nhanh {count} email...")
        
        for i in range(count):
            category = "SHORT_TERM" if i % 2 == 0 else "LONG_TERM"
            email_info = self.generate_email(category)
            
            # Hiển thị thời gian còn lại ngay khi tạo
            remaining = self.get_remaining_time(email_info['created_at'], email_info['total_duration'])
            remaining_display = self.format_duration(remaining)
            
            print(Fore.GREEN + f" {i+1}. {email_info['email']} - ⏰ {remaining_display}")
    
    def check_expired_emails(self):
        """Kiểm tra email hết hạn"""
        expired_emails = []
        
        for email in self.generated_emails:
            remaining = self.get_remaining_time(email['created_at'], email['total_duration'])
            if remaining == 0:
                expired_emails.append(email)
                
        return expired_emails

def main():
    system = AdvancedTempEmail()
    
    while True:
        system.clear_screen()
        print(Fore.RED + """
▄▄▄█████▓ ▒█████   ▒█████   ██▓         █████▒▄▄▄       ██▀███   ███▄ ▄███▓
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██   ▒▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░       ▒████ ░▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ░▓█▒  ░░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██ 
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ░▒█░    ▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░    ▒ ░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░    ░       ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░       ░ ░     ░   ▒     ░░   ░ ░      ░   
             ░ ░      ░ ░      ░  ░                ░  ░   ░            ░   
        TEMP EMAIL v3.0 - MINHDEVTOOL
    """)
        
        # Kiểm tra email hết hạn
        expired = system.check_expired_emails()
        if expired:
            print(Fore.RED + f"⚠️  Có {len(expired)} email đã hết hạn!")
        
        print(Fore.CYAN + "🎯 CHỨC NĂNG CHÍNH:")
        print(Fore.YELLOW + " 1. ⚡ Tạo email NGẮN HẠN (Best Quality)")
        print(Fore.YELLOW + " 2. 🐢 Tạo email DÀI HẠN (Best Quality)") 
        print(Fore.YELLOW + " 3. 🚀 Tạo nhanh 5 email (Auto Mix)")
        print(Fore.YELLOW + " 4. 📊 Xem thống kê")
        print(Fore.YELLOW + " 5. 📧 Hiển thị tất cả email + THỜI GIAN CÒN LẠI")
        print(Fore.YELLOW + " 0. ❌ Thoát")
        
        choice = input(Fore.GREEN + "\n👉 Chọn chức năng (0-5): ").strip()
        
        if choice == "1":
            email_info = system.generate_email("SHORT_TERM")
            remaining = system.get_remaining_time(email_info['created_at'], email_info['total_duration'])
            print(Fore.GREEN + f"\n✅ Đã tạo: {email_info['email']}")
            print(Fore.CYAN + f"   ⚡ Thời hạn: {email_info['duration_display']} | Còn lại: {system.format_duration(remaining)}")
            print(Fore.CYAN + f"   Chất lượng: {email_info['quality']}")
            
        elif choice == "2":
            email_info = system.generate_email("LONG_TERM")
            remaining = system.get_remaining_time(email_info['created_at'], email_info['total_duration'])
            print(Fore.GREEN + f"\n✅ Đã tạo: {email_info['email']}")
            print(Fore.CYAN + f"   🐢 Thời hạn: {email_info['duration_display']} | Còn lại: {system.format_duration(remaining)}")
            print(Fore.CYAN + f"   Chất lượng: {email_info['quality']}")
            
        elif choice == "3":
            system.quick_generate(5)
            
        elif choice == "4":
            system.show_stats()
            
        elif choice == "5":
            system.display_all_emails()
            
        elif choice == "0":
            print(Fore.RED + "\n👋 Thoát hệ thống!")
            break
            
        else:
            print(Fore.RED + "❌ Lựa chọn không hợp lệ!")
        
        input(Fore.YELLOW + "\n↵ Nhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()