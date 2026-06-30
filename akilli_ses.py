import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import pyautogui

print("Sistem baslatiliyor, lutfen bekleyin...")

# 1. Yeni ve Hatasız El Dedektörünü Başlatıyoruz
dedektor = HandDetector(detectionCon=0.8, maxHands=1)

# 2. Kamerayı Açıyoruz
kamera = cv2.VideoCapture(0)

# Değişim takibi için eski mesafe değerini tutuyoruz
eski_mesafe = 0

print("\nKamera aciliyor! Kapatmak icin 'q' tusuna basin.")

while True:
    kontrol, kare = kamera.read()
    if not kontrol:
        break
        
    kare = cv2.flip(kare, 1)
    
    # El eklemlerini bul ve çiz
    eller, kare = dedektor.findHands(kare)
    
    if eller:
        el = eller[0]
        lmList = el["lmList"]
        
        # Baş parmak ucu ve İşaret parmak ucu
        x1, y1 = lmList[4][0], lmList[4][1]
        x2, y2 = lmList[8][0], lmList[8][1]
        
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        # Parmak uçlarına daire çizelim
        cv2.circle(kare, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(kare, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(kare, (x1, y1), (x2, y2), (255, 0, 0), 3)
        
        # İki parmak arası mesafeyi hesapla
        mesafe = math.hypot(x2 - x1, y2 - y1)
        
        # Hatalı basımları engellemek için küçük bir eşik kontrolü (Hassasiyet ayarı)
        if abs(mesafe - eski_mesafe) > 8:
            if mesafe > 130:
                # Parmaklar çok açıksa klavyeden 'Ses Açma' tuşuna bas
                pyautogui.press("volumeup")
            elif mesafe < 60:
                # Parmaklar çok yakınsa klavyeden 'Ses Kısma' tuşuna bas
                pyautogui.press("volumedown")
                
            eski_mesafe = mesafe
        
        # Parmaklar tamamen birleştiğinde ortada kırmızı bir nokta çıksın
        if mesafe < 35:
            cv2.circle(kare, (cx, cy), 12, (0, 0, 255), cv2.FILLED)
            
    cv2.imshow("Yapay Zeka ile Kesintisiz Ses Kontrolu", kare)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()