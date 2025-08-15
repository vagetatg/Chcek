import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = int(os.getenv("API_ID", 23255238))
API_HASH = os.getenv("API_HASH", "009e3d8c1bdc89d5387cdd8fd182ec15")
SESSION = os.getenv("STRING_SESSION", "BQFa2kUAgJ2vE8ErskR-BaBnUjFLvuqcZZK39CJPAQ7eZHyWnXUk0lInX6aXrvR14LFaKn0PR7bDemFAMTRnCpgxmq1Qc1wmULdR3hLM2fyN1tuqNO2fNFltSD6IXrBOhP-Hcoc-fkgghicu1a2svu1l0RJ_hfgEWZjIsjJcvLXh_yqtbngECV94APUbhcpPCKmHqVA9MOlnEKPYXnA22INedndRNpin0VsRXzDy3Qcg0TyNFZ3DztFKSnMtSDJP3plbFCIAOXxZP1i0ato0WOc0km1aPzbqaFE7tH6aJ8IWKWrdYCYI6Jxsqis1GMnkJpq1VtU8vFtyNkAoU76HXRS1I26bUgAAAAGreD5iAA")
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
    for i in range(1, 6):
        text_msg = f"/check {i}"
        try:
            await client.send_message(TARGET_CHAT_ID, text_msg)
            await asyncio.sleep(10)
        except Exception as e:
            await message.reply(f"❌ Error at {i}: {e}", quote=True)
            break
    await message.reply("✅ Finished test sending!", quote=True)

if name == "main":
    app.run()
