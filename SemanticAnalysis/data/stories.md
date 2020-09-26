<!-- 功能一:查寄件人資料 -->
## ask_data_sender
* ask_sender
  - cusOrder_sender
  - form{"name": "cusOrder_sender"}
  - form{"name": null}
  - action_restart

<!-- 功能一:查收件人資料 -->
## ask_data_cusOwner
* ask_cusOwner
  - cusOrder_cusOwner
  - form{"name": "cusOrder_cusOwner"}
  - form{"name": null}
  - action_restart

<!-- 功能一:詢問是否查寄件人 -->
## ask_target_sender
* input_cusOrder
  - utter_ask_target
* ask_sender
  - reply_data_sender

<!-- 功能一:詢問是否查收件人 -->
## ask_target_cusOwner
* input_cusOrder
  - utter_ask_target
* ask_cusOwner
  - reply_data_cusOwner

<!-- 功能二:電話查客戶單號 -->
## ask_data_phone
* ask_custNum
  - utter_custNum
* input_phone
  - reply_custNum_phone
  - action_restart

<!-- 功能二:地址查客戶單號 -->
## ask_data_addr
* ask_custNum
  - utter_custNum
* input_addr
  - reply_custNum_addr
  - action_restart

<!-- 功能二:詢問是否電話查客戶單號 -->
## ask_target_custNum
* input_phone
  - reply_custNum_phone
  - action_restart

<!-- 功能二:詢問是否地址查客戶單號 -->
## ask_target_custNum
* input_addr
  - utter_ask_path
* ask_custNum
  - reply_custNum_addr
  - action_restart

<!-- 功能三:查郵遞區號 -->
## ask_data_posCode
* ask_posCode
  - utter_posCode
* input_addr
  - reply_posCode
  - action_restart

<!-- 功能三:詢問是否查郵遞區號 -->
## ask_target_posCode
* input_addr
  - utter_ask_path
* ask_posCode
  - reply_posCode
  - action_restart



<!-- 例外訊息 -->
## default fallback
* out_of_scope
  - action_default_fallback


