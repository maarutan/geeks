import os

# from web3 import Web3
from eth_account import Account

# Включаем непроверенные функции HD Wallet
Account.enable_unaudited_hdwallet_features()

from mnemonic import Mnemonic


def create_wallets_bip39(num_wallets, num_words):
    # Создание директории для кошельков, если она не существует
    os.makedirs("wallets", exist_ok=True)

    # Проверяем, что количество слов для seed phrase правильное
    if num_words not in [12, 15, 18, 21, 24]:
        raise ValueError("Number of words must be 12, 15, 18, 21, or 24")

    mnemo = Mnemonic("english")
    for _ in range(num_wallets):
        # Генерируем новый аккаунт
        seed = mnemo.generate(strength=num_words * 32 // 3)
        mnemonic_words = seed
        acc = Account.from_mnemonic(mnemonic_words)
        address = acc.address

        # Создаем файл для каждого адреса
        with open(f"wallets/{address}.txt", "w") as file:
            file.write(mnemonic_words)

    print(f"Generated {num_wallets} wallets in the 'wallets' folder.")


# Количество кошельков для генерации
num_wallets = 50
# Количество слов в seed phrase
num_words = 12

create_wallets_bip39(num_wallets, num_words)
