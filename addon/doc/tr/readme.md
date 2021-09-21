# Eklenti Paketleyici  

Bu eklenti, kurulu eklentilerin bir yedeğine sahip olma ihtiyacından kaynaklanmaktadır.

NVDA, resmi arşivlerden veya yazarların farklı github hesaplarından kolayca edinilebilen geniş bir resmi eklenti koleksiyonuna sahiptir.

Ancak aynı zamanda, kaynağını belirlemek bazen zor olan bir dizi resmi olmayan eklentiye de sahiptir.

Bu fikir, bir arkadaşım benden resmi olmayan bir eklenti istediğinde ortaya çıktı ve eklenti benim erişimimde olmadığı için onu paketlemek zorunda kaldım.

Eklenti paketleme süreci kolay ama herkes tarafından bilinmiyor, bu yüzden NVDA'nın böyle bir özelliği olsa harika olur diye düşündüm.

İşte bu eklentinin yaptığı şey bu: kullanıcının sahip olmak istediği eklentileri otomatik olarak paketler, böylece başka bir NVDA kopyasına, temiz bir NVDA kurulumuna veya sadece onu paylaşmak için kurulabilirler.

## Eklentiyi kullanma

Eklenti dört alana ayrılmıştır:

* İlki, etkin veya devre dışı bırakılmış tüm yüklü eklentilerimizin bir listesini içerir. Bu listede istediğimiz tüm eklentileri seçebiliriz.
* İkincisi, tüm eklentileri hızlı bir şekilde seçmek veya yaptığımız tüm seçimleri hızla silmek için bir dizi düğme içerir.
* Üçüncüsü, çıktı dizinini içeren bir okuma metin kutusu ve bu çıktı dizinini seçmek için bir düğme.

Çıktı dizinini herhangi bir zamanda kontrol etmeyi kolaylaştırmak için metin kutusunu salt okunur olarak koydum. Yanlışlıkla basılmasını önlemek için normal bir düzenleme alanı olarak koymamaya karar verdim ve bu nedenle dizin etkilenebilir.

* Dördüncüsü, önceden paketlenmiş eklentileri oluşturmak için düğme ve eklentiden çıkmak için bir düğme içeren düğme sırasıdır.

### Eklentikısayolları

* Alt + L: odak noktamızı açık listeye yerleştirecek.
* Alt + S: Daha önce seçili olup olmadığına bakılmaksızın tüm eklentileri bizim için seçecektir.
* Alt + T: Seçili bütün eklentilerin seçimini temizler.
* Alt + D: Çıktı dizinini seçmek için bir dizin seçim penceresi açacaktır.
* Alt + E: Çıktı dizininde seçtiğimiz eklentilerin oluşturulmasına başlayacaktır.
* Alt + K veya Alt + F4: Eklentiyi kapatır.

## İlgilenilen diğer bilgiler

* Eklenti, kullanım seyri hakkında bilgi diyalogları ile her zaman bizi uyaracaktır.
* Bir eklenti seçmeden eklenti oluşturmaya çalışırsak bizi uyarır.
* Tanımlanmış bir çıktı dizini olmadan bir eklenti oluşturmaya çalışırsak bizi uyarır.
* İşlem başarılı olduğunda ve bir hata oluştuğunda bizi uyaracaktır.
* Çıktı dizini, eklentiyi bir sonraki kullanımımızda belirtilmesi için kaydedilecektir. Çıktı dizini silinirse bu ayar silinecek ve başka bir tane seçmemiz gerekecek.existing directory.
* Eklentileri oluştururken, bir ilerleme çubuğu her zaman tamamlanan yüzde hakkında bizi uyaracaktır.
* Ortaya çıkan dosyaların adında oluşturulduklarını ve orijinal olmadıklarını belirten bir etiket bulunur. Bu etiket (gen).

# Çok önemli bir uyarı

Ortaya çıkan dosyaların, bu eklenti tarafından herhangi bir şey eklemeden veya çıkarmadan, Addon dizinimizde sahip olduğumuz şekilde olduğunu belirtmekte fayda var.

Bu, seçtiğimiz eklentinin tüm bilgilerinin dahil olduğu anlamına gelir.

Bir eklenti geliştiricisinin, eklenti dizininin kendisinde hassas bilgiler içermesi normal değildir.

Aslında, bu kötü bir uygulama olarak kabul edilir, bu nedenle en azından resmi eklentilerde bu pek olası değildir.

Ancak yüzlerce farklı türden resmi olmayan eklenti olduğundan, bir eklentinin kendi dizininde hassas bilgiler içermesi durumunda bu hassas bilgilerin silineceği konusunda uyarılırsınız. oluşturulan dosyada.


Bu nedenle, paylaşacağımız oluşturulmuş bir eklentinin paylaşmak istemediğimiz herhangi bir hassas bilgi getirip getirmediğini bilmek için bu gizlilik ve güvenlik yönünü dikkate almalıyız.

Bahsettiğim gibi, bu neredeyse imkansız, ancak bu eklentiyi kullanarak uyarıldığınızı ve bu eklentinin yazarının tüm sorumluluklardan muaf olduğunu kabul etmiş olursunuz.

Çeviren: Umut KORKMAZ