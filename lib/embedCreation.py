import discord


def embed_Move_Details(char_name, char_url, char_moveIcon, char_imgur, char_move,
                       char_guard, char_dmg, char_startup, char_active, char_recovery, char_advantage, char_notes):

    embed = discord.Embed(title=char_name.title() + " Frame Data (DustLoop)",
                          colour=discord.Colour(0x6342FC),
                          url=char_url,
                          description="**Move: " + char_move + "**\n" + char_moveIcon)

    embed.set_thumbnail(url=char_imgur)
    embed.set_author(name=char_name.title(), url=char_url, icon_url="https://www.fightersgeneration.com/nf/dl/dragonballfighterz.jpg")
    embed.add_field(name="Damage", value=char_dmg)
    embed.add_field(name="Guard", value=char_guard)
    embed.add_field(name="Startup", value=char_startup)
    embed.add_field(name="Active", value=char_active)
    embed.add_field(name="Recovery", value=char_recovery)
    embed.add_field(name="Frame Advantage", value=char_advantage)
    embed.add_field(name="Notes", value=char_notes)

    return embed


def embed_Similar_Moves(similar_Moves_List, char_name, char_url, char_imgur):
    embed = discord.Embed(title=char_name.title() + " Frame Data (RBNorway)",
                          colour=discord.Colour(0xFF5733),
                          url=char_url,
                          description="**Move Not Found.**")
    embed.set_thumbnail(url=char_imgur)
    embed.set_author(name=char_name.title(), url=char_url, icon_url="https://i.imgur.com/9YWQdwE.jpg")

    moveList = ''
    if len(similar_Moves_List) == 0:
        moveList = 'No similar moves found.'
    for moveNum, move in enumerate(similar_Moves_List):
        if moveNum < 9:
            moveList = moveList + move + '\n'

    embed.add_field(name='Similar moves', value=moveList)

    return embed


#This code is for the ~legend command and shows the user all the game notations.
def embed_legend():
    forwardStr = '**f** = forward \t\t<:FORWARD:418969486259912727>'
    backwardStr = '**b** = backward\t<:BACK:418969621748514816>'
    upwardStr = '**u** = up  \t\t\t\t<:UP:418969652136509441>'
    downwardStr = '**d** = down\t\t\t<:DOWN:418969652224458763>'
    directionStr = forwardStr + '\n' + backwardStr + '\n' + upwardStr + '\n' + downwardStr + '\n'

    lpStr = '**1** = Light Attack\t\t   <:1_:418969652148961282>'
    mpStr = '**2** = Medium Attack    <:2_:418969652488699904>'
    hpStr = '**3** = Heavy Attack\t    <:3_:418969652509671424>'
    spStr = '**4** = Special Attack\t  <:4_:418969652488568832>'
    attackStr = lpStr + '\n' + mpStr + '\n' + hpStr + '\n' + spStr

    lmStr = '**DR** = Dragon Rush'
    shStr = '**SD** = Super Dash'
    mhStr = '**MH** = Vanish'
    lmhsStr = '**SP** = Sparking'
    stateStr = lmStr + '\n' + shStr + '\n' + mhStr + '\n' + lmhsStr + '\n'

    dbfz_glossary_url = 'https://www.couchwarriors.org/welcome-to-dragonball-fighterz-a-beginners-guide/'
    thumbnail = 'http://i.imgur.com/bLLr0sj.png'
    embed = discord.Embed(title="Dragon Ball Fighter Z Notations",
                          colour=discord.Colour(0x7fffd4),
                          url=dbfz_glossary_url,
                          description="A list of dragon ball fighter z notations")
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name='Directions', value=directionStr)
    embed.add_field(name='Attack', value=attackStr)
    embed.add_field(name='State', value=stateStr)

    return embed
