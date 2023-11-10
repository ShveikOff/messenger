#Классы чата и группы на примере telegramm

class chat:
    
    def __init__(self, user_name, user_status):
        self.user_info = False
        self.contact_name = user_name
        self.contact_status = user_status
        self.user_name = user_name
        self.notifications = True
        self.send_message = None
        self.photo_list = {}
        self.videos_list = {}
        self.shar_links_list = {}
        self.gifs_list = {}
        self.edit_contact = None
        self.delete_contact = None
        self.block_user = None
        self.set_wallpaper = None
        self.chat_export = None
        self.clear_history = None
        self.delete_chat = None
      
    def search(self, searching_text):
        pass
    def call(self):
        pass
    def message(self):
        pass
    def display_info(self):
        print(f'''
              Contact name: {self.contact_name}\n
              Contact status: {self.contact_status}\n
              Notifications: {self.notifications}\n 
              Foto: {len(self.photo_list)}\n 
              Videos: {len(self.videos_list)}\n 
              Shared_links: {len(self.shar_links_list)}\n 
              Gifs: {len(self.gifs_list)}\n
              ''')

print_shop = chat('rakursfoto', 'last seen recently')
print_shop.notifications = True
print_shop.photo_list = {1: '', 2: '', 3: '', 4: ''}
print_shop.videos_list = {1: ''}

print_shop.display_info()