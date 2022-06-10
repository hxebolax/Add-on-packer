# NVDA Eklentileri için Yardımcı Araçlar Kılavuzu:

Bu eklenti, yüklenecek, kaldırılacak ve zaten yüklü eklentilerimiz için bir yardımcı araç paketi olmaya çalışır.  

Farklı alanlarda, eklentilerimize toplu bir şekilde işlemler yapma imkanı vererek ve eklenti yöneticisinde olduğu gibi tek tek gitmek zorunda kalmadan mümkün olduğunca hızlı olmaya çalışıyoruz.  

Halihazırda yeni özellikler olarak eklenen alanlar, farklı sürümlerde iyileştirilecektir.  

Bu eklenti, NVDA>Araçlar>NVDA eklentileri için yardımcı araçlar yolunu takip ederek çalıştırılır.  

Eklenti, hızlı kullanım için atanmış bir kısayol tuşuna sahip değildir.  

Girdi hareketleri iletişim kutusunda, NVDA eklentileri için yardımcı araçlar başlığı altından eklenebilir.  

## sorumluluk reddi:

Eklentinin kullanımından son kullanıcı sorumludur.  

Her şeyin mümkün olduğunca güvenilir olması amaçlanmıştır, ancak sorunlar her zaman ortaya çıkabilir, bu nedenle tamamlayıcı yazarı bu eklentinin kullanımından kaynaklanan herhangi bir sorundan sorumlu olmayacaktır.  

# Genel açıklama:

Uygulama 3 bölümde ele alınmaktadır.  

* Birinci bölüm: Kullanmak istediğimiz kategoriyi seçebileceğimiz liste. Eklentiyi her açtığımızda imleç bu listeye odaklanır.
Bu listede yukarı ve aşağı hareket etmeliyiz.
* İkinci bölüm: Seçtiğimiz kategorinin içeriğini gösteren alandır.
Bu alan kategoriye göre değişmektedir. Kategorilerin açıklaması daha sonra verilecektir.
Kısayol tuşları veya sekme  ile kategorilere erişebiliriz.
* Üçüncü bölüm: Bu bölüm, herhangi bir işlem yapıldığında etkinleştirilecek ve kullanıcıya neler olduğu hakkında bilgi veren bir düzenleme kutusu içerir. Kullanıcı ayrıca tüm işlemlerde bir ilerleme çubuğu ile bilgilendirilir.

Seçtiğimiz kategoriye bağlı olarak butonlar ve bir kapat tuşu içerir.

Güncel bir işlem olmadığı sürece eklenti Escape, Alt+F4 ile kapatılabilir veya Kapat düğmesine sekme ile gelerek de kapatılabilir.

## Eklenti paketleyici:

Sekme ile listeye gelip bu kategoriyi seçersek, yüklediğimiz tüm eklentilerin etkin, devre dışı veya desteklenmemesine bakılmaksızın sıralandığı bir listeye erişiriz.  

Alt+L ile de hızlı bir şekilde erişebildiğimiz bu listede seçmek istediğimiz tüm eklentileri boşluk bırakarak seçip seçtiğimiz bir dizine yedekleyebiliriz.  

Her eklenti kendi adı, sürümü ve “_gen” tanımlayıcısı ile oluşturulacaktır, oluşturulan bu eklentiler diğer NVDA kullanıcıları tarafından sorunsuz bir şekilde kurulabilir.  

Seç adlı butonun üzerine sekme tuşu ile gelip boşluk çubuğu ile etkinleştirdiğimizde: Tümünü seç ve Seçimi temizle seçeneklerini görüyoruz. Aynı içeriğe ALT+S kısayolu ile de erişebiliriz.  

Yine tab ile üzerine gelerek veya ALT+O kısayolu kullanılarak Oluştur butonu etkinleştirildiğinde, Dosya kaydetme penceresi açılır ve bir dizin seçmemiz istenir.  

Dizin seç ile belirttiğimiz konumu onayladıktan sonra, listeden seçtiğimiz eklentinin paketlenme işlemi başlayacaktır. Bu esnada, aşamaların erişilebilir şekilde gösterildiği bir kutu ekrana gelecek ve penceredeki diğer bütün butonlar işlem tamamlanana kadar devre dışı bırakılacaktır.  

İşlem tamamlandıktan sonra, bize bildirilir ve olumlu veya olumsuz bilgiler sunulur. ALT+B ile Kabul et tıklanarak pencere kapatılır.  

Eklenti oluşturma işleminin gerçekleştirilebilmesi için, listeden en az bir eklentinin seçili olması gerekir. Aksi taktirde, bir mesaj ile kullanıcı uyarılacaktır.  

## Çoklu yükleyici:

Bu kategori, Eklentilerimizin bulunduğu bir Dizin seçmemize izin verecek ve hepsini bir kerede kurabileceğiz.  

İlk listeden Çoklu yükleyici seçeneğini seçtikten sonra sekme tuşu ile ilerlediğimizde: "Yüklemek istediğiniz eklentilerin bulunduğu bir dizin seçin" butonuna erişiriz. ALT+S ile de erişebildiğimiz bu düğmeye bastığımızda, kurmak istediğimiz eklentilerin bulunduğu klasörü seçebiliriz.  

Bu kategorideki arayüzün geri kalanı, biz bir dizin seçene kadar devre dışı bırakılır.  

Bir dizin seçtiğimizde, odak bizi eklentileri tararken neler olup bittiği hakkında bilgilendirileceğimiz tek okuma kutusunda bırakacak, ayrıca ilerleme çubuğundan da bilgi alacağız.  

Tarama bittiğinde herhangi bir sorun olup olmadığı ve nasıl hareket edileceği konusunda bilgilendirileceğiz. Kullanmakta olduğmuz NVDA sürümü ile uyumsuz ve hasarlı olan eklentiler listeye dahil edilmez.  

Tarama işlemi tamamlandıktan sonra, açılan uyarı mesajını Kabul et butonuna basarak kapatırsak, belirttiğimiz dizindeki sorunsuz eklentiler adları ile listeye eklenecektir.  

Listeye, ALT+L ile de erişebilir ve istedeğimiz kadar eklentiyi boşluk çubuğu ile seçebiliriz.  

Seçme işlemini tamamladıktan sonra sekme tuşuna basarsak seç butonu gelir. Eklenti paketleyici alanında olduğu gibi aynı işleve sahiptir.  

Eğer tekrar Tab tuşuna basarsak, Yükle butonu gelir. ALT+Y ile de hızlıca erişebiliriz.  

Seçtiğimiz en az bir veya daha fazla eklenti, NVDA'nın kullandığı klasik eklenti kurma penceresini göstermeden daha hızlı şekilde kurulacaktır.  

Bu alanda da sadece uyumlu eklentilerin kurulabildiğini ve size sorun yaşatmayacağını belirtmeliyiz.  

Yükle butonuna basıldığı anda, Eklenti sürecin belirtildiği kutuya odaklanacaktır.  

Ayrıca süreç bittiğinde: yüklenen, kurulamayan ve varsa hataların bizlere bildirildiği bir pencere açılır.  

Pencerede verilen sonuçlara bağlı olarak: Kapat butonunun yanı sıra, Kabul et veya İptal düğmeleri de bulunabilir.  

Kabul et düğmesi etkinleştirilirse, Yüklenen eklentilerin ve yapılan değişikliklerin etkin olabilmesi için NVDA yeniden başlatılır.  

Kabul etmez ve kapatırsak, NVDA'yı yeniden başlatana kadar eklentiyi tekrar kullanamayacağız, bu yinelenen eylemleri önlemek için bir korumadır.  

Aksi takdirde hatalar varsa ve yalnızca iptal düğmesi sunulursa, başka şeyler yapmak için ona basabilir ve arayüze dönebiliriz.  

### UYARI:

Bu kategori, eklentilerin kurulumunu kolaylaştırmak için uygulanmaktadır, ancak yanlış eklentiler yüklenerek  kullanılması okuyucunun performansının düşmesine neden olabilir. Doğru şekilde kullanmak kullanıcının sorumluluğundadır.  

## Eklentileri Kaldır:

Bu kategori, eklentileri hızlı ve tek bir hareketle kaldırmamıza olanak tanır.  

Yüklü eklentilerin gösterildiği listeden dilediğimiz eklentiyi boşluk çubuğu ile seçebiliriz. Listeye: ALT+L ile de erişebiliriz.  

Yine, diğer kategorilerde de olduğu gibi ALT+S ile de erişebildiğimiz Seç butonu bulunur.  

ALT+R ile de hızlıca erişebileceğimiz kaldır düğmesine bastığımızda, seçtiğimiz eklentilerin kaldırılma süreci başlar ve yine aşamaların verildiği bilgi kutusuna odaklanırız.  

Ayrıca ilerleme çubuğu aracılığıyla bilgilendirileceğiz.  

İşlem tamamlandıktan sonra, yine bilgilendirileceğiz. Kabul Et butonuna basarsak NVDA yeniden başlar. Bir hata varsa da Kapat veya İptal düğmelerini kullanabiliriz.  

Bu kategoride de kapat butonu ile pencereyi kapatırsak, NVDA programını yeniden başlatana kadar eklentiyi kullanamayacağımızı unutmamalıyız.  

## Uyarı!

Kaldır butonuna basmadan önce, kaldırmak istediğiniz eklentilerin paketlerine erişebileceğinizden, gerektiğinde yeniden kurabileceğinizden ve paketlere erişim bilgilerinin silinecek dizinde olmadığından emin olmalısınız. Nitekim, kaldırma işlemi geri alınamaz.  

Bu genellikle iyi bir uygulama değildir ve NVDA, eklentilerin bilgileri eklentinin aynı dizininde tutmasını önermez, ancak bu zaten eklenti programcısının bir kararıdır.  

Bu nedenle, bu kategoriyi sizin sorumluluğunuzda kullanmak için kendimi tekrar ediyorum.  

## Eklentileri etkinleştir/devre dışı bırak:

Bu kategori, Eklentilerimizi etkinleştirmemize veya toplu olarak devre dışı bırakmamıza izin verecektir.  

(Alt+L) ile hızlı bir şekilde erişebileceğimiz eklentiler listesinde devre dışı bırakmak istediğimiz eklentileri boşluk çubuğu ile işaretleyebiliriz.  

Eğer daha önceden devre dışı bırakılmış eklentiler varsa, "Devre dışı eklentilerin listesi adlı bir liste daha bulunur. Bu listeler arasında ALT+L ile hızlıca geçiş yapılabilir. Bir eklentiyi etkinleştirmek istersek, yine boşluk çubuğu ile işaretleyebiliriz.  

Etkinler listesinde işaretlenen eklentileri devre dışı bırakarak, devre dışı listesinde işaretlenen eklentileri etkinleştirerek işlemin ters yapılacağını göz önünde bulundurarak iki listede eklentileri işaretleyebiliriz.  

Bu kategoride de bir Seç düğmesi bulunur. Lakin, devre dışı bırakılmış eklenti bulunuyorsa, Etkin eklentiler ve Devre dışı eklentiler şeklinde iki seçenek ve alt menüleri bulunacaktır.  

Sekme veya ALT+U ile erişebileceğimiz Uygula butonuna bastığımızda yine salt okunur bir bilgi kutusu açılırve aşamaları takip edebiliriz.  

Eylem bittiğinde, önceki kategorilerde olduğu gibi ilgili düğmelerin bildirilmesi ve etkinleştirilmesi gerçekleşecektir.

Eylem tatmin ediciyse ve yeniden başlatmazsak, NVDA yeniden başlatılana kadar eklentinin kullanılmayacağını tekrar hatırlatıyorum.  

## Manifest değiştirici:

Bu kategoride Manifest dosyasını değiştirebilir ve böylece eklentileri NVDA'nın gerektirdiği API ile uyumlu hale getirebiliriz. Manifest dosyasını, yüklü olan eklenti için veya .Add-on uzantısına sahip kurulu olmayan eklenti için değiştirebiliriz.  

Artık en son NVDA politikasına ve hatta yeni değişikliklere göre, NVDA programcılarının her yıl ilk sürümünde, NVDA sürümüyle kendi Manifest dosyalarını eşleştirmek için sürümü değiştirmeleri gerekecek.  

Bunu hemen yapacak programcılar olacak, diğerleri geç kalacak ve sadece takviyeleri bırakmak veya herhangi bir nedenle bunu yapmayacak olanlar olacak.  

Bu son durumda, lastTestedNVDAVersion özelliğinin değişikliğini elle yapmalıyız ve çok sayıda eklentimiz varsa, zaman kaybetmek zorunda kalacağız. Ayrıca birçok kişi kullanıcı seviyesi olduğu için bu tüm kullanıcılar için bir görev değildir.  

Ayrıca, betaları ve RC'leri test etmek istiyorsak, Manifest dosyalarında bu parametreyi değiştirmemiz gerekecek, aksi takdirde eklentiyi yükleyemeyeceğiz.  

NVDA sürekli gelişen bir okuyucudur ve pek çok kez geliştirme eksikliği ve bunları NVDA'nın evriminde getirdiği değişikliklere adapte edememe nedeniyle yolda kalan eklentiler vardır.  

Bu, Manifest'lerdeki tarihin değiştirilmesinin, güncellenmemiş eklentileri kullanmaya devam etmek için anlık bir sorunu çözdüğü veya geliştiricinin bunları güncellemeyi geciktirdiği anlamına Manifest dosyalarındaki tarih değişikliği, geliştirici güncellemeleri geciktirdiğinde geçici bir çözüm olacaktır. Tarih değişikliğinin işe yaramadığı ve kod uyumsuzluğu yaşanan durumlarda geliştirici ile iletişime geçmek gerektiği unutulmamalıdır.  

Bu yardımcı araç ile, Manifest dosyalarını değiştirsek de, geliştirici bir güncelleme sunduğunda mutlaka güncellemenin yüklenmesi gerekir. Verilen güncellemede Manifest dosyasındaki uyum haricinde başka geliştirmeler de yapılmış olabilir.  

Bu kategoriye eriştiğimizde, API sürümüyle birlikte yüklediğimiz tüm eklentileri içeren listeye gireceğiz. (Alt+L) ile hızlı bir şekilde erişebilir, manifestini değiştirmek istediğimiz eklentileri üzerlerine tıklayarak ve istediğimiz kadar seçebiliriz.  

Sekme tuşuna bastığımızda sırasıyla üç seçim kutusuna erişiriz:  

* Ana sürümü seç: Bu seçim kutusundaki tarih kullanılan NVDA sürümü ile aynı olmalı.
* Ara sürümü seç: Burada 1'de bırakmak yeterlidir ancak yılda dört ara sürüm çıkarıldığı düşünüldüğünde 4 olarak seçilmesi daha uygun olabilir.
* Düzeltme sürümü seç: Bu kutuda 0 bırakmak yeterli, ancak yine de 9'a kadar seçenek sundum.

Sekme tuşuna basarsak, listedeki tüm eklentileri seçmemize veya seçimini kaldırmamıza izin verecek bir seçim butonumuz var.  

Eğer tab tuşuna bir defa daha basarsak, Uygula butonuna erişiriz. Yine ALT+U kısayolunu kullanabiliriz.  

Bu düğmeye basarsak, aşağıdaki seçeneklerin bulunduğu bir menü görüntülenecektir:

* Dosyaya uygula: Yaptığımız değişiklikleri listeden seçtiğimiz ve kurulu olan eklentinin manifest dosyasına uygular.
* Eklenti paketine uygula: Yaptığımız değişiklikleri, kurulu olmayan ve .nvda-addon uzantısına sahip dosyaya uygular.

Eğer değişiklikleri bir eklenti paketine uygularsak: eklentiyi seçtiğimiz dizinde aynı adla bir eklenti paketi oluşturulacak. Ancak güvenlik nedeni ile sonuna: "_gen_modify_manifest" ibaresi de eklenecektir.  

Seçeneklerden herhangi biri ile odak tek okuma kutusuna bırakılacak ve ne olduğu konusunda bilgilendirileceğiz.  

Davranış, kabul etme ve iptal etme düğmeleriyle önceki kategorilerdekiyle aynı olacaktır.  

Daha önce bir eklenti dosyası seçersek, dosyaya uygulamak için daha büyük, daha küçük ve revizyonun birleştirilmiş çerçevelerini değiştirmemiz gerektiğinde, manifeste bu yapılandırmayı seçtiğimizi hatırlıyorum.  

## Uyarı!

Bu yardımcı programın kullanımı ve sonuçları münhasıran son kullanıcının sorumluluğundadır.  

## Eklenti belgeleri:

Bu kategoriyi belgelere erişim sorunu yaşayan kullanıcılar olduğunu gördüğüm için oluşturdum. Eklentilerin nasıl kullanılacağını öğrenebilmek için geliştiricinin sunduğu belgeleri okumalısınız.  

Bu kategoride, herhangi bir nedenle belgesi olmayanlar hariç, belgeleri olan tüm eklentilerin görüntüleneceği bir liste bulacağız. Yine ALT+L ile liste alanına hızlıca erişebiliriz.  

Eğer bir defa sekme tuşuna basarsak, listeden seçtiğimiz eklentinin belgesini varsayılan tarayıcımızda açabileceğimiz Eklenti belgesini Aç butonu gelir. ALT+A ile de etkinleştirebiliriz.  

# Çevirmenler ve ortak çalışanlar:

Birisi çevirilerle işbirliği yapmak isterse, bunu Github eklenti deposu aracılığıyla veya <xebolax@gmail.com> adresine e-posta göndererek yapabilir.  

* İngilizce: Otomatik çeviri
* Türkçe: Umut KORKMAZ

# Değişiklik Günlüğü:
## Güncelleme bilgileri:
Bu eklenti aşağıdaki yükseltme yolunu izleyecektir:  

Bu kayıtta yalnızca daha büyük boyutlu sürümler (ör. v3.1) listelenir.  

Daha büyük type.menor.x sürümleri (ör. v3.1.2) çeviri güncellemeleridir.  

Eklentideki değişiklikler, en son gelişmelerin açıklandığı bu bölüme yansıtılacaktır.  

Ana belge, kullanıcı için bir yönlendirme olarak değiştirilmeyecektir.  

Değişikliklerden haberdar olmak için bu bölümü incelemek kullanıcının sorumluluğundadır.  

## Sürüm 1.0:

♪ İlk Sürüm.  

Yeni işlevlerin dahil edilmesiyle birlikte eski Eklenti Paketleyici ne sıfırdan yeniden yazılacaktır.  

Eklenti, NVDA eklentileri için yardımcı araçlar adını alır. Ancak, NVDA dahili olarak (addonPackager) adını kullanmaya devam eder.  

Bu eklentide, Manifest değiştirici bulunduğundan. CriCriCri eklentisi artık bakım almayacaktır.  

ArgosTranslate tarafından çevrildi

