import tkinter as tk
from tkinter import messagebox
import requests
import json

class WebexAPIApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Webex API Client")

        self.access_token = tk.StringVar()

        """ Entry fields """
        tk.Label(root, text="Access Token:").grid(row=0, column=0, sticky="e")
        self.token_entry = tk.Entry(root, textvariable=self.access_token)
        self.token_entry.grid(row=0, column=1)

        """ Buttons """
        self.btn_verify = tk.Button(root, text="Verify", command=self.verify_token)
        self.btn_verify.grid(row=1, column=1, padx=5, pady=5)

        self.btn_user_info = tk.Button(root, text="User Info", command=self.display_user_info)
        self.btn_user_info.grid(row=2, column=0, padx=5, pady=5)

        self.btn_list_rooms = tk.Button(root, text="List Rooms", command=self.list_rooms_window)
        self.btn_list_rooms.grid(row=2, column=1, padx=5, pady=5)

        self.btn_create_room = tk.Button(root, text="Create Room", command=self.create_room_window)
        self.btn_create_room.grid(row=3, column=0, padx=5, pady=10)

        self.btn_send_message = tk.Button(root, text="Send Message", command=self.send_message_window)
        self.btn_send_message.grid(row=3, column=1, padx=5, pady=10)

    """ verify access token """
    def verify_token(self):
        access_token = self.access_token.get()
        url = 'https://webexapis.com/v1/people/me'
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            messagebox.showinfo("Verification Successful", f"Welcome {user_info['nickName']}!")
        else:
            messagebox.showerror("Verification Failed", "Invalid Access Token")


    """ user information """
    def display_user_info(self):
        access_token = self.access_token.get()
        url = 'https://webexapis.com/v1/people/me'
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            messagebox.showinfo("User Information", 
                                f"Display Name: {user_info['displayName']}\n"
                                f"First Name: {user_info['firstName']}\n"
                                f"Last Name: {user_info['lastName']}\n"
                                f"Nickname: {user_info['nickName']}\n"
                                f"Email: {user_info['emails'][0]}")
        else:
            messagebox.showerror("Error", "Failed to fetch user information")

    
    """ list of rooms """
    def list_rooms_window(self):
        access_token = self.access_token.get()
        url = 'https://webexapis.com/v1/rooms'
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        params = {'max': '5'}  # Limiting to 5 rooms for simplicity
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            rooms = response.json()['items']
            self.display_rooms_window(rooms)
        else:
            messagebox.showerror("Error", "Failed to fetch room list")

    
    """ display room details """
    def display_rooms_window(self, rooms):
        self.rooms_window = tk.Toplevel(self.root)
        self.rooms_window.title("Rooms")

        self.current_index = 0
        self.rooms = rooms

        self.room_details_frame = tk.Frame(self.rooms_window)
        self.room_details_frame.pack()

        self.show_room_details()

        tk.Button(self.rooms_window, text="Prev", command=self.prev_room).pack(side="left")
        tk.Button(self.rooms_window, text="Next", command=self.next_room).pack(side="right")

    
    """ room details """
    def show_room_details(self):
        for widget in self.room_details_frame.winfo_children():
            widget.destroy()

        # Determine the range of rooms to display
        start_index = self.current_index
        end_index = min(start_index + 5, len(self.rooms))

        # Display details for each room within the range
        for i in range(start_index, end_index):
            room = self.rooms[i]
            tk.Label(self.room_details_frame, text=f"Room Name: {room['title']}").pack()
            tk.Label(self.room_details_frame, text=f"Room ID: {room['id']}").pack()
            tk.Label(self.room_details_frame, text=f"Last Activity: {room['lastActivity']}").pack()
            tk.Label(self.room_details_frame, text="").pack()

    """ next room """
    def next_room(self):
        self.current_index += 5
        if self.current_index >= len(self.rooms):
            self.current_index = 0
        self.show_room_details()


    """ previous room """
    def prev_room(self):
        self.current_index -= 5
        if self.current_index < 0:
            self.current_index = (len(self.rooms) - 1) // 5 * 5
        self.show_room_details()



    """ create a new room """
    def create_room_window(self):
        self.create_room_window = tk.Toplevel(self.root)
        self.create_room_window.title("Create Room")

        tk.Label(self.create_room_window, text="Room Name:").grid(row=0, column=0, sticky="w")
        self.room_name_entry = tk.Entry(self.create_room_window)
        self.room_name_entry.grid(row=0, column=1)

        create_btn = tk.Button(self.create_room_window, text="Create", command=self.create_room)
        create_btn.grid(row=1, column=0, columnspan=2, pady=10)

    
    """ create a room """
    def create_room(self):
        room_name = self.room_name_entry.get()
        access_token = self.access_token.get()
        url = 'https://webexapis.com/v1/rooms'
        headers = {'Authorization': 'Bearer {}'.format(access_token), 'Content-Type': 'application/json'}
        data = {'title': room_name}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            messagebox.showinfo("Room Created", "Room created successfully")
            self.create_room_window.destroy()
        else:
            messagebox.showerror("Error", "Failed to create room")

    
    """ send message window """
    def send_message_window(self):
        self.send_message_window = tk.Toplevel(self.root)
        self.send_message_window.title("Send Message")

        tk.Label(self.send_message_window, text="Room Name:").grid(row=0, column=0, sticky="w")
        self.message_room_entry = tk.Entry(self.send_message_window)
        self.message_room_entry.grid(row=0, column=1)

        tk.Label(self.send_message_window, text="Message:").grid(row=1, column=0, sticky="w")
        self.message_entry = tk.Entry(self.send_message_window)
        self.message_entry.grid(row=1, column=1)

        send_btn = tk.Button(self.send_message_window, text="Send", command=self.send_message)
        send_btn.grid(row=2, column=0, columnspan=2, pady=10)

    
    """ send a message to a room """
    def send_message(self):
        access_token = self.access_token.get()
        room_name = self.message_room_entry.get()
        message = self.message_entry.get()
    
        # Fetch list of rooms
        url = 'https://webexapis.com/v1/rooms'
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = requests.get(url, headers=headers)
    
        if response.status_code == 200:
            rooms = response.json().get('items', [])
            # Find the roomId for the provided roomName
            room_id = None
            for room in rooms:
                if room['title'] == room_name:
                    room_id = room['id']
                    break
        
            if room_id:
                # Send message to the room
                url = 'https://webexapis.com/v1/messages'
                headers = {'Authorization': 'Bearer {}'.format(access_token), 'Content-Type': 'application/json'}
                data = {'roomId': room_id, 'markdown': message}
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    messagebox.showinfo("Message Sent", "Message sent successfully")
                    self.send_message_window.destroy()
                else:
                    messagebox.showerror("Error", "Failed to send message")
            else:
                messagebox.showerror("Error", f"Room '{room_name}' not found")
        else:
            messagebox.showerror("Error", "Failed to fetch room list")

def main():
    root = tk.Tk()
    app = WebexAPIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
