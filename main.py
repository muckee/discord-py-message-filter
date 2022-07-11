import os, json, re
from os.path import join, dirname
from dotenv import load_dotenv
import interactions

# Load environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Get value of DISCORD_TOKEN from environment variables
token = os.environ.get('DISCORD_TOKEN')

# Get list of admin role IDs from environment variables. Messages from users with these roles will not be filtered
# If no roles are provided, only the administrator and owners will be allowed to bypass message filters
admin_role_ids = os.environ.get('DISCORD_ADMIN_ROLE_IDS')
admin_role_id_list = []
if admin_role_ids != '':
    admin_role_id_list = list(map(str.strip, admin_role_ids.split(',')))

# Get list of listenable channel IDs from .env
# If value of environment variable is '*', all channels will be filtered
channel_ids = os.environ.get('DISCORD_CHANNEL_IDS')
channel_id_list = []
if not channel_ids == '*':
    channel_id_list = list(map(str.strip, channel_ids.split(',')))

# Get list of message filters from './expressions.json'
expressions_file = open('expressions.json')
expressions_data = (json.load(expressions_file))['expressions']

# Initialise discord bot with token from .env and necessary intents
bot = interactions.Client(
    token=token,
    intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT,
)

@bot.event(name="on_ready")
async def on_ready():
    print('ready')

# Listen to all messages
@bot.event(name="on_message_create")
async def on_message_create(message: interactions.Message):
    # Whenever we specify any other event type that isn't "READY," the function underneath
    # the decorator will most likely have an argument required. This argument is the data
    # that is being supplied back to us developers, which we call a data model.

    # In this example, we're listening to messages being created. This means we can expect
    # a "message" argument to be passed to the function, which will be the data model of such.

    # We can use the data model to access the data we need.
    # Keep in mind that you can only access the message content if your bot has the MESSAGE_CONTENT intent.
    # You can find more information on this in the migration section of the quickstart guide.

    # Check if user has permission to bypass message filters (admin, elevated role)
    has_permission = False
    guild = await message.get_guild()

    # if message.member.id == guild.owner_id:
    #     has_permission = True

    # Check if user has not already been granted permission
    if not has_permission:
        # Compare all user roles against approved roles
        for role in message.member.roles:

            # if str(role) in admin_role_id_list:
            #     has_permission = True
            #     print('has permission')
            #     break

            guildRole = next((r for r in guild.roles if r.id == role), None)

            # print(guildRole.permissions)
            if guildRole != None:
                print(guildRole)
                if int(guildRole.permissions) & interactions.Permissions.ADMINISTRATOR:
                    has_permission = True
                    break

    # Check if all channels are monitored and if the current channel ID is not filtered
    channel_is_monitored = True
    if len(channel_id_list) and str(message.channel_id) not in channel_id_list:
        channel_is_monitored = False
        print('is monitored')

    print('hit 1')
    # If all checks fail, filter the message
    if not has_permission and channel_is_monitored:

        # Iterate over all regular expressions
        for expression in expressions_data:

            if(expression['type'] == 'string'):
                res = message.content.find(expression['expression'])
                if res > -1:
                    await message.delete(
                        reason='Contains disallowed expression: ' + expression['expression']
                    )
                    break

            elif(expression['type'] == 'regex'):
                # Search regular expression within message
                res = re.search(expression['expression'], message.content)

                # If result was found
                if not res == None:

                    # Delete message
                    await message.delete(
                        reason='Contains disallowed expression: ' + expression['expression']
                    )
                    break

    print(
        f"We've received a message from {message.author.username}. The message is: {str(message.content)}."
    )

# Run bot
bot.start()