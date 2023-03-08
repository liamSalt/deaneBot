import discord
import search
import randomArticle
import birdh
from discord.ext import commands
import gDrive



client = commands.Bot(command_prefix = ",")



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game("with words | ,help"))
    print("Bot is ready")



    
@client.command(brief="Defines a search term | .define [query]",aliases=['def'])
async def define(ctx,*,query=""):
    query=query.lower().replace(' ','').replace("'",'')

    embed = discord.Embed(
                                                                
        colour = discord.Colour.blue()
    )

    
    
    if len(query)==7 and query[:-1] in ["random"]: #random article starts with letter
        result = randomArticle.randomArticle(query[-1])
        embed.add_field(name="Define",value='**'+result[0]+'**'+'\n'+result[1],inline=False)
        embed.set_author("-------------------------------------------------------")
        
        await ctx.send(embed=embed)
        #await ctx.send('**'+result[0]+'**'+'\n'+result[1])
    elif query in ["","random"]: #random article starts with any letter
        result = randomArticle.randomArticle()
        embed.add_field(name="Define",value='**'+result[0]+'**'+'\n'+result[1],inline=False)
        
        await ctx.send(embed=embed)
        #await ctx.send('**'+result[0]+'**'+'\n'+result[1])
    elif search.isSubject(query[:5]) or search.isSubject(query[:4]) or search.isSubject(query[:3]): #check if starts with course code
        result = search.searchLocal(query,'./CourseCodes/')
        embed.add_field(name="Course Code "+'**'+query+'**',value=result,inline=False)
        embed.set_author("-------------------------------------------------------")
        
        await ctx.send(embed=embed)
        
    else:
        
        result = search.searchLocal(query) #check added definitions
        if result == "not found":
            result = search.searchEncy(query) #check queen's encyclopedia
            embed.add_field(name="Define",value='**'+result[0]+'**'+'\n'+result[1],inline=False)
            string = "_"  
            embed.set_author(name=string*40)
            embed.set_footer(text=string*47)
            await ctx.send(embed=embed)
        else:
            embed.add_field(name="Define "+'**'+query+'**',value=result,inline=False)
            embed.set_author("-------------------------------------------------------")
            
            await ctx.send(embed=embed)

@client.command(brief="Fetches grade distribution from quBirdhunter 2018-19",aliases=['bh'])
async def bird(ctx,*,query=""):
    embed = discord.Embed(
                                                                 
        colour = discord.Colour.green()
    )
    result = birdh.haveDistro(query)
    embed.add_field(name="QU Birdhunter 2018-19",value=result,inline=False)
    embed.set_author("-------------------------------------------------------")
    
    
    await ctx.send(embed=embed)
    


@client.command(brief="add custom definitions | .add name,alias1,alias2: definition)",description="use .add alias word:existing def to expand existing keywords")
@commands.has_role('Moderators')
async def add(ctx,*,definition=""):
    query = definition.split(":")
    if definition == "" or len(query)!=2 or query[1].rstrip()=="":
        await ctx.send("**Error**\n Format: .add name,alias1,alias2: definition")


            
        
    else:
        
        if query[0][:5].lower()=='alias': #.add alias thing,thing1,thing2:existing word
            
            query[0] = query[0][5:]
            query[0]=query[0].replace(" ","").replace("'","")
            Local = search.searchLocal(query[1]) #check local defs
            courses = search.searchLocal(query[1],'./CourseCodes/') #check course codes
            ency = search.searchEncy(query[1]) #check encyclopedia

            if Local !="not found":
                query[1] = Local
            elif courses!= "not found":
                query[1] = courses
            elif ency!="error":
                query[1] = '**'+ency[0]+'**'+'\n'+ency[1]

        aliases = query[0].split(',')
        for alias in aliases:
            print(alias)
            file = open('./Definitions/'+alias[0]+'.txt','a')
            file.write(alias.lower().replace(" ",'')+":"+query[1].replace("https","")+";\n")
            file.close()
            gDrive.addRow(alias.lower().replace(" ",''),query[1].replace("https","")) #add to drive
        await ctx.send("added!")
'''            
@client.command(brief="Saves New definitions from Google Drive"))
@commands.has_role('Moderators')
async def syncDrive(ctx):
    gDrive.saveNewRows()
'''

@client.command(brief="purge messages from chat")
@commands.has_role('Moderators')
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount+1)

token = open('token.txt').read()
client.run(token)
