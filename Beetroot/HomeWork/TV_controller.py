from .Classes_TV import TV_controller

CHANNELS = ["BBC", "Discovery", "TV1000", "Auto24", "NewsOne"]

controller = TV_controller("Samsung", CHANNELS)

controller.first_channel()
controller.last_channel()
controller.turn_channel(10)
controller.turn_channel(1)
controller.turn_channel(5)
controller.next_channel()
controller.next_channel()
controller.previous_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(1)
controller.is_exist(6)
controller.is_exist('Auto24')
