import reflex as rx

class Device(rx.model, table=True):
    device_id: int
    device_name: str
