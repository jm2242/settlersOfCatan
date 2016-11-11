from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class StudentListButton(ListItemButton):
    pass

class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):
        #1. get students name
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
        #2. add to list view
        self.student_list.adapter.data.extend([student_name])
        #3. reset list view
        self.student_list._trigger_reset_populate()

    def delete_student(self):
        #if list item is selected:
        if self.student_list.adapter.selection:
            #get tet from item selected
            selection = self.student_list.adapter.selection[0].text
            #remove item from list view
            self.student_list.adapter.data.remove(selection)
            #reset list
            self.student_list._trigger_reset_populate()

    def replace_student(self):
        #combination of submit and delete
        if self.student_list.adapter.selection:
            #get tet from item selected
            selection = self.student_list.adapter.selection[0].text
            #remove item from list view
            self.student_list.adapter.data.remove(selection)
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
            # 2. add to list view
            self.student_list.adapter.data.extend([student_name])
            self.student_list._trigger_reset_populate()


class StudentDBApp(App):
    def build(self):
        return StudentDB()


dbApp = StudentDBApp()
dbApp.run()