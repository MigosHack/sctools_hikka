from .. import loader, utils
from telethon import events, functions
from telethon.tl.types import Message

@loader.tds
class JoskiModuleMod(loader.Module):
	"""МегаКрутой модуль"""
	strings = {"name": "SCTOOOOOLS"}
	
	def __init__(self):
		self.tasks = []
		
    @loader.unrestricted
    @loader.ratelimit
    async def sc2pngcmd(self, message):
        """Запустить автоматический фарминг в боте"""
        await message.edit("пашол наху")