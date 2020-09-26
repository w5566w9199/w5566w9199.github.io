import os
import requests
import re
# actions預設
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# Rasa功能引入
import asyncio
from rasa.core import utils
from rasa.utils import io
from rasa.utils.endpoints import EndpointConfig
from rasa.cli.arguments import default_arguments
from rasa.core.agent import Agent
from rasa.core.interpreter import NaturalLanguageInterpreter, RasaNLUHttpInterpreter, RasaNLUInterpreter
from rasa.core.trackers import DialogueStateTracker
from rasa.core.domain import Domain
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
# 郵遞區號
import zipcodetw
# 資料庫
from pymongo import MongoClient
import pymongo

# 連線Mongodb
connect = MongoClient(host='localhost', port=27017, username="", password="")
db = connect['worker']
collect = db['Client']

# 客戶單號查寄件人資料
class FormActionReplySender(FormAction):    
    def name(self) -> Text:		

        return "cusOrder_sender"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("123123")
        return ["cusOrder"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "cusOrder": [self.from_text()]            
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        shipNum = tracker.get_slot("cusOrder")
        print(shipNum.zfill(14))
        search = collect.find_one({'cusOrder': shipNum.zfill(14)})
        if (search == None):
            dispatcher.utter_message(text="查無資料")
        else:
            dispatcher.utter_message(text="寄件人是{data}".format(data=search['senderName']))        
            dispatcher.utter_message(text="寄件地址是{data}".format(data=search['senderAddr']))        
            dispatcher.utter_message(text="寄件人電話是{data}".format(data=search['senderPhone']))

        return []

# 客戶單號查收件人資料
class FormActionReplyCusowner(FormAction):
    def name(self) -> Text:
        return "cusOrder_cusOwner"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cusOrder"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cusOrder": [self.from_text()]            
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        shipNum = tracker.get_slot("cusOrder")
        search = collect.find_one({'cusOrder': shipNum.zfill(14)})
        if (search == "" or search == None):
            dispatcher.utter_message(text="查無此客戶單號")
        else:
            dispatcher.utter_message(text="收件人是{data}".format(data=search['cusOwnerName']))      
            dispatcher.utter_message(text="地址是{data}".format(data=search['addr']))        
            dispatcher.utter_message(text="連絡電話是{data}".format(data=search['contractTel']))    

        return []

# 客戶單號查寄件人資料
class ActionReplySender(Action):
    def name(self) -> Text:
        return "reply_data_sender"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        shipNum = tracker.get_slot("cusOrder")
        search = collect.find_one({'cusOrder': shipNum})

        if (search == None):
            dispatcher.utter_message(text="查無資料")
        else:
            dispatcher.utter_message(text="寄件人是{data}".format(data=search['senderName']))        
            dispatcher.utter_message(text="寄件地址是{data}".format(data=search['senderAddr']))        
            dispatcher.utter_message(text="寄件人電話是{data}".format(data=search['senderPhone']))

        return []

# 客戶單號查收件人資料
class ActionReplyCusowner(Action):
    def name(self) -> Text:
        return "reply_data_cusOwner"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        shipNum = tracker.get_slot("cusOrder")
        search = collect.find_one({'cusOrder': shipNum})

        if (search == "" or search == None):
            dispatcher.utter_message(text="查無此客戶單號")
        else:
            dispatcher.utter_message(text="收件人是{data}".format(data=search['cusOwnerName']))      
            dispatcher.utter_message(text="地址是{data}".format(data=search['addr']))        
            dispatcher.utter_message(text="連絡電話是{data}".format(data=search['contractTel']))        
            
        return []

# 電話查客戶單號
class CusNumPhone(Action):
    def name(self) -> Text:
        return "reply_custNum_phone"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cusPhone = tracker.get_slot("phone")
        # data = "".join(re.findall(r'[0-9]+',"cusPhone"))
        search = collect.find_one({'$or':[{'contractTel': cusPhone},{'senderPhone': cusPhone}]}, {'_id':0 , 'cusOrder':1, 'senderName':1})
        if (search == "" or search == None):
            dispatcher.utter_message(text="查無此電話")
        else:
            dispatcher.utter_message(text="客戶單號是{data}".format(data=search['cusOrder']))
            dispatcher.utter_message(text="寄件名稱是{data}".format(data=search['senderName']))

        return []

# 地址查客戶單號
class CusNumAddrees(Action):
    def name(self) -> Text:
        return "reply_custNum_addr"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cusAddr = tracker.get_slot("address")
        search = collect.find_one({'$or':[{'addr': cusAddr},{'senderAddr': cusAddr}]} , {'_id':0 , 'cusOrder':1, 'senderName':1})
        if (search == "" or search == None):
            dispatcher.utter_message(text="查無此地址")
        else:
            dispatcher.utter_message(text="客戶單號是{data}".format(data=search['cusOrder']))
            dispatcher.utter_message(text="寄件名稱是{data}".format(data=search['senderName']))

        return []

# 查詢郵遞區號
class ActionReplyposCode(Action):
    def name(self) -> Text:
        return "reply_posCode"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        address = tracker.get_slot("address")
        poscode = zipcodetw.find(address)
        if (poscode != ""):
            dispatcher.utter_message(text="郵遞區號是{poscode}".format(poscode=poscode))
        else:
            dispatcher.utter_message(text="地址錯誤")

        return []


# 例外判斷回傳區塊
class ActionCustomFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("無法辨識")

        return []
