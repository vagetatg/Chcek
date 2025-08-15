import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = int(os.getenv("API_ID", 23255238))
API_HASH = os.getenv("API_HASH", "009e3d8c1bdc89d5387cdd8fd182ec15")
SESSION = os.getenv("STRING_SESSION", "BQFa2kUAkepbbcmMCuupoE-wOEdFoeuESDjuyYRfGJm3KFUBE16xau9WHt7tOLgJZBvzKOmyrGiMdBoUP1iwSCzK0v8rGeL--JvR-dErDVEtIDCIPUPP9LBQdrixQMyj8jFkS0euhmMh5w4hvRNAAr18IAFR4ACS5Iay4qyD12OZtIpXnofMKs0VMq1wSGwGr9C0THM8pTDzFmnHrnaDzNX6uRYkkjIf4l57EFVzXScUFB5GaQF03IpzSqybbzB_q2CBOVNgHgTGAuhhny_n6-xIYC65Wbm_RJkAU_mEBOmVlslhnsn2_DpgcdzMgFdlmN2mgYNsaIptkUKr7VoJ-j72ttMK0QAAAAGreD5iAA")
OWNER_ID = int(os.getenv("OWNER_ID", "7078181502"))
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID", "-1002025076123"))

app = Client(
    name="userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    in_memory=True
)

@app.on_message(filters.command("start") & filters.user(OWNER_ID))
async def start_sending_checks(client: Client, message: Message):
    await message.reply("✅ Starting test messages...", quote=True)
    for i in range(1, 4500):
        text_msg = f"/check {i}"
        try:
            await client.send_message(TARGET_CHAT_ID, text_msg)
            await asyncio.sleep(10)
        except Exception as e:
            await message.reply(f"❌ Error at {i}: {e}", quote=True)
            break
    await message.reply("✅ Finished test sending!", quote=True)

if __name__ == "__main__":
    app.run()
