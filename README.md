# Yapay Zeka Tabanlı Temassız Ses Yönetim Sistemi 🖐️🔊

Bu proje, insan-bilgisayar etkileşimini optimize etmek amacıyla geliştirilmiş, gerçek zamanlı bir bilgisayarlı görü uygulamasıdır. Kullanıcıların kameraya gösterdiği el hareketleriyle bilgisayarın ses seviyesini temassız yönetmesini sağlar.

## Öne Çıkan Mühendislik Yaklaşımları

* **Donanım Bağımsızlığı:** Ses kartı sürücülerinin hata risklerini ortadan kaldırmak için, evrensel klavye tetikleyicilerini (`PyAutoGUI`) simüle eden bir tersine mühendislik mimarisi tercih edilmiştir.
* **CPU Optimizasyonu:** İşlemci yükünü azaltmak amacıyla sadece işlevsel olan baş parmak (ID 4) ve işaret parmağı (ID 8) uç noktaları filtrelenerek matematiksel analize dahil edilmiştir.
* **Hassasiyet Filtresi:** El titremelerinden kaynaklanan kararsız tetiklenmeleri önlemek adına bir hassasiyet eşiği (`threshold > 8`) entegre edilmiştir.

## Kullanılan Teknolojiler
* Python 3.12, OpenCV (cv2), cvzone Hand Tracking Module, PyAutoGUI, Math