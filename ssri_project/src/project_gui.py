import dearpygui.dearpygui as dpg

def on_selection(sender, unused, user_data):
    if user_data[1]:
        print("User selected 'Ok'")
    else:
        print("User selected 'Cancel'")

    # guarantee these commands happen in another frame
   
   #width = dpg.get_item_width(modal_id)
    #height = dpg.get_item_height(modal_id)
    #dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])"""

dpg.create_context()
dpg.create_viewport(title='SSRI Project', width=600, height=600)

with dpg.window(label="Exit", modal=True, show=False, tag="modal_id", no_title_bar=True):
    dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))
    dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))
       

with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("fonts/DMSans-Regular.ttf", 16)

with dpg.window(label="SSRI Project"):
    dpg.bind_font(default_font)
    dpg.add_text("SSRI Project")
    questionnaireb = dpg.add_button(tag="questionnaire", label="Enter wellbeing questionnaire")
    exitb = dpg.add_button(tag="exit", label="Exit the program", 
        callback=lambda: dpg.configure_item("modal_id", show=True))
    
    #if dpg.get_item_state(exitb)["clicked"] == True:

dpg.show_font_manager()
dpg.show_style_editor()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
