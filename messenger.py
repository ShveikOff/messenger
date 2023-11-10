import time

### message поступает на сервер в виде словаря {'text' : text, adres : {fromWho : userid, toWho : userid, where : groupid}}

#Класс сообщения в телеграмм
class messages:

    buffer = []
    
    def __init__ (self, message):
        self.time = time()
        self.text = message['text']
        self.fromWho = message['adres']['fromWho']
        self.toWho = message['adres']['toWho']
        self.where = message['adres']['where']
        self.adres = (self.fromWho, self.toWho, self.where)
        #self.sent = False
        #self.readen = False
        #self.links = ''
        #self.foto_id = None
        #self.video_id = None
        #self.file_id = None
        #self.audio_message_id = None
        #self.attachments = (self.links, self.foto_id, self.video_id, self.file_id, self.audio_message_id)

    def send (self):
        messages.buffer.append(self)
        pass
    
    def redact (self):
        pass

    def pin (self):
        pass

    def replay (self):
        pass

    def delete (self):
        pass

    def forward (self):
        pass

    def display_info(self):
        print (messages.buffer)



class users:

    user_list = {}

    def __init__(self):
        self.id = None
        self.password = None
        self.description = None
        self.phone_number = None
        self.name = None
        self.uniq_name = None
        self.avatar_id = None
        self.user_info = (self.description, self.phone_number, self.name, self.uniq_name, self.avatar_id)
        self.status = 'offline'
        self.contacts = {}
        self.add_to_user_list()
    
    def add_to_user_list(self):
        users.user_list[self.id] = self

    def add_contact (self):
        pass
    
    def create_group (self):
        pass

    def delete_account (self):
        pass

    def change_user_info (self):
        pass
    
    def display_info (self):
        print (users.user_list)

class chats:

    chat_list = []

    def __init__(self):
        self.companion = None
        self.contrcompanion = None
        self.secretchat = False
        self.attachments = ()

    def add_message(self):
        pass
      
    def auto_delete (self):
        pass

    def history_export (self):
        pass

    def text_search (self):
        pass

    def delete_history (self):
        pass

    def delete_chat (self):
        pass
    
    def display_info(self):
        print(chats.chat_list)
    
class groups:

    def __init__(self):
        self.id = None
        self.description = None
        self.name = None
        self.type = None
        self.linked_chanal = None
        self.attachments = None
        self.members_status = []
        self.reactions = None
        self.permissions = None
        self.invate_link = ''

    def text_search (self):
        pass

    def by_user_search (self):
        pass

    def leave_group (self):
        pass
    
    def auto_delete (self):
        pass

    def set_rights (self):
        pass

    def appoint_admin (self):
        pass

    def delete_member (self):
        pass

    def add_member (self):
        pass

    def delete_group (self):
        pass

    def clean_history (self):
        pass

    def survey (self):
        pass


