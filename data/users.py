import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


user = User("Masha WWW", "test@user.ru", "450926, г. Уфа, ул. Трактовая, 30",
            "190576, г. Санкт-Петербург, ул. Горная, 39")
