from pynput import keyboard

class ShortcutsManager:
    hotkeys = {}
    def set_shortcut(self, character, key_combination):
        keys = key_combination.split('+')
        key_codes = []
        for key in keys:
            if key.isalpha():
                key_codes.append(keyboard.KeyCode.from_char(key))
            else:
                key_codes.append(getattr(keyboard.Key, key.upper()))
        hotkey = keyboard.HotKey(key_codes, lambda: print(character))
        self.hotkeys[hotkey] = character
        hotkey.start()
        
    def delete_shortcut(self, character):
        for hotkey, value in self.hotkeys.items():
            if value == character:
                hotkey.stop()
                del self.hotkeys[hotkey]
                break
    
    def view_shortcuts(self):
        return self.hotkeys.items()