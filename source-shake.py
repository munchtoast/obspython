import obspython as obs
import math, time

# Global variables to restore the scene item after shake
shaken_sceneitem = None     # Reference to the modified scene item
shaken_sceneitem_angle = 0  # Initial rotation angle, used as well for oscillations
source_name = "Spaceship"  # Name of the source to shake
frequency = 2              # Frequency of oscillations in Hertz
amplitude = 10             # Angular amplitude of oscillations in degrees
intervals = 0              # Restrict how many times you can oscillate
shaken_scene_handler = None # Signal handler of the scene kept to restore

def script_description():
  return """Source Shake!!
            Shake a source in the current scene when a hotkey is pressed. Go to Settings then Hotkeys to select the key combination.Check the Source Shake Scripting Tutorial on the OBS Wiki for more information."""

#Reset the angle of the scene
def reset_source():
    sceneitem = get_sceneitem_from_source_name_in_current_scene(source_name)
    if sceneitem:
        id = obs.obs_sceneitem_get_id(sceneitem)
        obs.obs_sceneitem_set_rot(sceneitem, 0) #Resets the image to the original angle
    else:
        restore_sceneitem_after_shake()


# Animates the scene item corresponding to source_name in the current scene
def shake_source():
    global intervals
    print(intervals)
    sceneitem = get_sceneitem_from_source_name_in_current_scene(source_name)
    if sceneitem and intervals <= 100: #Shake the screen until after 100 times
        id = obs.obs_sceneitem_get_id(sceneitem)
        if shaken_sceneitem and obs.obs_sceneitem_get_id(shaken_sceneitem) != id:
            restore_sceneitem_after_shake()
        if not shaken_sceneitem:
            save_sceneitem_for_shake(sceneitem)
        angle = shaken_sceneitem_angle + amplitude*math.sin(time.time()*frequency*2*math.pi)
        obs.obs_sceneitem_set_rot(sceneitem, angle)
        intervals += 1
    else:
        reset_source()

# Saves the original rotation angle of the given sceneitem (assumed not None)
def save_sceneitem_for_shake(sceneitem):
    global shaken_sceneitem, shaken_sceneitem_angle, shaken_scene_handler
    shaken_sceneitem = sceneitem
    shaken_sceneitem_angle = obs.obs_sceneitem_get_rot(sceneitem)
    scene_as_source = obs.obs_scene_get_source(obs.obs_sceneitem_get_scene(sceneitem))
    shaken_scene_handler = obs.obs_source_get_signal_handler(scene_as_source)
    obs.signal_handler_connect(shaken_scene_handler, "item_remove", on_shaken_sceneitem_removed)

# Restores the original rotation angle on the scene item after shake
def restore_sceneitem_after_shake():
    global shaken_sceneitem, shaken_sceneitem_angle
    if shaken_sceneitem:
        obs.obs_sceneitem_set_rot(shaken_sceneitem, shaken_sceneitem_angle)
        obs.signal_handler_disconnect(shaken_scene_handler, "item_remove", on_shaken_sceneitem_removed)
        shaken_sceneitem = None

# Retrieves the scene item of the given source name in the current scene or None if not found
def get_sceneitem_from_source_name_in_current_scene(name):
    result_sceneitem = None
    current_scene_as_source = obs.obs_frontend_get_current_scene()
    if current_scene_as_source:
        current_scene = obs.obs_scene_from_source(current_scene_as_source)
        result_sceneitem = obs.obs_scene_find_source_recursive(current_scene, name)
        obs.obs_source_release(current_scene_as_source)
    return result_sceneitem

# Called at script unload
def script_unload():
    restore_sceneitem_after_shake()

# Called before data settings are saved
def script_save(settings):
    restore_sceneitem_after_shake()
    obs.obs_save_sources()

# Callback for item_remove signal
#User deleting the scene while this script is running WILL CAUSE OBS TO CRASH
def on_shaken_sceneitem_removed(calldata):
    restore_sceneitem_after_shake()

#Treat this as main
def script_tick(seconds):
    global intervals
    if (intervals != 2):
        shake_source()

    intervals += 1