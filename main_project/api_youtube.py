#!/usr/bin/env python
# coding: utf-8

# In[33]:


from googleapiclient.discovery import build
import numpy as np
import re
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

youTubeApiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

youtube=build('youtube', 'v3', developerKey=youTubeApiKey)

#extraindo videos de uma playlist 
#aqui só poderás entrar a parte depois da palavra LIST na url da playlist
playlistId = 'PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4'
playlist_Name = 'lex_videos'
nextPage_token = None


# In[34]:


playlist_videos = []

while True:
    res = youtube.playlistItems().list(part='snippet', playlistId = playlistId, maxResults=50, pageToken=nextPage_token).execute()
    playlist_videos += res['items']
  
    nextPage_token = res.get('nestPageToken')
    
    print(len(playlist_videos))

    if nextPage_token is None:
        break
        

    


# In[35]:


print(playlist_videos[2])


# In[36]:


videos_ids = list(map(lambda x: x['snippet']['resourceId']['videoId'], playlist_videos))
videos_ids


# In[37]:


stats = []
for video_id in videos_ids:
    res = youtube.videos().list(part='statistics', id=video_id).execute()
    stats+=res['items']
stats


# In[ ]:





# In[38]:


# exemplo para ver o que acontece se eu pegar a descrição do primeiro vídeo
descricao = list(map(lambda x: x['snippet']['description'], playlist_videos))
print(descricao[0])


# In[39]:


# exemplo para a separação dos assuntos em listas
# esse exemplo é do primeiro vídeo.
assuntos = re.findall(r'[0-9]+:[0-9]*.+', descricao[0])
assuntos


# In[40]:


# vamos criar uma listas de listas,para armazenar todos os assuntos
lista_assuntos = []
for numero_video in range(0,50):
    assunto = re.findall(r'[0-9]+:[0-9]*.+', descricao[numero_video])
    lista_assuntos.append(assunto)
    
lista_assuntos


# In[41]:


# agora que temos uma lista de todos os assuntos dos últimos 50 vídeos, vamos pegar os princioapis assuntos para fzr a estatística
assuntos_destaques = ['dollar','Bitcoin','Satoshi Nakamoto','wars','network', 'Ethereum', 'Tesla','Elon Musk','Deep Fakes','AWS','Book','recommendations','currency Money','AI','Leadership','Learning','Artificial intelligence','Blockchain','NFTs','quantum computers','Mars','Robots','Nuclear','SpaceX','programming','JavaScript','TypeScript','HTML5','Python','C#','Ruby','startups','physics','Machine learning']

#criando um dicionário para fzr a contagem:
contador_assuntos={}


for x in assuntos_destaques:
    contador_assuntos[x]=0
contador_assuntos
    


# In[42]:


# testando para o primeiro vídeo
lista= lista_assuntos[0]
for num in range(0,len(assuntos_destaques)):
    for c in lista:
        if assuntos_destaques[num] in c:
            contador_assuntos[assuntos_destaques[num]]+=1
            
print(contador_assuntos)
        


# In[43]:


#como vimos que funcionou, vamos fazer para todos os vídeos:
cont=0
while cont<50:
    for num in range(0,len(assuntos_destaques)):
        for c in lista_assuntos[cont]:
            if assuntos_destaques[num] in c:
                contador_assuntos[assuntos_destaques[num]]+=1
    cont+=1


df_assuntos= pd.DataFrame(list(contador_assuntos.items()),columns=['Assuntos','Quant. citações'])

df_assuntos


    


# # Fazendo a estatística
# 

# In[44]:


video_titulo = list(map(lambda x: x['snippet']['title'], playlist_videos))
print(video_titulo)


# In[45]:


#para sabermos os nomes, vamos utilizar expressões regurales

nomes_entrevistados=[]
for hj in video_titulo:
    nomes_entrevistados.append(re.findall(r'(.+\S+):', hj)) #expressão regular para pegar todas as letras antres de :

print(nomes_entrevistados)


# In[46]:



# vamos fazer agora da data de publicação, quantidade de curtidas, descurtidas, visualizações, comentários.
data_publicacao= list(map(lambda x: x['snippet']['publishedAt'], playlist_videos))
curtidas= list(map(lambda x: x['statistics']['likeCount'], stats))
descurtidas=list(map(lambda x: x['statistics']['dislikeCount'], stats))
visualizacoes=list(map(lambda x: x['statistics']['viewCount'], stats))
comentarios= list(map(lambda x: x['statistics']['commentCount'], stats))

print(data_publicacao, curtidas, descurtidas,visualizacoes,comentarios)


# ## criando o dataframe principal

# In[47]:


# Mas antes de criarmos o dataframe, vamos converter as estatísticas que estão como strings para inteiros
#o método que eu encontrei mais eficaz para isso é usando a função map (int, arg)


curtidas1= list(map(int, curtidas))
descurtidas1=list(map(int, descurtidas))
visualizacoes1=list(map(int, visualizacoes))
comentarios1= list(map(int, comentarios))






Lex_df = pd.DataFrame({
    'Entrevistado':nomes_entrevistados,
    'Assuntos': lista_assuntos,
    'Descrição': descricao,
    'Data de publicação':data_publicacao, 
    'Visualizações':visualizacoes1,
    'Curtidas':curtidas1,
    'Descurtidas':descurtidas1,
    'Comentários':comentarios1
    
    
})

# vamos arrumar o horário
Lex_df['Data de publicação']=pd.to_datetime(Lex_df['Data de publicação'])


Lex_df


# # Visualização dos dados

# In[ ]:





# In[48]:


#vamos fazer um filtro dos assuntos mais comentados
#vamos lembrar que df_assuntos é o dataframe dos assuntos mais citados



# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots(figsize=(10,15))

# Example data
assunto = df_assuntos['Assuntos']
y_pos = np.arange(len(assunto))
citacao = df_assuntos['Quant. citações']


ax.barh(y_pos, citacao, align='center', color='b')
ax.set_yticks(y_pos)
ax.set_yticklabels(assunto)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Citações')
ax.set_title('ASSUNTOS MAIS FALADOS NO PODCAST DE LEX FRIDMAN')

plt.show()




# In[49]:


#comparando a quantidade de likes com deslikes

fig, ax = plt.subplots(figsize=(15,7))
rects1 = ax.bar('Data de publicação', 'Curtidas', label='LIKES', width=2, color='g', data=Lex_df)
rects2 = ax.bar('Data de publicação', 'Descurtidas', label='DESLIKES', width=2,color='r', data=Lex_df)



ax.set_title('CURTIDAS CO DESCURTIDAS EM CADA VÍDEO')
ax.legend()


fig.tight_layout()

plt.show()


# In[50]:


# top 5 videos com mais visualizações

somatório_vis = 0
for x in visualizacoes1:
    somatório_vis+=x
    
print('o somatório de visualização dos últimos 50 vídeos é', somatório_vis)

videos_mais_vistos= Lex_df.sort_values(['Visualizações'], ascending=False)

top5_videos_mais_vistos=videos_mais_vistos[0:5]
top5_videos_mais_vistos


# In[51]:


# PARA SABERMOS AS PROPORÇÕES, TEREMOS QUE SABER O SOMATÓRIO DE VISUALIZAÇÕES TOTAL.



top_5_vis= list(top5_videos_mais_vistos['Visualizações']) #transformando as visualizações dos 5 mais vistos em uma lista 

soma_top_5 = sum(top_5_vis)



labels = 'Dan Carlin', 'Joe Rogan', 'Avi Loeb', 'Tim Dillon','Eric Weinstein', 'Outros'
sizes = [top_5_vis[0]*100/somatório_vis, top_5_vis[1]*100/somatório_vis,top_5_vis[2]*100/somatório_vis, top_5_vis[3]*100/somatório_vis,top_5_vis[4]*100/somatório_vis, 64] 


fig1, ax1 = plt.subplots(figsize=(15,15))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('ENTREVISTADOS MAIS VISTOS')

plt.show()


# In[ ]:





# In[52]:



plt.figure(figsize=(15,15))

# visualização
plt.subplot(221)
plt.bar('Data de publicação', 'Visualizações', width=5, data=Lex_df)
plt.ylabel('quantidade de visualização (milhão)')
plt.title('Visualização')


#comentario
plt.subplot(222)
plt.bar('Data de publicação', 'Comentários', width=5, color='b', data=Lex_df)
plt.ylabel('quantidade de Comentários')
plt.title('Comentários')


#deslike
plt.subplot(223)
plt.bar('Data de publicação', 'Descurtidas', color='r', width=5, data=Lex_df)
plt.ylabel('quantidade de Descurtidas')

plt.title('Descurtidas')


# like
plt.subplot(224)
plt.bar('Data de publicação', 'Curtidas', width=5, color='g', data=Lex_df)
plt.ylabel('quantidade de curtidas')
plt.title('Curtidas')


plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()


# In[ ]:





# In[54]:


#Analisando as melhores datas para lançar um vídeo
plt.figure(figsize=(15,15))

plt.plot('Data de publicação', 'Visualizações', 'o-', color='g', label='VISUALIZAÇÕES' ,data=Lex_df)

plt.title('Data de lançamento  x Curtidas')
plt.xlabel('Data de publucação do vídeo')
plt.ylabel('VISUALIZAÇÕES (milhão)')
plt.legend()
plt.fill_between('Data de publicação', 'Visualizações', data=Lex_df)
plt.show()


# In[55]:


# Criando o número de curtidas por data de lançamento
plt.figure(figsize=(15,15))

plt.plot('Data de publicação', 'Curtidas', 'o-', color='b', label='Número de curtidas' ,data=Lex_df)

plt.title('Número de curtidas  x  Data de publicação')
plt.xlabel('Data de publucação do vídeo')
plt.ylabel('Quantidade de curtidas')
plt.legend()
plt.fill_between('Data de publicação', 'Curtidas', data=Lex_df)
plt.show()


# In[ ]:





# In[ ]:




