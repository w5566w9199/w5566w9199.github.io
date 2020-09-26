## intent:ask_sender
- 寄件人
- 查寄件人
- 搜尋寄件人
- 查寄件人資料

## intent:ask_cusOwner
- 收件人
- 查收件人
- 搜尋收件人
- 查收件人資料

## intent:ask_custNum
- 客戶單號
- 查客戶單號
- 查詢客戶單號
- 搜尋客戶單號

## intent:ask_posCode
- 郵遞區號
- 查郵遞區號
- 查詢郵遞區號
- 搜尋郵遞區號

## intent:input_cusOrder
- 託運單號[98765432104321](cusOrder)
- 託運號碼[33366699955514](cusOrder)
- 託運單號是[12345678901234](cusOrder)
- 客戶單號是[00002543412137](cusOrder)
- 客戶單號是[00002543412925](cusOrder)
- 客戶單號[00002543412918](cusOrder)
- 客戶單號[00002543412931](cusOrder)
<!-- 客戶單號為14碼 -->
## regex:cusOrder
- [0-9]{14}

## intent:input_phone
- 電話號碼是[0222675100](phone)
- 號碼是[033842026](phone)
- 市話是[033842026](phone)
- 電話[0912123456](phone)
- 手機[0909852963](phone)
<!-- 電話號碼 -->
## regex:phone
- [0-9]*

## intent:input_addr
- [台北市大安區忠孝東路四段７１號](address)
- [新北市蘆洲區光華路172號](address)
- [基隆市安樂區基金三路63號](address)
- [桃園市中壢區工業區北園路37號](address)
- [台中市北區三民路三段129號](address)
- [台南市仁德區文華路二段66號](address)
- [高雄市鳳山區國泰路二段156號](address)
- [新竹縣竹北市自強五路60號](address)
- [新竹市東區忠孝路300號](address)
- [苗栗縣頭份鎮八德一路193號3樓](address)
- [彰化縣溪湖鎮彰水路二段762號](address)
- [南投縣埔里鎮中山路一段421號](address)
- [雲林縣麥寮鄉海豐村永和40-160號](address)
- [嘉義縣水上鄉柳鄉村柳子林119號](address)
- [屏東縣萬巒鄉東山路110號](address)
- [宜蘭縣冬山鄉永興路二段273巷1號](address)
- [花蓮縣吉安鄉明仁三街45號](address)
- [台東縣卑南鄉泰安村6號](address)
- [澎湖縣馬公市新復路2巷22號](address)
- [金門縣金湖鎮安民村1之10號](address)
- [連江縣南竿鄉介壽村202號](address)



<!-- 例外訊息區塊 -->
## intent: out_of_scope
- 無法辨識
- 輸入錯誤
- 聽不懂
- 啦啦啦
- 嘿嘿嘿
- 壞掉了
- 怪怪的
- 不見了
- 例外情況


