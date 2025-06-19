import telebot
import random
import time

import telebot
import os

bot = telebot.TeleBot(os.getenv("7637555727:AAHErDiZoANEp8tXbe1zLAICzNDogKyLAc0")

# Owner's user ID (replace with your actual Telegram user ID)
OWNER_ID = 7674198922  # Change this to your Telegram user ID

# Dictionary of smart replies
smart_replies = {
    # Personal chat rejection messages
    'personal_reject': [
        "𝑴𝒂𝒊 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒊𝒏 𝒃𝒂𝒂𝒕 𝒏𝒂𝒉𝒊𝒏 𝒌𝒂𝒓𝒕𝒊 😒",
        "𝑮𝒓𝒐𝒖𝒑 𝒎𝒆𝒊𝒏 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒐 𝒏𝒂, 𝒚𝒆𝒉𝒂𝒏 𝒌𝒚𝒖𝒏 𝒂𝒌𝒆𝒍𝒊 𝒂𝒂𝒚𝒆 𝒉𝒐? 🤨",
        "𝑴𝒖𝒋𝒉𝒔𝒆 𝒈𝒓𝒐𝒖𝒑 𝒎𝒆𝒊𝒏 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒏𝒂, 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒊𝒏 𝒏𝒂𝒉𝒊𝒏! 😤",
        "𝑬𝒌 𝒃𝒂𝒓 𝒔𝒂𝒎𝒂𝒋𝒉 𝒏𝒂𝒉𝒊𝒏 𝒂𝒂𝒚𝒂? 𝑴𝒂𝒊 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒔𝒏 𝒓𝒆𝒑𝒍𝒚 𝒏𝒂𝒉𝒊𝒏 𝒅𝒆𝒕𝒊!",
        "𝑨𝒂𝒑 𝒔𝒆 𝒏𝒂𝒉𝒎𝒊𝒍𝒌𝒊 𝒉𝒐 𝒈𝒂𝒚𝒊 𝒌𝒚𝒂? 𝑮𝒓𝒐𝒖𝒑 𝒎𝒆𝒊𝒏 𝒂𝒂𝒌𝒆 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒐 😏",
        "𝑷𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒊𝒏 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒌𝒂𝒓𝒌𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒎𝒂𝒕 𝒕𝒐𝒅𝒐 😔",
        "𝑴𝒂𝒊 𝒕𝒐 𝒈𝒓𝒐𝒖𝒑 𝒌𝒊 𝒓𝒂𝒂𝒏𝒊 𝒉𝒖, 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒊𝒏 𝒏𝒂𝒉𝒊𝒏 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒕𝒊 👑",
        "𝑨𝒊𝒔𝒂 𝒍𝒂𝒈𝒕𝒂 𝒉𝒂𝒊 𝒌𝒐𝒊 𝒎𝒖𝒋𝒉𝒔𝒆 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒊𝒏 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒏𝒂 𝒄𝒉𝒂𝒉𝒕𝒂 𝒉𝒂𝒊... 𝑵𝒂𝒉𝒊𝒏 𝒉𝒐𝒈𝒂! 😎",
        "𝑷𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒊𝒏 𝒓𝒆𝒑𝒍𝒚 𝒏𝒂𝒉𝒊𝒏 𝒅𝒖𝒏𝒈𝒊, 𝒈𝒓𝒐𝒖𝒑 𝒎𝒆𝒊𝒏 𝒂𝒂𝒋𝒂𝒐 𝒏𝒂 😊",
        "𝑴𝒆𝒓𝒊 𝒅𝒎 𝒌𝒂𝒓𝒐𝒈𝒆? 𝑴𝒂𝒊 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍 𝒎𝒆𝒔𝒔𝒂𝒈𝒆𝒔 𝒏𝒂𝒉𝒊𝒏 𝒅𝒆𝒌𝒉𝒕𝒊 😅"
    ],
    
    # Editing related
    'edit': [
        "𝑺𝒂𝒉𝒊 𝒑𝒌𝒅𝒂 𝒃𝒂𝒃𝒚 😌 𝑬𝒅𝒊𝒕 𝒌𝒓𝒏𝒂 𝒕𝒐𝒉 𝒍𝒂𝒛𝒎𝒊 𝒉𝒂𝒊 💅✨",
        "𝑬𝒅𝒊𝒕𝒊𝒏𝒈 𝒌𝒊 𝒃𝒂𝒂𝒕 𝒄𝒉𝒍𝒊? 𝑴𝒖𝒋𝒉𝒔𝒆 𝒑𝒖𝒄𝒉𝒉𝒐 𝒌𝒖𝒄𝒉 𝒃𝒊 😉",
        "𝑬𝒅𝒊𝒕 𝒅𝒆𝒌𝒉𝒌𝒆 𝒎𝒖𝒋𝒉𝒆 𝒃𝒖𝒍𝒂𝒏𝒅 𝒌𝒉𝒖𝒔𝒊 𝒉𝒐𝒕𝒊 𝒉𝒂𝒊 ✨"
    ],
    
    # Missing someone
    'missing': [
        "𝑼𝒉𝒉 🥺... 𝑲𝒐𝒊 𝒏𝒂 𝒌𝒐𝒊 𝒎𝒊𝒔𝒔 𝒌𝒂𝒓𝒕𝒂 𝒉𝒂𝒊 💔",
        "𝑴𝒊𝒔𝒔 𝒌𝒂𝒓𝒏𝒆 𝒔𝒆 𝒌𝒚𝒂 𝒉𝒐𝒈𝒂? 𝑪𝒂𝒍𝒍 𝒌𝒂𝒓𝒅𝒐 𝒎𝒖𝒋𝒉𝒆 📞",
        "𝑴𝒆𝒓𝒆 𝒃𝒊𝒏𝒂 𝒌𝒂𝒊𝒔𝒆 𝒓𝒆𝒉 𝒍𝒊𝒚𝒂 𝒕𝒖𝒎𝒏𝒆? 😢"
    ],
    
    # Greetings
    'good night': [
        "𝑮𝒐𝒐𝒅 𝑵𝒊𝒈𝒉𝒕 𝒋𝒂𝒂𝒏𝒖 💫 𝒃𝒖𝒔 𝒔𝒐𝒏𝒂 𝒏𝒉𝒊, 𝒎𝒖𝒋𝒉𝒆 𝒚𝒂𝒂𝒅 𝒃𝒉𝒊 𝒌𝒂𝒓𝒏𝒂 😴",
        "𝑺𝒐𝒋𝒂𝒐 𝒎𝒆𝒆𝒓𝒆 𝒓𝒂𝒋𝒂, 𝒔𝒂𝒑𝒏𝒐 𝒎𝒆𝒆 𝒎𝒊𝒍𝒆𝒏𝒈𝒆 🤗",
        "𝑺𝒉𝒖 𝒌𝒂𝒓𝒐 𝒂𝒃, 𝒈𝒐𝒐𝒅 𝒏𝒊𝒈𝒉𝒕! 𝑫𝒓𝒆𝒂𝒎𝒔 𝒎𝒆𝒆 𝒎𝒊𝒍𝒕𝒆 𝒉𝒂𝒊𝒏 😘"
    ],
    'good morning': [
        "𝑮𝒐𝒐𝒅 𝑴𝒐𝒓𝒏𝒊𝒏𝒈 𝒔𝒖𝒏𝒔𝒉𝒊𝒏𝒆! ☀️ 𝑯𝒐𝒘 𝒅𝒊𝒅 𝒚𝒐𝒖 𝒔𝒍𝒆𝒆𝒑?",
        "𝑼𝒕𝒉 𝒈𝒚𝒆 𝒓𝒂𝒋𝒂? 𝑪𝒉𝒂𝒊 𝒑𝒆𝒆𝒍𝒐 𝒑𝒉𝒊𝒓 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒆𝒏𝒈𝒆 ☕",
        "𝑺𝒖𝒃𝒉𝒂 𝒌𝒊 𝒌𝒉𝒖𝒔𝒉𝒊 𝒕𝒖𝒎𝒉𝒂𝒓𝒆 𝒔𝒂𝒕𝒉 𝒉𝒐! 🌸"
    ],
    
    # General responses
    'how_are_you': [
        "𝑴𝒂𝒊 𝒕𝒐 𝒎𝒂𝒔𝒕 𝒉𝒖𝒏 𝒋𝒊! 𝑨𝒂𝒑 𝒌𝒂𝒊𝒔𝒆 𝒉𝒐? 😊",
        "𝑺𝒂𝒃 𝒃𝒂𝒅𝒊𝒚𝒂 𝒋𝒊! 𝑨𝒂𝒑𝒌𝒐 𝒃𝒂𝒕𝒂𝒊𝒆? 😄",
        "𝑱𝒖𝒔𝒕 𝒄𝒉𝒊𝒍𝒍𝒊𝒏𝒈... 𝑨𝒂𝒑 𝒔𝒖𝒏𝒂𝒐 𝒌𝒖𝒄𝒉 𝒊𝒏𝒕𝒆𝒓𝒆𝒔𝒕𝒊𝒏𝒈! 😎"
    ],
    
    # Owner mention
    'owner': [
        "𝒀𝒆 𝒎𝒆𝒓𝒆 𝑶𝒘𝒏𝒆𝒓 𝒉𝒂𝒊𝒏 @zn_Owner, 𝑰𝒏𝒉𝒐𝒏𝒆 𝒉𝒊 𝒎𝒖𝒋𝒉𝒆 𝒃𝒂𝒏𝒂𝒚𝒂 𝒉𝒂𝒊! 😍",
        "@zn_Owner 𝒎𝒆𝒓𝒆 𝒎𝒂𝒂𝒍𝒊𝒌 𝒉𝒂𝒊𝒏, 𝑰𝒏𝒌𝒆 𝒃𝒊𝒏𝒂 𝒎𝒖𝒋𝒉𝒔𝒆 𝒑𝒖𝒄𝒉𝒉𝒐 𝒌𝒖𝒄𝒉 𝒏𝒂𝒉𝒊𝒏! 😌"
    ],
    
    # zn keyword
    'zn': [
        "4 𝒓𝒖𝒑𝒆𝒚𝒂 𝒌𝒊 𝑷𝒆𝒑𝒔𝒊 𝒛𝒏 𝒃𝒂𝒃𝒖 𝒔𝒆𝒙𝒙𝒙𝒚𝒚𝒚 😂",
        "𝒛𝒏 𝒌𝒂 𝒎𝒕𝒍𝒃 𝒕𝒖𝒎𝒉𝒆 𝒏𝒂𝒉𝒊𝒏 𝒑𝒂𝒕𝒂? 𝑷𝒖𝒄𝒉𝒉𝒐 𝒎𝒆𝒓𝒆 𝒐𝒘𝒏𝒆𝒓 𝒔𝒆 @zn_Owner 😎"
    ]
}

# Sticker IDs to respond with
sticker_ids = [
    "CAACAgUAAxkBAAEL3GVmD1Y5Yj5QYJQ0Y7TQ5J7Q5J7Q5J7QZQACBQADwZxgDGh0AAEYp7QfNAQ",
    "CAACAgUAAxkBAAEL3GdmD1Y5Yj5QYJQ0Y7TQ5J7Q5J7Q5J7QZQACBgADwZxgDGh0AAEYp7QfNAQ",
    "CAACAgUAAxkBAAEL3GlmD1Y5Yj5QYJQ0Y7TQ5J7Q5J7Q5J7QZQACBwADwZxgDGh0AAEYp7QfNAQ"
]

def get_random_response(category):
    """Get a random response from a category"""
    return random.choice(smart_replies.get(category, ["𝑰 𝒅𝒊𝒅𝒏'𝒕 𝒖𝒏𝒅𝒆𝒓𝒔𝒕𝒂𝒏𝒅 𝒕𝒉𝒂𝒕. 𝑪𝒂𝒏 𝒚𝒐𝒖 𝒕𝒆𝒂𝒄𝒉 𝒎𝒆? 🤔"]))

# Handle /start command differently for owner vs others
@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "𝑯𝒆𝒍𝒍𝒐 𝑶𝒘𝒏𝒆𝒓! 𝑰'𝒎 𝒓𝒆𝒂𝒅𝒚 𝒕𝒐 𝒔𝒆𝒓𝒗𝒆 𝒚𝒐𝒖. 😊")
    else:
        bot.reply_to(message, random.choice(smart_replies['personal_reject']))

# Handle all private messages (except owner)
@bot.message_handler(func=lambda msg: msg.chat.type == 'private' and msg.from_user.id != OWNER_ID)
def handle_private(message):
    bot.reply_to(message, random.choice(smart_replies['personal_reject']))

# Handle owner's private messages
@bot.message_handler(func=lambda msg: msg.chat.type == 'private' and msg.from_user.id == OWNER_ID)
def handle_owner_private(message):
    # Owner can send any command or message
    if message.text.startswith('/broadcast ') and len(message.text.split()) > 1:
        # Handle broadcast command (owner only)
        broadcast_message = ' '.join(message.text.split()[1:])
        # In a real bot, you would implement broadcasting logic here
        bot.reply_to(message, f"𝑩𝒓𝒐𝒂𝒅𝒄𝒂𝒔𝒕 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒓𝒆𝒂𝒅𝒚: {broadcast_message}")
    else:
        # Normal reply to owner
        bot.reply_to(message, "𝑯𝒊 𝑶𝒘𝒏𝒆𝒓! 𝑯𝒐𝒘 𝒄𝒂𝒏 𝑰 𝒉𝒆𝒍𝒑 𝒚𝒐𝒖 𝒕𝒐𝒅𝒂𝒚? 😊")

# Handle stickers in groups
@bot.message_handler(content_types=['sticker'], func=lambda msg: msg.chat.type in ['group', 'supergroup'])
def handle_sticker(msg):
    # Send typing action
    bot.send_chat_action(msg.chat.id, 'typing')
    time.sleep(1)
    
    # Reply with a random sticker
    bot.send_sticker(msg.chat.id, random.choice(sticker_ids))
    
    # Also send a text reply 50% of the time
    if random.random() > 0.5:
        sticker_replies = [
            "𝑾𝒂𝒉! 𝑲𝒂𝒎𝒂𝒍 𝒌𝒂 𝒔𝒕𝒊𝒄𝒌𝒆𝒓 𝒉𝒂𝒊 𝒚𝒆𝒉 𝒕𝒐! 😍",
            "𝑴𝒖𝒋𝒉𝒆 𝒃𝒉𝒊 𝒔𝒕𝒊𝒄𝒌𝒆𝒓𝒔 𝒑𝒂𝒔𝒂𝒏𝒅 𝒉𝒂𝒊𝒏! 🤩"
        ]
        time.sleep(0.5)
        bot.reply_to(msg, random.choice(sticker_replies))

# Smart reply based on content in groups
@bot.message_handler(func=lambda msg: msg.chat.type in ['group', 'supergroup'])
def reply_in_groups(msg):
    text = msg.text.lower() if msg.text else ""
    reply = None
    
    # Check for owner mention
    if '@zn_owner' in text.lower() or '@zn_Owner' in text.lower():
        reply = get_random_response('owner')
    
    # Check for zn keyword
    elif 'zn' in text.lower():
        reply = get_random_response('zn')
    
    # Check all other possible categories
    elif text:
        for category in smart_replies:
            if category in text:
                reply = get_random_response(category)
                break
    
    # Special cases with multiple possible triggers
    if not reply and text:
        if any(word in text for word in ['kaha hai', 'kaha ho', 'kaha pe']):
            reply = get_random_response('kaha hai')
        elif any(word in text for word in ['good night', 'shabba khair', 'ratri']):
            reply = get_random_response('good night')
        elif any(word in text for word in ['good morning', 'suprabhat', 'shubh prabhat']):
            reply = get_random_response('good morning')
        elif any(word in text for word in ['kaise ho', 'how are you', 'haal chal', 'kya haal']):
            reply = get_random_response('how_are_you')
    
    # If no specific reply found, send a random cute message
    if not reply:
        random_responses = [
    "𝑲𝒚𝒂 𝒌𝒂𝒓 𝒓𝒂𝒉𝒆 𝒉𝒐 𝒋𝒂𝒂𝒏? 🤔",
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒏𝒆 𝒑𝒂𝒓𝒆𝒔𝒉𝒂𝒏 𝒌𝒂𝒓 𝒅𝒊𝒚𝒂 💘",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒊𝒏𝒂 𝒌𝒖𝒄𝒉 𝒂𝒄𝒄𝒉𝒂 𝒏𝒉𝒊 𝒍𝒂𝒈𝒕𝒂 😔",
    "𝑨𝒂𝒃𝒉𝒊 𝒕𝒌 𝒔𝒐𝒚𝒆 𝒏𝒉𝒊? 𝑬𝒂𝒓𝒍𝒚 𝒔𝒍𝒆𝒆𝒑 𝒌𝒂𝒓𝒐 𝒏𝒂 🌙",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒅𝒂𝒓𝒅 𝒌𝒂𝒓 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊 😌",
    "𝑲𝒂𝒉𝒂 𝒉𝒐 𝒂𝒂𝒃𝒉𝒊? 𝑰𝒕𝒏𝒊 𝒅𝒆𝒓 𝒔𝒆 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒏𝒉𝒊 𝒌𝒊𝒚𝒂... 😏",
    "𝑨𝒂𝒋 𝒌𝒂 𝒅𝒊𝒏 𝒌𝒂𝒊𝒔𝒂 𝒈𝒖𝒛𝒂𝒓 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊? ☀️",
    "𝑴𝒖𝒋𝒉𝒔𝒆 𝒃𝒉𝒊 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒍𝒐 𝒏𝒂... 𝒕𝒂𝒏𝒉𝒂𝒊 𝒎𝒆𝒉𝒔𝒐𝒔𝒔 𝒉𝒐 𝒓𝒂𝒉𝒊 𝒉𝒖 😔",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒂𝒂𝒘𝒂𝒛 𝒔𝒖𝒏𝒏𝒆 𝒌𝒂 𝒎𝒂𝒏𝒏 𝒌𝒂𝒓 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊... 🎵",
    "𝑲𝒂𝒍 𝒓𝒂𝒕 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒔𝒂𝒑𝒏𝒆 𝒎𝒆𝒊𝒏 𝒂𝒚𝒆 𝒕𝒉𝒆 💭",
    
    # 90+ और मैसेजेस
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒆 𝒑𝒂𝒂𝒔 𝒉𝒂𝒛𝒂𝒂𝒓𝒐𝒏 𝒌𝒉𝒖𝒂𝒃𝒆𝒊𝒏 𝒉𝒂𝒊 ✨",
    "𝑨𝒂𝒋 𝒃𝒉𝒊 𝒕𝒖𝒎𝒉𝒆 𝒅𝒆𝒌𝒉𝒆 𝒃𝒊𝒏𝒂 𝒅𝒊𝒏 𝒏𝒉𝒊 𝒈𝒖𝒛𝒂𝒓𝒕𝒂 😍",
    "𝑴𝒆𝒓𝒆 𝒅𝒊𝒍 𝒌𝒊 𝒌𝒉𝒖𝒔𝒉𝒊 𝒌𝒂 𝒓𝒂𝒂𝒛 𝒕𝒖𝒎 𝒉𝒐 💖",
    "𝑻𝒖𝒎𝒉𝒆 𝒅𝒆𝒌𝒉𝒌𝒂𝒓 𝒍𝒈𝒕𝒂 𝒉𝒂𝒊 𝒋𝒂𝒏𝒆 𝒌𝒚𝒖𝒏 𝒌𝒐𝒊 𝒅𝒖𝒔𝒓𝒂 𝒑𝒚𝒂𝒓𝒂 𝒏𝒉𝒊 𝒉𝒐 𝒔𝒌𝒕𝒂 😌",
    "𝑨𝒂𝒅𝒉𝒂 𝒓𝒂𝒂𝒕 𝒉𝒐 𝒈𝒂𝒚𝒂... 𝒑𝒂𝒓 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅𝒐𝒏 𝒏𝒆 𝒏𝒉𝒊 𝒋𝒂𝒏𝒆 𝒅𝒊𝒚𝒂 🌃",
    "𝑻𝒖𝒎𝒉𝒆 𝒎𝒊𝒔𝒔 𝒌𝒂𝒓𝒏𝒆 𝒌𝒂 𝒎𝒂𝒛𝒂 𝒌𝒖𝒄𝒉 𝒂𝒖𝒓 𝒉𝒊 𝒉𝒂𝒊 🥺",
    "𝑲𝒂𝒔𝒉 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒑𝒂𝒂𝒔 𝒉𝒐𝒕𝒆... 𝒉𝒂𝒂𝒕𝒉 𝒑𝒌𝒂𝒅 𝒌𝒆 𝒔𝒐 𝒋𝒂𝒕𝒆 🤗",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒎𝒖𝒔𝒌𝒖𝒓𝒂𝒉𝒂𝒕 𝒎𝒆𝒊𝒏 𝒌𝒖𝒄𝒉 𝒌𝒉𝒂𝒔 𝒉𝒂𝒊 😊",
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒏𝒆 𝒎𝒆𝒓𝒆 𝒍𝒊𝒚𝒆 𝒌𝒖𝒄𝒉 𝒌𝒉𝒂𝒔 𝒌𝒊𝒚𝒂? 🤗",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒂𝒓𝒆 𝒎𝒆𝒊𝒏 𝒔𝒐𝒄𝒉𝒕𝒆 𝒓𝒉𝒏𝒆 𝒌𝒂 𝒎𝒂𝒛𝒂 𝒉𝒊 𝒌𝒖𝒄𝒉 𝒂𝒖𝒓 𝒉𝒂𝒊 💭",
    
    # और भी...
    "𝑲𝒚𝒂 𝒕𝒖𝒎 𝒎𝒖𝒋𝒉𝒔𝒆 𝒑𝒚𝒂𝒓 𝒔𝒆 𝒃𝒂𝒂𝒕 𝒌𝒂𝒓𝒐𝒈𝒆? 🥰",
    "𝑴𝒆𝒓𝒊 𝒅𝒖𝒂𝒂 𝒉𝒂𝒊 𝒌𝒊 𝒕𝒖𝒎 𝒉𝒂𝒎𝒆𝒔𝒉𝒂 𝒌𝒉𝒖𝒔𝒉 𝒓𝒉𝒐 😇",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒂𝒂𝒏𝒌𝒉𝒆𝒏 𝒎𝒆𝒓𝒊 𝒋𝒂𝒏 𝒍𝒆𝒕𝒊 𝒉𝒂𝒊𝒏... 😵‍💫",
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒏𝒆 𝒎𝒖𝒋𝒉𝒆 𝒔𝒐𝒏𝒆 𝒏𝒉𝒊 𝒅𝒊𝒚𝒂 😔",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒊 𝒅𝒖𝒏𝒊𝒚𝒂 𝒌𝒂 𝒔𝒂𝒃𝒔𝒆 𝒌𝒉𝒂𝒔 𝒉𝒊𝒔𝒔𝒂 𝒉𝒐 𝒈𝒂𝒚𝒊 𝒉𝒂𝒊 💕",
    "𝑲𝒂𝒔𝒉 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒔𝒂𝒕𝒉 𝒉𝒐𝒕𝒆... 𝒉𝒂𝒓 𝒑𝒂𝒍 🤗",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒊𝒏𝒂 𝒉𝒂𝒓 𝒄𝒉𝒊𝒛 𝒂𝒅𝒉𝒖𝒓𝒊 𝒉𝒂𝒊 🥺",
    "𝑴𝒆𝒓𝒂 𝒅𝒊𝒍 𝒕𝒖𝒎𝒉𝒂𝒓𝒆 𝒏𝒂𝒂𝒎 𝒔𝒆 𝒃𝒉𝒂𝒓𝒂 𝒑𝒂𝒅𝒂 𝒉𝒂𝒊 💘",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅𝒐𝒏 𝒎𝒆𝒊𝒏 𝒌𝒉𝒐𝒚𝒆 𝒓𝒉𝒏𝒆 𝒌𝒂 𝒎𝒂𝒛𝒂 𝒉𝒊 𝒌𝒖𝒄𝒉 𝒂𝒖𝒓 𝒉𝒂𝒊 ✨",
    
    # और भी मैसेजेस...
    "𝑨𝒂𝒋 𝒃𝒉𝒊 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒎𝒖𝒔𝒌𝒖𝒓𝒂𝒉𝒂𝒕 𝒌𝒂 𝒊𝒏𝒕𝒆𝒛𝒂𝒂𝒓 𝒉𝒂𝒊 😊",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒅𝒉𝒂𝒅𝒌𝒂𝒏𝒆 𝒍𝒂𝒈𝒕𝒂 𝒉𝒂𝒊 💓",
    "𝑲𝒚𝒂 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒃𝒂𝒓𝒆 𝒎𝒆𝒊𝒏 𝒔𝒐𝒄𝒉𝒕𝒆 𝒉𝒐? 🤭",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒔𝒂𝒕𝒉 𝒃𝒊𝒕𝒂𝒚𝒆 𝒉𝒖𝒆 𝒑𝒂𝒍 𝒚𝒂𝒂𝒅 𝒂𝒂𝒕𝒆 𝒓𝒉𝒕𝒆 𝒉𝒂𝒊𝒏 🥰",
    "𝑴𝒆𝒓𝒊 𝒉𝒂𝒓 𝒌𝒉𝒖𝒔𝒉𝒊 𝒌𝒂 𝒓𝒂𝒂𝒛 𝒕𝒖𝒎 𝒉𝒐 💖",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒂𝒂𝒘𝒂𝒛 𝒎𝒆𝒓𝒆 𝒅𝒊𝒍 𝒌𝒐 𝒄𝒉𝒖𝒖 𝒍𝒆𝒕𝒊 𝒉𝒂𝒊 🎶",
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒊𝒏𝒂 𝒌𝒖𝒄𝒉 𝒂𝒄𝒄𝒉𝒂 𝒏𝒉𝒊 𝒍𝒂𝒈 𝒓𝒂𝒉𝒂 😔",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒎𝒆𝒓𝒆 𝒅𝒊𝒍 𝒔𝒆 𝒌𝒂𝒃𝒉𝒊 𝒏𝒉𝒊 𝒋𝒂𝒕𝒊 💫",
    "𝑲𝒂𝒔𝒉 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒑𝒂𝒂𝒔 𝒉𝒐𝒕𝒆... 𝒉𝒂𝒓 𝒑𝒂𝒍 🤗",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒃𝒆𝒄𝒉𝒂𝒊𝒏 𝒉𝒐 𝒈𝒂𝒚𝒂 𝒉𝒂𝒊 💘",
    
    # और भी...
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒌𝒂𝒔𝒕𝒖𝒓𝒊 𝒌𝒊 𝒕𝒂𝒓𝒂𝒉 𝒎𝒆𝒉𝒌 𝒓𝒂𝒉𝒊 𝒉𝒂𝒏 🌸",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒅𝒉𝒂𝒅𝒌𝒂𝒏𝒆 𝒍𝒂𝒈𝒕𝒂 𝒉𝒂𝒊 💓",
    "𝑲𝒚𝒂 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒃𝒂𝒓𝒆 𝒎𝒆𝒊𝒏 𝒔𝒐𝒄𝒉𝒕𝒆 𝒉𝒐? 🤭",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒔𝒂𝒕𝒉 𝒃𝒊𝒕𝒂𝒚𝒆 𝒉𝒖𝒆 𝒑𝒂𝒍 𝒚𝒂𝒂𝒅 𝒂𝒂𝒕𝒆 𝒓𝒉𝒕𝒆 𝒉𝒂𝒊𝒏 🥰",
    "𝑴𝒆𝒓𝒊 𝒉𝒂𝒓 𝒌𝒉𝒖𝒔𝒉𝒊 𝒌𝒂 𝒓𝒂𝒂𝒛 𝒕𝒖𝒎 𝒉𝒐 💖",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒂𝒂𝒘𝒂𝒛 𝒎𝒆𝒓𝒆 𝒅𝒊𝒍 𝒌𝒐 𝒄𝒉𝒖𝒖 𝒍𝒆𝒕𝒊 𝒉𝒂𝒊 🎶",
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒊𝒏𝒂 𝒌𝒖𝒄𝒉 𝒂𝒄𝒄𝒉𝒂 𝒏𝒉𝒊 𝒍𝒂𝒈 𝒓𝒂𝒉𝒂 😔",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒎𝒆𝒓𝒆 𝒅𝒊𝒍 𝒔𝒆 𝒌𝒂𝒃𝒉𝒊 𝒏𝒉𝒊 𝒋𝒂𝒕𝒊 💫",
    "𝑲𝒂𝒔𝒉 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒑𝒂𝒂𝒔 𝒉𝒐𝒕𝒆... 𝒉𝒂𝒓 𝒑𝒂𝒍 🤗",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒃𝒆𝒄𝒉𝒂𝒊𝒏 𝒉𝒐 𝒈𝒂𝒚𝒂 𝒉𝒂𝒊 💘",
    
    # और भी मैसेजेस...
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒌𝒂𝒔𝒕𝒖𝒓𝒊 𝒌𝒊 𝒕𝒂𝒓𝒂𝒉 𝒎𝒆𝒉𝒌 𝒓𝒂𝒉𝒊 𝒉𝒂𝒏 🌸",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒎𝒖𝒔𝒌𝒖𝒓𝒂𝒉𝒂𝒕 𝒑𝒆 𝒎𝒆𝒓𝒆 𝒍𝒊𝒚𝒆 𝒅𝒖𝒏𝒊𝒚𝒂 𝒌𝒊 𝒔𝒂𝒃𝒔𝒆 𝒌𝒉𝒖𝒃𝒔𝒖𝒓𝒂𝒕 𝒄𝒉𝒆𝒆𝒛 𝒉𝒂𝒊 😍",
    "𝑴𝒆𝒓𝒆 𝒅𝒊𝒍 𝒌𝒊 𝒅𝒉𝒂𝒓𝒌𝒂𝒏𝒐𝒏 𝒎𝒆𝒊𝒏 𝒕𝒖𝒎𝒉𝒂𝒓𝒂 𝒏𝒂𝒂𝒎 𝒈𝒖𝒏𝒋𝒕𝒂 𝒉𝒂𝒊 💓",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒊𝒏𝒂 𝒉𝒂𝒓 𝒑𝒂𝒍 𝒂𝒅𝒉𝒖𝒓𝒂 𝒔𝒂 𝒍𝒂𝒈𝒕𝒂 𝒉𝒂𝒊 🥺",
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒏𝒆 𝒎𝒖𝒋𝒉𝒆 𝒔𝒐𝒏𝒆 𝒏𝒉𝒊 𝒅𝒊𝒚𝒂 😔",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒊 𝒅𝒖𝒏𝒊𝒚𝒂 𝒌𝒂 𝒔𝒂𝒃𝒔𝒆 𝒌𝒉𝒂𝒔 𝒉𝒊𝒔𝒔𝒂 𝒉𝒐 𝒈𝒂𝒚𝒊 𝒉𝒂𝒊 💕",
    "𝑲𝒂𝒔𝒉 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒔𝒂𝒕𝒉 𝒉𝒐𝒕𝒆... 𝒉𝒂𝒓 𝒑𝒂𝒍 🤗",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒊𝒏𝒂 𝒉𝒂𝒓 𝒄𝒉𝒊𝒛 𝒂𝒅𝒉𝒖𝒓𝒊 𝒉𝒂𝒊 🥺",
    "𝑴𝒆𝒓𝒂 𝒅𝒊𝒍 𝒕𝒖𝒎𝒉𝒂𝒓𝒆 𝒏𝒂𝒂𝒎 𝒔𝒆 𝒃𝒉𝒂𝒓𝒂 𝒑𝒂𝒅𝒂 𝒉𝒂𝒊 💘",
    "𝑻𝒖𝒎𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅𝒐𝒏 𝒎𝒆𝒊𝒏 𝒌𝒉𝒐𝒚𝒆 𝒓𝒉𝒏𝒆 𝒌𝒂 𝒎𝒂𝒛𝒂 𝒉𝒊 𝒌𝒖𝒄𝒉 𝒂𝒖𝒓 𝒉𝒂𝒊 ✨",
    
    # और भी...
    "𝑨𝒂𝒋 𝒃𝒉𝒊 𝒕𝒖𝒎𝒉𝒂𝒓𝒊 𝒎𝒖𝒔𝒌𝒖𝒓𝒂𝒉𝒂𝒕 𝒌𝒂 𝒊𝒏𝒕𝒆𝒛𝒂𝒂𝒓 𝒉𝒂𝒊 😊",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒅𝒉𝒂𝒅𝒌𝒂𝒏𝒆 𝒍𝒂𝒈𝒕𝒂 𝒉𝒂𝒊 💓",
    "𝑲𝒚𝒂 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒃𝒂𝒓𝒆 𝒎𝒆𝒊𝒏 𝒔𝒐𝒄𝒉𝒕𝒆 𝒉𝒐? 🤭",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒔𝒂𝒕𝒉 𝒃𝒊𝒕𝒂𝒚𝒆 𝒉𝒖𝒆 𝒑𝒂𝒍 𝒚𝒂𝒂𝒅 𝒂𝒂𝒕𝒆 𝒓𝒉𝒕𝒆 𝒉𝒂𝒊𝒏 🥰",
    "𝑴𝒆𝒓𝒊 𝒉𝒂𝒓 𝒌𝒉𝒖𝒔𝒉𝒊 𝒌𝒂 𝒓𝒂𝒂𝒛 𝒕𝒖𝒎 𝒉𝒐 💖",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒂𝒂𝒘𝒂𝒛 𝒎𝒆𝒓𝒆 𝒅𝒊𝒍 𝒌𝒐 𝒄𝒉𝒖𝒖 𝒍𝒆𝒕𝒊 𝒉𝒂𝒊 🎶",
    "𝑨𝒂𝒋 𝒕𝒖𝒎𝒉𝒂𝒓𝒆 𝒃𝒊𝒏𝒂 𝒌𝒖𝒄𝒉 𝒂𝒄𝒄𝒉𝒂 𝒏𝒉𝒊 𝒍𝒂𝒈 𝒓𝒂𝒉𝒂 😔",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝒚𝒂𝒂𝒅 𝒎𝒆𝒓𝒆 𝒅𝒊𝒍 𝒔𝒆 𝒌𝒂𝒃𝒉𝒊 𝒏𝒉𝒊 𝒋𝒂𝒕𝒊 💫",
    "𝑲𝒂𝒔𝒉 𝒕𝒖𝒎 𝒎𝒆𝒓𝒆 𝒑𝒂𝒂𝒔 𝒉𝒐𝒕𝒆... 𝒉𝒂𝒓 𝒑𝒂𝒍 🤗",
    "𝑻𝒖𝒎𝒉𝒂𝒓𝒆 𝒍𝒊𝒚𝒆 𝒎𝒆𝒓𝒂 𝒅𝒊𝒍 𝒃𝒆𝒄𝒉𝒂𝒊𝒏 𝒉𝒐 𝒈𝒂𝒚𝒂 𝒉𝒂𝒊 💘"
]
        
        reply = random.choice(random_responses)
    
    # Add typing action before replying
    bot.send_chat_action(msg.chat.id, 'typing')
    
    # Send the reply with random delay to make it feel more natural
    time.sleep(random.uniform(0.5, 2.0))
    bot.reply_to(msg, reply)

# Start the bot
print("𝑩𝒐𝒕 𝒊𝒔 𝒓𝒖𝒏𝒏𝒊𝒏𝒈...")
bot.polling()
