from dataclasses import dataclass

@dataclass
class Address:
    street: str
    city: str
    prefecture: str
    postal_code: str
    country: str = "Japan"  # デフォルト値

    def __str__(self):
        return f"{self.street}, {self.city}, {self.prefecture}, {self.postal_code}, {self.country}"

# インスタンス作成
home_address = Address("1-2-3 Akihabara", "Tokyo", "Tokyo", "100-0001")

# 表示
print(home_address)  # => 1-2-3 Akihabara, Tokyo, Tokyo, 100-0001, Japan
