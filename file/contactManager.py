class ContactManager:


    def __init__(self, filename: str):
        self.filename = filename

    def add_contact(self):

        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email address: ")
        with open(self.filename, "a") as f:
            f.write(f"{name},{phone},{email}\n")

    def read_contact_list(self):

        with open(self.filename, "r") as f:
            for line in f:
                contact_data = line.split(",")
                contact = Contact(*contact_data)
                print(contact)

    def search_contact(self, name: str):

        with open(self.filename, "r") as f:
            for line in f:
                contact_data = line.split(",")
                if contact_data[0] == name:
                    contact = Contact(*contact_data)
                    return contact
        return None

    def update_information(self):

        name = input("Enter contact name to update: ")
        with open(self.filename, "r") as f:
            lines = f.readlines()
        with open(self.filename, "w") as f:
            for line in lines:
                contact_data = line.split(",")
                if contact_data[0] == name:
                    new_name = input("Enter new contact name: ")
                    new_phone = input("Enter new contact phone number: ")
                    new_email = input("Enter new contact email address: ")
                    contact_data[0] = new_name
                    contact_data[1] = new_phone
                    contact_data[2] = new_email
                    line = ",".join(contact_data)
                f.write(line)


if __name__ == "__main__":
    contact_manager = ContactManager("contac_list.txt")

    contact_manager.add_contact()
    contact_manager.read_contact_list()

    contact_manager.update_information()
    contact_manager.read_contact_list()